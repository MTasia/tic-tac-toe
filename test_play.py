from src.play import *


def create_visible_field():
    field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return field


def match_field(field, field_visible):
    for i in range(N):
        for j in range(N):
            if field[i][j] == X or field[i][j] == O:
                field_visible[i][j] = field[i][j]
    return field_visible


def main():
    field_visible = create_visible_field()

    is_ans = False
    while not is_ans:
        print('Do you want play first - X? (y/n)')
        ans = input()
        if ans == YES:
            is_ans = True
            print('Well! You are -' + X)
            player = X
            robot = O
        elif ans == N0:
            is_ans = True
            print('Well! You are -' + O)
            player = O
            robot = X

    field = create_field(robot)
    field_visible = match_field(field, field_visible)

    while True:
        is_ans = False
        while not is_ans:
            # print('Before player select')
            print_field(field_visible)
            print("Select cell from 1 to 9, please (you are -", player, ")")
            cell = input()
            try:
                cell = int(cell)
                if 1 <= cell <= 9:
                    i = (cell - 1) // 3
                    j = cell % 3
                    if j == 1:
                        j = 0
                    elif j == 2:
                        j = 1
                    elif j == 0:
                        j = 2

                    if field[i][j] != X and field[i][j] != O:
                        field[i][j] = player
                        field_visible[i][j] = player
                        is_ans = True
                        # print('After player select')
                        # print('Visible')
                        # print_field(field_visible)
                        # print('Working')
                        # print_m(field)
                    else:
                        print('This cell is taken. Select another cell, please.')
            except:
                pass


        field, status = play(field, robot, player)
        field_visible = match_field(field, field_visible)

        if status == ROBOT_WIN:
            print(ROBOT_WIN)
            print_field(field_visible)
            break
        if status == PLAYER_WIN:
            print(PLAYER_WIN)
            print_field(field_visible)
            break
        if status == DEED_HEAR:
            print(DEED_HEAR)
            print_field(field_visible)
            break

    print("THE END!")


if __name__ == '__main__':
    main()
