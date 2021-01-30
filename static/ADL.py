import requests
from config import HostConfig

#define variables to url
list_url = 'http://' + HostConfig.IP + '/rtLog/v1.0/list';

# Simple list function
def list():
  myResponse = requests.get(list_url);
  print (myResponse.status_code)

  # For successful API call, response code will be 200 (OK)
  if(myResponse.ok):

    respData = myResponse.content;

    return respData;

  else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()

# call list()
respData = list();
# format respData into HTML table
print "calling json2html.."
from json2html import *
htmldata = json2html.convert(json = respData);
f = open('data.html','w');
f.write(htmldata);
f.close();
