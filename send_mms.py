from twilio.rest import Client
import os

def create_twilio_client():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    return Client(account_sid, auth_token)

def send_image_mms():
    client = create_twilio_client()
    image_url = 'https://cd85-50-109-244-47.ngrok-free.app/media/detection.jpg'

    message = client.messages.create(
        from_='+18336934531',
        media_url=[image_url],
        to='+15034737870'
    )

    print(message.sid)

# call the send_image_mms function
# send_image_mms()
