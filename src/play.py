from utils.helps import *


def create_field(robot):
    field = [
        [20, 10, 20],
        [10, 30, 10],
        [20, 10, 20]
    ]

    return field


def check_win(field):
    if field[0][0] == field[0][1] and field[0][1] == field[0][2]:
        return True, field[0][0]
    elif field[1][0] == field[1][1] and field[1][1] == field[1][2]:
        return True, field[1][0]
    elif field[2][0] == field[2][1] and field[2][1] == field[2][2]:
        return True, field[2][0]

    elif field[0][0] == field[1][0] and field[1][0] == field[2][0]:
        return True, field[0][0]
    elif field[0][1] == field[1][1] and field[1][1] == field[2][1]:
        return True, field[0][1]
    elif field[0][2] == field[1][2] and field[1][2] == field[2][2]:
        return True, field[0][0]

    elif field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        return True, field[0][0]
    elif field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        return True, field[0][2]

    return False, 0


def check_dead_heat(field):
    is_dead_heat = True
    for i in range(N):
        for j in range(N):
            if cell_is_free(field[i][j]):
                is_dead_heat = False
                return is_dead_heat
    return is_dead_heat


def change_weight_after_payer(field, robot, player):
    # 0 0
    if cell_is_free(field[0][0]):
        if (field[0][1] == player and field[0][2] == player) or \
                (field[1][0] == player and field[2][0] == player) or \
                (field[1][1] == player and field[2][2] == player):
            field[0][0] = 200

    # 0 1
    if cell_is_free(field[0][1]):
        if (field[0][0] == player and field[0][2] == player) or \
                (field[1][1] == player and field[2][1] == player):
            field[0][1] = 200

    # 0 2
    if cell_is_free(field[0][2]):
        if (field[0][0] == player and field[0][1] == player) or \
                (field[1][2] == player and field[2][2] == player) or \
                (field[1][1] == player and field[2][0] == player):
            field[0][2] = 200

    # 1 0
    if cell_is_free(field[1][0]):
        if (field[0][0] == player and field[2][0] == player) or \
                (field[1][1] == player and field[1][2] == player):
            field[1][0] = 200

    # 1 1
    if cell_is_free(field[1][1]):
        if (field[0][0] == player and field[2][2] == player) or \
                (field[0][2] == player and field[2][0] == player) or \
                (field[1][0] == player and field[1][2] == player) or \
                (field[0][1] == player and field[2][1] == player):
            field[1][1] = 200

    # 1 2
    if cell_is_free(field[1][2]):
        if (field[0][2] == player and field[2][2] == player) or \
                (field[1][0] == player and field[1][1] == player):
            field[1][2] = 200

    # 2 0
    if cell_is_free(field[2][0]):
        if (field[0][0] == player and field[1][0] == player) or \
                (field[2][1] == player and field[2][2] == player) or \
                (field[0][2] == player and field[1][1] == player):
            field[2][0] = 200

    # 2 1
    if cell_is_free(field[2][1]):
        if (field[0][1] == player and field[1][1] == player) or \
                (field[2][0] == player and field[2][2] == player):
            field[2][1] = 200

    # 2 2
    if cell_is_free(field[2][2]):
        if (field[0][0] == player and field[1][1] == player) or \
                (field[0][2] == player and field[1][2] == player) or \
                (field[2][0] == player and field[2][1] == player):
            field[2][2] = 200

    return field


def change_weight_after_robot(field, max_i, max_j):
    for i in range(N):
        if field[i][max_j] != X and field[i][max_j] != O:
            if i == 0 or i == 2:
                field[i][max_j] = 100
            elif i == 1:
                field[i][max_j] = 50
    for j in range(N):
        if field[max_i][j] != X and field[max_i][j] != O:
            if j == 0 or j == 2:
                field[max_i][j] = 100
            elif j == 1:
                field[max_i][j] = 50
    return field


def make_move(field, robot, player):
    field = change_weight_after_payer(field, robot, player)
    # print('After change weight for player')
    # print_m(field)

    max_weight = -1
    for i in range(N):
        for j in range(N):
            if cell_is_free(field[i][j]):
                max_weight = field[i][j]
                max_i, max_j = i, j

    if max_weight == -1:
        return field, DEED_HEAR

    for i in range(N):
        for j in range(N):
            if cell_is_free(field[i][j]):
                if field[i][j] > max_weight:
                    max_weight = field[i][j]
                    max_i, max_j = i, j

    field[max_i][max_j] = robot

    # print('After robot select')
    # print_m(field)

    return field


def play(field, robot, player):
    is_win, winner = check_win(field)
    if is_win:
        if robot == winner:
            return field, ROBOT_WIN
        else:
            return field, PLAYER_WIN

    is_dead_heat = check_dead_heat(field)
    if is_dead_heat:
        return field, DEED_HEAR

    new_field = make_move(field, robot, player)

    is_win, winner = check_win(new_field)
    if is_win:
        if robot == winner:
            return new_field, ROBOT_WIN
        else:
            return new_field, PLAYER_WIN

    is_dead_heat = check_dead_heat(new_field)
    if is_dead_heat:
        return new_field, DEED_HEAR

    return new_field, 0
