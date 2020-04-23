import twilio.rest
from twilio.rest import Client
account_sid = 'ACd6aad6cb6e31bb8fc324d95e7142c763'
auth_token = 'a1221b507dea4800bd00c7a3d221c4e8'
client = Client(account_sid, auth_token)

 

message = client.messages \
    .create(
         body='',
         from_='+19798032727',
         to='+919818225401'
     )

 

print(message.sid)
