from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
from emailpy import send_email
import json
import pandas as pd

from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 

class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 
	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]

class ActionCheckLocation(Action):
  def name(self):
    return 'action_check_location'
    
  def run(self, dispatcher, tracker, domain):
    config={ "user_key":"<Enter Key"}
    zomato = zomatopy.initialize_app(config)
    loc = tracker.get_slot('location')
    loc_valid=False
    loc_operational=False
    tier_1_2_cities = ['bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 'coimbatore', 'nagpur', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 'pondicherry', 'purulia', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virarcity', 'vijayawada', 'vellore', 'warangal', 'surat', 'visakhapatnam'] # Wikipedia January 2020
    valid=zomato.check_city_valid(loc) ##(valid_city,valid_country)
    if(valid[0]): # if valid
      # dispatcher.utter_message("Looking for "+str(loc).lower()+"  in list")
      if(loc.lower() in tier_1_2_cities):
        loc_operational=True
      loc_valid=True
    else: # if city name not in zomato database
      # dispatcher.utter_message("couldn't find "+str(loc).lower()+" anywhere")
      loc_valid=False
      loc_operational=False
    
    return [SlotSet('location_valid',loc_valid),SlotSet('location_operational',loc_operational)]

class ActionSearchRestaurants(Action):
  def name(self):
    return 'action_search_restaurants'
    
  def run(self, dispatcher, tracker, domain):
    config={ "user_key":"<Enter Key"}
    found_restaurants=True
    zomato = zomatopy.initialize_app(config)
    loc = tracker.get_slot('location')
    cuisine = tracker.get_slot('cuisine')
    budget = tracker.get_slot('budget')
    priceMin=0
    priceMax=1000000
    if(budget=="<300"):
      priceMax=299
    elif(budget=="300-700"):
      priceMin=300
      priceMax=699
    else:
      priceMin=700
    location_detail=zomato.get_location(loc, 1)
    d1 = json.loads(location_detail)
    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]
    cuisines_dict={'american':1,'mexican':73,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
    results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50) ## get a list of 50 restaurants then filter top 5 by budget
    d = json.loads(results)
    # try: ## WHen API limits exceeded
    if d['results_found'] == 0:
        response= "no results"
        dispatcher.utter_message("Sorry, We couldn't find any "+str(cuisine)+" restaurants in "+str(loc)+".")
        found_restaurants=False

    else:
      r_data=[]
      for i,r in enumerate(d["restaurants"]):
        r_l=[]
        cost_for_two=int(r['restaurant']['average_cost_for_two'])
        if(cost_for_two>=priceMin and cost_for_two<=priceMax):
          r_l.append(r['restaurant']['id'])
          r_l.append(r['restaurant']['name'])
          r_l.append(float(r['restaurant']['user_rating']['aggregate_rating']))
          r_l.append(cost_for_two)
          r_l.append(r['restaurant']['location']['address'])
          r_data.append(r_l)
      df=pd.DataFrame(data=r_data,columns=["ID","Name","Rating","Avg_Cost_for_Two","Address"])
      df.set_index('ID', inplace=True)
      df=df.sort_values('Rating',ascending=False)
      if(len(df.Name)>=5): 
        response="Top 5 "+str(cuisine)+" restaurants near "+str(loc)+" are: \n"
        for i in range(5):
          response+=str(i+1)+" "+df.Name[i]+" in "+df.Address[i]+" has been rated "+str(df.Rating[i])+" \n"
      elif(len(df.Name)>0 and len(df.Name)<5):  # Couldn't find 5 restaurants
        response="Sorry we could not find enough restaurants with given details \n"
        response+="Top "+str(len(df.Name))+" "+str(cuisine)+" restaurants near "+str(loc).rstrip()+" are: \n"
        for i in range(len(df.Name)):
          response+=str(i+1)+" "+df.Name[i]+" in "+df.Address[i]+" has been rated "+str(df.Rating[i])+" \n"
      else:
        response="Sorry, We couldn't find any restaurants matching your requirements."
        found_restaurants=False
    # except:
    #   dispatcher.utter_message("Sorry, We couldn't find any "+str(cuisine)+" restaurants in "+str(loc)+".")
    #   found_restaurants=False
    dispatcher.utter_message(response)
    return [SlotSet('found_restaurants',found_restaurants)]

class ActionSearchRestaurantsTopTen(Action):
  def name(self):
    return 'action_send_email'

  def run(self, dispatcher, tracker, domain):
    mail_status=False
    config={ "user_key":"<Enter Key"}
    zomato = zomatopy.initialize_app(config)
    loc = tracker.get_slot('location')
    cuisine = tracker.get_slot('cuisine')
    user_domain = tracker.get_slot('email')
    found_restaurants = tracker.get_slot('found_restaurants')
    name = user_domain.split('@')[0]
    location_detail=zomato.get_location(loc, 1)
    d1 = json.loads(location_detail)
    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]
    cuisines_dict={'american':1,'mexican':73,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
    budget = tracker.get_slot('budget')
    priceMin=0
    priceMax=1000000
    if(budget=="<300"):
      priceMax=299
    elif(budget=="300-700"):
      priceMin=300
      priceMax=699
    else:
      priceMin=700
    results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50) ## get a list of 50 restaurants then filter top 5 by budget
    d = json.loads(results)
    if d['results_found'] == 0:
        response= "no results"
    else:
      r_data=[]
      for i,r in enumerate(d["restaurants"]):
        r_l=[]
        cost_for_two=int(r['restaurant']['average_cost_for_two'])
        if(cost_for_two>=priceMin and cost_for_two<=priceMax):
          r_l.append(r['restaurant']['id'])
          r_l.append(r['restaurant']['name'])
          r_l.append(float(r['restaurant']['user_rating']['aggregate_rating']))
          r_l.append(cost_for_two)
          r_l.append(r['restaurant']['location']['address'])
          r_data.append(r_l)
      df=pd.DataFrame(data=r_data,columns=["ID","Name","Rating","Avg_Cost_for_Two","Address"])
      df.set_index('ID', inplace=True)
      df=df.sort_values('Rating',ascending=False)
      if(found_restaurants==True):
        if(len(df.Name)>=10): 
          response="Top 10 "+str(cuisine)+" restaurants near "+str(loc)+" are: \n"
          for i in range(10):
            response+=str(i+1)+" "+df.Name[i]+" in "+df.Address[i]+" has been rated "+str(df.Rating[i])+". Average Cost for Two is Rs. "+str(df.Avg_Cost_for_Two[i])+". \n"
          mail_status=True
          send_email(name,user_domain,response)
        elif(len(df.Name)>0 and len(df.Name)<10):  # Couldn't find 10 restaurants
          response="All "+str(cuisine)+" restaurants near "+str(loc).rstrip()+" are: \n"
          for i in range(len(df.Name)):
            response+=str(i+1)+" "+df.Name[i]+" in "+df.Address[i]+" has been rated "+str(df.Rating[i])+". Average Cost for Two is Rs. "+str(df.Avg_Cost_for_Two[i])+". \n"
          mail_status=True
          send_email(name,user_domain,response)
        dispatcher.utter_message("Mail Sent!")
      else:
        mail_status=False
        dispatcher.utter_message("Sorry.No restaurants found")
    # dispatcher.utter_message(response)
    return [SlotSet('mail_sent',mail_status)]
