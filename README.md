# Project Readme: Jetson-Inference Image Capture and Texting

This project uses Jetson-Inference and Twilio to capture an image and text it to a desired phone number upon detecting a specific item.

## Prerequisites
- Jetson board with JetPack SDK
- Python 3.x
- Jetson-Inference library
- Twilio account

## Setup
1. Clone Jetson-Inference repository.
2. Install Python dependencies.
3. Configure Twilio API credentials in `detectnet-camera.py`.
4. Specify the desired phone number in `detectnet-camera.py`.

## Usage
1. Connect a camera or webcam to your Jetson board.
2. Run `detectnet-camera.py`.
3. Monitor the terminal for detection alerts and image capture notifications.

## Customization
- Modify the detection model, item of interest, and add additional functionality as needed.

## Troubleshooting
- Refer to the documentation and support resources for Jetson-Inference and Twilio.
- Ensure internet connectivity on the Jetson board.

## Disclaimer
- Use this project at your own risk.
- Consider privacy and legal aspects when capturing and transmitting images via text messages.
