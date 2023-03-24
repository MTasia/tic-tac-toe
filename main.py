import numpy as np
import cv2

from find_play_field import find_play_field
from play import play


def main():
    counter = 0
    n = 3

    robot = 1
    # если про первой итерации поле путое - 1 ходит робот крестиками (по дефолту робот ходит первым)
    # если на поле уже есть крестик, то робот ходит вторым ноликами

    steps = 2
    while counter < steps:
        img = cv2.imread('photo/tic3.jpg')

        field = find_play_field(img)
        print(field)

        if counter == 0:
            for i in range(n):
                for j in range(n):
                    if field[i][j] != 0:
                        robot = 2


        next_field = play(field, robot)
        print(next_field)

        counter += 1
        print()


if __name__ == '__main__':
    main()
