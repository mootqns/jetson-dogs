import os
import sys
import jetson_inference
import jetson_utils
import send_mms

def start_detection():
    net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.85)
    camera = jetson_utils.gstCamera(2592, 1944, "/dev/video0")
    display = jetson_utils.glDisplay()

    obj_detected = False  # flag to track detection status

    # specify the custom file path
    file_path = "media"

    while display.IsOpen():
        img, width, height = camera.CaptureRGBA()

        detections = net.Detect(img, width, height)

        # check if any person detection is present
        obj_present = any(net.GetClassDesc(d.ClassID) == "dog" for d in detections)

        if obj_present and not obj_detected:
            print('person detected')
            obj_detected = True

            # generate a unique image filename
            image_name = "detection.jpg"
            image_path = os.path.join(file_path, image_name)

            # save the image when person is detected
            jetson_utils.saveImageRGBA(image_path, img)

            # mms image
            send_mms.send_image_mms()

            # exit
            sys.exit()

        elif not obj_present and obj_detected:
            print('person undetected')
            obj_detected = False

        display.RenderOnce(img, width, height)
        display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

start_detection()