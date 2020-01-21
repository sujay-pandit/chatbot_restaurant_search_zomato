## Rasa based chat bot to recommend restaurants using Zomato API

### - Features:
```
- restaurant search using zomato API
- sending emails to user with additional details
```
### - Requirements:

#### -- Install Rasa and RasaX : 
`pip install rasa-x --extra-index-url https://pypi.rasa.com/simple`
#### -- Rasa NLU and Spacy : 
`pip install rasa[spacy]`
`python -m spacy download en_core_web_md`
`python -m spacy link en_core_web_md en`
#### -- ZomatoAPI:
You can generate an API key from https://developers.zomato.com/api (max 1000 API calls/day). 

### - Steps to chat with pre-trained bot: 
```
- CLI-1
-- rasa run actions
- CLI-2
-- rasa shell
```
### - Steps to interactively train:
```
- CLI-1
-- rasa run actions
- CLI-2
-- rasa interactive
```
Exported stories will be available in data/stories.md

### - Additional details:
```
- add your email-id in emailpy.py
- add zomato API key in actions.py
```
