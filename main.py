import numpy as np
import cv2

from find_play_field import find_play_field
from play import play, create_field
from utils.const import *
from utils.helps import *


def main():
    counter = 0

    robot = X
    player = O
    field = create_field(robot)
    print_m(field)

    steps = 1
    while counter < steps:
        img = cv2.imread('photo/tic3.jpg')

        detect_field = find_play_field(img)
        print_m(detect_field)

        for i in range(N):
            for j in range(N):
                if detect_field[i][j] == NON:
                    detect_field[i][j] = field[i][j]

        field, status = play(detect_field, robot, player)
        print_m(field)

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
