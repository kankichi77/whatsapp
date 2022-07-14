## WhatsApp Messager wrapper for python

### Requirements:
- Python 3

### Usage:
```
import whatsapp

ENDPOINT = 'https://graph.facebook.com/v13.0/XXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TO_NUMBER = 'XXXXXXXX'
TEMPLATE_NAME = 'TEMPLATE_NAME'

wam = whatsapp.Message(url = ENDPOINT, token = ACCESS_TOKEN)
wam.set_data(to=TO_NUMBER, template_name=TEMPLATE_NAME)
print(wam.send())
```
