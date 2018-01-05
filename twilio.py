from twilio.rest import TwilioRestClient
# Your Account SID from twilio.com/console
account_sid = "ACc6f8ade7555ee1a7f24b2bdd4e8c6209"
# Your Auth Token from twilio.com/console
auth_token  = "32860a0736f781792ea54c212307d6a3"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Hey asshole you got my sister pregrent, what are you going to do about it!",
    to="+16501990355", 
    from_="+12092104153")
print(message.sid)