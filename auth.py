"""

Script that logs into Cisco DNA Center Always on Sandbox and 
retrieves and authentication token.


"""

#import requests library and basic HTTP auth to pass a username and password

import requests
from requests.auth import HTTPBasicAuth

#Defines global variables we don't want changed

USER = "devnetuser"
PASS = "Cisco123!"
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"


#Create dictionary for the resposne payload, headers, in this we are doing an http post
#so we need to specify the content type we are sending rather than accepting a format

headers = {'Content-Type': 'application/json'}

#creates a response variable with the value of our post request notice this is a post not a get
#which is different than what we have been doing so far we are sending the server something not
#asking for it.  Also note we are passing a username and password and lastly as you will notice
#in the next lab we have set verify to false this is because DNA Center is using a self signed
#certificate and we are aware so we want to accept the risk and continue
#THIS SHOULD NOT BE DONE IN A PRODUCTION ENVIRONMENT IT IS A SECURITY ISSUE!!!!

response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

#converts our respone to json format and stores it in our variable resposneJSON

responseJSON = response.json()

#prints responseJSON variable

print(responseJSON)