import cv2


def capture_camera(cap):
    ret, frame = cap.read()

    # while True:
    #     ret, frame = cap.read()
    #     cv2.imshow("from camera", frame)
    #     cv2.waitKey(1)

    return frame
