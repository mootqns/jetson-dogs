# Project Readme: Jetson-Inference Image Capture and Texting

This project uses Jetson-Inference and Twilio to capture an image and text it to a desired phone number upon detecting a specific item.

## Prerequisites
- NVIDIA Jetson Xavier AGX with JetPack SDK
- Python 3.x
- Jetson-Inference library
- Twilio account

## Setup
1. Clone Jetson-Inference repository.
2. Install Python dependencies.
3. Configure Twilio API credentials as enviroment variables
4. Specify the desired phone number in `my-detection.py`.

## Usage
1. Connect a camera or webcam to your Jetson board.
2. Run `my-detection.py`.
3. Monitor the terminal for detection alerts and image capture notifications.
