from twilio.rest import Client
import requests
import os

def get_ngrok_url():
    ngrok_url = 'http://localhost:4040/api/tunnels'
    response = requests.get(ngrok_url)
    data = response.json()
    forwarding_url = data['tunnels'][0]['public_url']
    
    return forwarding_url

def create_twilio_client():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    return Client(account_sid, auth_token)

def send_image_mms():
    client = create_twilio_client()
    image_url = str(get_ngrok_url()) + '/media/detection.jpg'

    message = client.messages.create(
        from_ = os.environ['TWILIO_PHONE_NUM'],
        media_url =[ image_url],
        to = os.environ['PERSONAL_NUM']
    )

