# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACb3491848fff896e1e3a46ea6476d3b85'
auth_token = 'f71dfa84c61c8972c7cbff2df15b1387'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="Here is your payment link please click it\nhttps://alhamra.ae/",
         from_='whatsapp:+14155238886',
         to='whatsapp:+918903600437'
     )

print(message.sid)
