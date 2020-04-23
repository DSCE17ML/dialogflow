from twilio.rest import Client
account_sid = 'ACd6aad6cb6e31bb8fc324d95e7142c763'
auth_token = '6149e48e0f3fa1a6cd3f0a39030b8919'
client = Client(account_sid, auth_token)

 

message = client.messages \
    .create(
         body='Hi, call to check a postman.',
         from_='+19798032727',
         to='+919818225401'
     )

 
print("Sent")
print(message.sid)
