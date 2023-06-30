import numpy as np
import cv2

from camera import capture_camera
from find_play_field import find_play_field
from play import play, create_field
# from camera import capture_camera
from utils.const import *
from utils.helps import *


def main():
    counter = 0
    robot = X
    player = O
    field = create_field(robot)
    # print_m(field)

    steps = 1
    # while True:
    while counter < steps:
        # frame = capture_camera()
        # cv2.imwrite("image.jpg", frame)
        # cv2.imshow("from camera", frame)
        # cv2.waitKey(0)
        img = cv2.imread('../real_photo/test2.png')

        # for test image cut off the bottom of the sheet and rotate to 180 deg
        w, h = img.shape[:2]
        crop_left = 500
        crop_right = 30
        img = img[0: w, crop_left: h - crop_right]
        # img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("first cut off for rela photo", img)
        cv2.waitKey(0)

        detect_field = find_play_field(img)
        print("detecting field")
        print_m(detect_field)

        for i in range(N):
            for j in range(N):
                if detect_field[i][j] == NON:
                    detect_field[i][j] = field[i][j]

        field, status = play(detect_field, robot, player)
        # print("robot made a move")
        # print_m(field)

        print("robot made a move")
        field_user = field_for_user(field)
        print_m(field_user)

        if status == ROBOT_WIN:
            print(ROBOT_WIN)
            break
        if status == PLAYER_WIN:
            print(PLAYER_WIN)
            break

        counter += 1
        print()


if __name__ == '__main__':
    main()
