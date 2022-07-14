## WhatsApp Messaging wrapper for python.

### Requirements:
- Python 3

### Usage:

from whatsapp import WhatsApp_Message

ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ENDPOINT = 'https://graph.facebook.com/v13.0/XXXXXXXXXXXX'
TO_NUMBER = 'XXXXXXXX'
TEMPLATE_NAME = 'TEMPLATE_NAME'

wam = WhatsApp_Message(url = ENDPOINT, token = ACCESS_TOKEN)
wam.set_data(to=TO_NUMBER, template_name=TEMPLATE_NAME)
print(wam.send())
