import requests, json

class Message():
  def __init__(self, url, token):
    self.url = url
    self.token = token
    self.data = None

  @property
  def headers(self):
    if self.token:
      return {
        'Authorization': 'Bearer ' + self.token,
        'Content-Type': 'application/json'
      }
    else:
      return None

  def set_data(self, to, template_name):
    self.data = {
      'messaging_product': 'whatsapp', 
      'to': to, 
      'type': 'template', 
      'template': 
      { 
        'name': template_name, 
        'language': 
        { 
          'code': 'en_US'
        } 
      } 
    }
  
  def send(self):
    output_json = requests.post(self.url, data = json.dumps(self.data), headers = self.headers).json()
    return json.dumps(output_json, indent=2)
