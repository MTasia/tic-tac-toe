import cv2
import socket
from camera import capture_camera
from find_play_field import find_play_field
from play import create_field, play
from robot.client import init_client, send_data, get_data
from utils.const import *
from utils.helps import field_for_user, print_m, matcing_filds, print_field, find_cell
from utils.img_helps import determ_figures

filed_Z = 73.53

center_field_X_cross = 413.35
center_field_Y_cross = 64.04

center_field_X_circle = 425.95
center_field_Y_circle = 54.68


def robot_moving(field, robot, player):
    old_filed = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            old_filed[i][j] = field[i][j]

    field, status = play(field, robot, player)

    field_i, field_j = find_cell(field, old_filed)
    print("Robot make a move to cell: ", field_i, field_j)
    return field, status, field_i, field_j


def get_img(cap):
    img = capture_camera(cap)
    # img = cv2.imread('real_photo/test0.png')

    # cropping image for detecting field
    w, h = img.shape[:2]
    crop_left = 500
    crop_right = 50
    img = img[0: w, crop_left: h - crop_right]
    # cv2.imshow("cropping img from camera", img)
    # cv2.waitKey(0)

    return img


def main():
    robot, player = X, O
    robot_step, player_step = True, False
    center_field_X, center_field_Y = center_field_X_cross, center_field_Y_cross

    is_ans = False
    while not is_ans:
        print('Do you want play first - X? (y/n)')
        ans = input()
        if ans == YES:
            is_ans = True
            print('Well! You are -' + X)
            robot, player = O, X
            robot_step, player_step = False, True
            center_field_X, center_field_Y = center_field_X_circle, center_field_Y_circle
        elif ans == N0:
            is_ans = True
            print('Well! You are -' + O)

    # creating field
    field = create_field(robot)

    # TODO: check, is robot ready to start
    print('Need run the prog on robot')
    print('Type anything, when you and robot will be ready to start')
    _ = input()

    cap = cv2.VideoCapture(0)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = init_client(client)
    print(res)

    send_data(client, robot)
    robot_ready_to_start = get_data(client)
    print(robot_ready_to_start)

    while True:
        if robot_step:
            field, status, field_iy, field_jx = robot_moving(field, robot, player)

            if field_iy == -1 and field_jx == -1:
                print("AAAAAAA: Make a move, please")

            # check, is data getting
            from_robot = get_data(client)
            print(from_robot)

            field_X = center_field_X + CELL * (field_iy - 1)
            field_Y = center_field_Y + CELL * (field_jx - 1)

            print("robot ready get a move, type anything")
            _ = input()

            print('data for send to robot - x', field_X)
            field_X_str = str(field_X)
            send_data(client, field_X_str)

            print("robot ready get a move, type anything AGAIN, please")
            _ = input()

            print('data for send to robot - y', field_Y)
            field_Y_str = str(field_Y)
            send_data(client, field_Y_str)

            # check, is data getting
            from_robot = get_data(client)
            print(from_robot)

            print("Robot made a move")
            field_user = field_for_user(field)
            print_m(field_user)

            if status == ROBOT_WIN:
                print(ROBOT_WIN)
                print_field(field)
                break
            if status == PLAYER_WIN:
                print(PLAYER_WIN)
                print_field(field)
                break
            if status == DEED_HEAR:
                print(DEED_HEAR)
                print_field(field)
                break

            robot_step, player_step = False, True

        else:
            is_ans = False
            while not is_ans:
                print('Did you make a move? (y/n)')
                ans = input()
                if ans == YES:
                    is_ans = True
                    print('Well! Let\'s continue')
                elif ans == N0:
                    print('Please, make a move')

            img = get_img(cap)

            detect_field = find_play_field(img)
            # print("detecting field")
            # print_m(detect_field)

            field = matcing_filds(field, detect_field)
            # print("MAIN: matching field")
            # print_m(field)

            robot_step, player_step = True, False

        # cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
