# Jetson-Inference Image Capture and Texting

This project uses Jetson-Inference and Twilio to capture an image and text it to a desired phone number upon detecting a specific item.

## Prerequisites
- NVIDIA Jetson Developer Kit with JetPack SDK
- Python 3.x
- Jetson-Inference library
- Twilio account
- Ngrok account 

## Setup
1. Clone Jetson-Inference repository.
2. Install Python dependencies.
3. Configure Twilio API credentials as enviroment variables.
4. Specify the desired phone number in `my-detection.py`.
5. Execute 'ngrok http 5000' in terminal.
6. Ensure ngrok forwarding url matches image_url in send_mms.py.

## Usage
1. Connect a camera or webcam to your Jetson Developer Kit. 
2. Run 'flask_app.py'.
3. Run `my-detection.py`.
4. Monitor the terminal for detection alerts and image capture notifications.
