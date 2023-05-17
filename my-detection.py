import os
import jetson_inference
import jetson_utils

net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.85)
camera = jetson_utils.gstCamera(2592, 1944, "/dev/video0")
display = jetson_utils.glDisplay()

person_detected = False  # flag to track detection status

# specify the custom file path
file_path = "media"

while display.IsOpen():
    img, width, height = camera.CaptureRGBA()

    detections = net.Detect(img, width, height)

    # check if any person detection is present
    person_present = any(net.GetClassDesc(d.ClassID) == "dog" for d in detections)

    if person_present and not person_detected:
        print('person detected')
        person_detected = True

        # generate a unique image filename
        image_name = "detection.jpg"
        image_path = os.path.join(file_path, image_name)

        # save the image when person is detected
        jetson_utils.saveImageRGBA(image_path, img, width, height)

    elif not person_present and person_detected:
        print('person undetected')
        person_detected = False

    display.RenderOnce(img, width, height)
    display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

