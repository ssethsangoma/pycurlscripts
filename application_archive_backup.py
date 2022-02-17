import pycurl, json
from io import BytesIO
try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode



option = json.load(open("config.json"))

response=BytesIO()
url = 'http://{0}/SAFe/sng_rest/api/backup/application/archive/'.format(option["SERVER"])


#postmark_url = 'http://'/SAFe/sng_rest/api/backup/application/archive/'
headers = {'Content-Type': 'application/json',}

c = pycurl.Curl()
c.setopt(pycurl.WRITEFUNCTION, response.write)

post_body = {}
p = urlencode(post_body)

c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, ['X-API-KEY: {0}'.format(option["API_KEY"]),'Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, p)
c.perform()
c.close()

data=response.getvalue()
print(data)

