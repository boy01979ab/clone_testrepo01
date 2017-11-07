import SoftLayer

from pprint import pprint as pp

# Valid Softlayer username
USERNAME = 'smfg_api_infra-infra-dev'
# Valid Softlayer apiKey token, Generate one for you or your users, or view yours at https://control.softlayer.com/account/users
API_KEY = '5b754c07871d6ac20aebab16e428adbbed1b20e18e47046e92c0edeaf340a746'

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

userCustomerService = client['SoftLayer_User_Customer']
accountService = client['SoftLayer_Account']

objectMask='accountId, id, sslVpnAllowedFlag, username, firstName, lastName'
#add pptpVpnAllowedFlag to retrieve boolean value for the
# other VPN connection type.
objectMask2='username'

objectFilter={"users":{"sslVpnAllowedFlag":{"operation":"1"}}} 
#change values between 1=True and 0=False as required, this will retrieve only the users with a True value for a SSL VPN private network connection.

try:
    
    users = client['SoftLayer_Account'].getUsers()
    print "--------------------------------------------------------------------------------------------------------------------------------------"

    for x in users:

      name = x['username']

      if x['sslVpnAllowedFlag'] :

         print ("%s : enabled" % name)

      else :

         print ("%s : disabled" % name)

    print "--------------------------------------------------------------------------------------------------------------------------------------"

except SoftLayer.SoftLayerAPIError as e:

    print("Unable to retrieve all account's users information, please refer to following error:  . %s %s " %
          (e.faultCode, e.faultString))
