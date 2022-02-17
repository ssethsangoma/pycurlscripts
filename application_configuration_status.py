#  Retrieve network configuration
#  sbc --> configuration --> IP setings --> Accesis control list
#

import pycurl, json
from io import BytesIO

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

try:
  option = json.load(open("config.json"))

  response=BytesIO()
  base_url = 'http://{0}/SAFe/sng_rest/api/'.format(option["SERVER"])
  method_name = "status"
  module_name = "application"
  obj_type = "configuration"
  obj_name = ""
  url = base_url+method_name+'/'+module_name+'/'+obj_type+'/'+obj_name
  headers = {'Content-Type': 'application/json',}
  c = pycurl.Curl()
  c.setopt(pycurl.WRITEFUNCTION, response.write)

  c.setopt(pycurl.URL, url)
  if(option["API_KEY"]):
    c.setopt(pycurl.HTTPHEADER, ['X-API-KEY: {0}'.format(option["API_KEY"]),'Accept: application/json'])
  else:
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])

  c.setopt(pycurl.HTTPGET, 1)
  c.perform()
  data=response.getvalue()
  print(data)
except:
  exdata=response.getvalue()
  print("exeption has been found")
  print(exdata)
finally:
  c.close()

