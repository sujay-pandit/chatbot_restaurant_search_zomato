<!-- ## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye -->

<!-- ## interactive_email_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_email_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_email_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bombay"}
    - slot{"location": "Bombay"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Bombay"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_email_story_4
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_email_story_5
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"location": "bangalore"}
    - utter_goodbye

## interactive_email_story_6
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"location": "Bangalore"}
    - utter_goodbye

## interactive_email_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bombay"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bombay"}
    - action_search_restaurants
    - slot{"location": "Bombay"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"location": "Bombay"}
    - utter_goodbye

## interactive_email_story_8
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"location": "Mumbai"}
    - utter_goodbye

## interactive_email_story_9 + NO to more details
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_top_ten
* greet
    - utter_goodbye

## interactive_email_story_10 + NO to more details
* greet
    - utter_greet
* restaurant_search{"location": "Bombay"}
    - slot{"location": "Bombay"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "Bombay"}
    - utter_ask_top_ten
* greet
    - utter_goodbye

## interactive_email_story_11 + NO to more details
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_top_ten
* greet
    - utter_goodbye

## interactive_email_story_12 + NO to more details
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_top_ten
* greet
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
    - utter_ask_budget{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujay9629@gmail.com"}
    - slot{"email": "sujay9629@gmail.com"}
    - action_send_email
    - slot{"location": "Chennai"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - utter_ask_budget
    - action_search_restaurants{"budget": "<300"}
    - slot{"budget":"<300"}
    - slot{"location": "Delhi"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sb693@snu.edu.in"}
    - slot{"email": "sb693@snu.edu.in"}
    - action_send_email
    - slot{"location": "Delhi"}
    - utter_goodbye
* greet
    - utter_greet

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* send_email{"budget": "<300"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"location": "chennai"}
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "jello123@mymail.in"}
    - slot{"email": "jello123@mymail.in"}
    - action_send_email
    - slot{"location": "Hyderabad"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Indian", "location": "FARidabad"}
    - slot{"cuisine": "Indian"}
    - slot{"location": "FARidabad"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"location": "FARidabad"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"location": "FARidabad"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Uttar Pradesh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Uttar Pradesh"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "sujayrpi@gamil.com"}
    - slot{"email": "sujayrpi@gamil.com"}
    - action_send_email
    - utter_goodbye -->
<!-- ## self_framed_story_basic_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
    - action_check_location{"location":"Chennai"}
    - slot{"location":"Chennai}
    - slot{"location_valid":True,"location_operational":True}
    - utter_ask_budget
* restaurant_search{"budget":"300-700"}
    - slot{"budget":"300-700"}
    - action_search_restaurants
    - slot{"found_restaurants":True}
    - utter_ask_top_ten
* send_email{"more_info_desired":"Yes"}
    - slot{"more_info_desired":"Yes"}
    - utter_ask_email
* send_email{"email":"sujayrpi@gmail.com"}
    - slot{"email":"sujayrpi@gmail.com"}
    - action_send_email
    - utter_ask_continue{"mail_sent":True}
    - slot{"mail_sent":True}
* goodbye{"continue":"No"}
    - slot{"continue":"No"}
    - utter_goodbye

## basic_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_top_ten
* affirm
    - utter_ask_email
* send_email{"email": "jello123@mymail.in"}
    - slot{"email": "jello123@mymail.in"}
    - action_send_email
    - slot{"location": "Hyderabad"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": false}
    - utter_ask_continue
* greet{"continue":false}
    - slot{"continue":false}
    - utter_goodbye -->

<!-- ========================================================================= -->

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_basic
* greet
    - utter_greet
* restaurant_search{"location": "Faridabad"}
    - slot{"location": "Faridabad"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
* exit
    - utter_goodbye
    - action_restart

<!-- ## interactive_story__not_operational_continue
* greet
    - utter_greet
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* location_fix{"ask_location_again": "Yes"}
    - slot{"ask_location_again": "Yes"}
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

# interactive_story__not_operational_continue
* greet
    - utter_greet
* restaurant_search{"location": "New York"}
    - slot{"location": "New York"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* location_fix{"ask_location_again": "Yes"}
    - slot{"ask_location_again": "Yes"}
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

# interactive_story__not_operational_continue
* greet
    - utter_greet
* restaurant_search{"location": "Liverpool"}
    - slot{"location": "Liverpool"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* location_fix{"ask_location_again": "Yes"}
    - slot{"ask_location_again": "Yes"}
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart -->

## interactive_story_no_restaurant_found
* greet{"greet": "yello"}
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_search_restaurants
    - slot{"found_restaurants": false}
* exit
    - utter_try_again_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_search_restaurants
    - slot{"found_restaurants": false}
    - utter_try_again_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* exit{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_search_restaurants
    - slot{"found_restaurants": false}
    - utter_try_again_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "Kochi"}
    - slot{"cuisine": "American"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* exit{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* exit{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": false}
    - utter_try_again_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "Chennai"}
    - slot{"cuisine": "American"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* exit{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": false}
    - utter_try_again_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Hyderabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* exit{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Jaipur"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Jaipur"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Faridabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Faridabad"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Lucknow"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bombay"}
    - slot{"location": "Bombay"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Vellore"}
    - slot{"location": "Vellore"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet{"greet": "yello"}
    - utter_greet
* restaurant_search{"cuisine": "CHinese", "location": "Gurgaon"}
    - slot{"cuisine": "CHinese"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "chandinee.c@gmail.com"}
    - slot{"email": "chandinee.c@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chneeio"}
    - slot{"location": "chneeio"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chasdse"}
    - slot{"location": "chasdse"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "ghoul"}
    - slot{"location": "ghoul"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Punjab"}
    - slot{"location": "Punjab"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Cehnnai"}
    - slot{"location": "Cehnnai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_2
    - utter_greet
* restaurant_search{"location": "jaiusp"}
    - slot{"location": "jaiusp"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_2
    - utter_greet
* restaurant_search{"location": "Gurgayon"}
    - slot{"location": "Gurgayon"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujayrpi@gmail.com"}
    - slot{"email": "sujayrpi@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "dubai"}
    - slot{"location": "dubai"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "New York"}
    - slot{"location": "New York"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "China"}
    - slot{"location": "China"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "Ohio"}
    - slot{"location": "Ohio"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Orissa"}
    - slot{"location": "Orissa"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart


## interactive_story_1
* restaurant_search{"location": "Boston"}
    - slot{"location": "Boston"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Bombay"}
    - slot{"location": "Bombay"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "food"}
    - slot{"location": "food"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Russia"}
    - slot{"location": "Russia"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_2
    - utter_greet
* restaurant_search{"location": "sfadfarea"}
    - slot{"location": "sfadfarea"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujay9629@gmail.com"}
    - slot{"email": "sujay9629@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart

## interactive_story_3
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": false}
    - utter_no_operations
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - action_check_location
    - slot{"location_valid": true}
    - slot{"location_operational": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* continue{"more_info_desired": "No"}
    - slot{"more_info_desired": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_4
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location_valid": false}
    - slot{"location_operational": false}
    - utter_location_not_found
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"found_restaurants": true}
    - utter_ask_top_ten
* send_email{"more_info_desired": "Yes"}
    - slot{"more_info_desired": "Yes"}
    - utter_ask_email
* send_email{"email": "sujay9629@gmail.com"}
    - slot{"email": "sujay9629@gmail.com"}
    - action_send_email
    - slot{"mail_sent": true}
    - utter_goodbye
    - action_restart
