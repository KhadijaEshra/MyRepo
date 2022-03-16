# Game 0 SOS Game
# By Khadija Eshra
# The function to print the board in rows and columns by using for loop:
def print_board(__board__):
    for row in __board__:
        for column in row:
            print(column, end=" ")
        print()
    print()


# The function takes the user location between 1-->5 and make sure the input is int:
def user_location_input(location):
    value = ''
    not_correct_input = True

    while not_correct_input:
        try:
            value = int(input("Enter your target location " + location + " (1 --> " + str(len(board)) + "): ")) - 1
            if 0 <= value <= len(board) - 1:
                not_correct_input = False
            else:
                print(location + " must be integer between 1 and " + str(len(board)) + "")
        except ValueError:
            print("location value is not an int!")

    return value


# The function to take the letter from the user and check if it 'o' or's' and return the letter:
def user_location_char():
    input_char = ''
    not_correct_input = True

    while not_correct_input:
        input_char = input("Please select S | O: ")
        if input_char.upper() == 'S' or input_char.upper() == 'O':
            not_correct_input = False
        else:
            print("Input char must be S | O")

    return input_char.upper()


# The function to check the direction of the letter if it O checked what before and after(up\down|right\left|cross)
# Horizontal\vertical\cross and if it = 'SOS' it increases the score for each 'SOS':
def get_direction_of_o(__board__, location_x, location_y):
    score = 0
    if location_x - 1 >= 0 and location_x + 1 <= len(board) - 1:
        if location_y - 1 < 0 or location_y + 1 > len(board) - 1:
            if __board__[location_x - 1][location_y] == 'S' and __board__[location_x + 1][location_y] == 'S':
                score += 1
        else:
            if __board__[location_x - 1][location_y - 1] == 'S' and __board__[location_x + 1][location_y + 1] == 'S':
                score += 1
            if __board__[location_x][location_y - 1] == 'S' and __board__[location_x][location_y + 1] == 'S':
                score += 1
            if __board__[location_x - 1][location_y] == 'S' and __board__[location_x + 1][location_y] == 'S':
                score += 1
            if __board__[location_x - 1][location_y + 1] == 'S' and __board__[location_x + 1][location_y - 1] == 'S':
                score += 1
    else:
        if location_y - 1 >= 0 and location_y + 1 <= len(board) - 1:
            if location_x - 1 < 0 or location_x + 1 > len(board) - 1:
                if __board__[location_x][location_y - 1] == 'S' and __board__[location_x][location_y + 1] == 'S':
                    score += 1

    return score


# The function to check the direction of the letter if it was S and if it = 'SOS' with the letter before and
# Tow location before if it then increased the score for each 'SOS':
def get_direction_of_s(__board__, location_x, location_y):
    score = 0
    if location_x + 2 <= len(board) - 1:
        if __board__[location_x + 1][location_y] == 'O' and __board__[location_x + 2][location_y] == 'S':
            score += 1
    if location_x - 2 >= 0:
        if __board__[location_x - 1][location_y] == 'O' and __board__[location_x - 2][location_y] == 'S':
            score += 1
    if location_y + 2 <= len(board) - 1:
        if __board__[location_x][location_y + 1] == 'O' and __board__[location_x][location_y + 2] == 'S':
            score += 1
    if location_y - 2 >= 0:
        if __board__[location_x][location_y - 1] == 'O' and __board__[location_x][location_y - 2] == 'S':
            score += 1
    if location_x + 2 <= len(board) - 1 and location_y + 2 <= len(board) - 1:
        if __board__[location_x + 1][location_y + 1] == 'O' and __board__[location_x + 2][location_y + 2] == 'S':
            score += 1
    if location_x + 2 <= len(board) - 1 and location_y - 2 >= 0:
        if __board__[location_x + 1][location_y - 1] == 'O' and __board__[location_x + 2][location_y - 2] == 'S':
            score += 1
    if location_x - 2 >= 0 and location_y - 2 >= 0:
        if __board__[location_x - 1][location_y - 1] == 'O' and __board__[location_x - 2][location_y - 2] == 'S':
            score += 1
    if location_x - 2 >= 0 and location_y + 2 <= len(board) - 1:
        if __board__[location_x - 1][location_y + 1] == 'O' and __board__[location_x - 2][location_y + 2] == 'S':
            score += 1

    return score


# The function to update tha board after each time the user entered any char:
def update_board(__board__, player_index):
    location_x = user_location_input("X")
    location_y = user_location_input("Y")
    user_char = user_location_char()

    if __board__[location_x][location_y] == '_':
        __board__[location_x][location_y] = user_char
        round_score = 0

        if user_char == 'O':
            round_score += get_direction_of_o(__board__, location_x, location_y)
        else:
            round_score += get_direction_of_s(__board__, location_x, location_y)

        if round_score == 0:
            return True
        else:
            players[player_index] += round_score
            return False
    else:
        print("Location must be empty in the board")
        return False


# The function to print the score on the screen after each round:
def print_score(__players__):
    print("-------------Current Score------------------")
    print("Player 1: " + str(__players__[0]))
    print("Player 2: " + str(__players__[1]))


# Main def, it has the board and each player score, and the option if the players want to continue the game or want not
# And print the final score.
board = [["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"]]
players = [0, 0]
print_board(board)
current_player_index = 0
round_count = len(board) * len(board)
exit_game = ''

while exit_game != 'x' and exit_game != 'X':
    print("Player " + str(current_player_index + 1) + " round.")
    round_count -= 1
    switch_player = update_board(board, current_player_index)

    if switch_player:
        if current_player_index == 0:
            current_player_index = 1
        else:
            current_player_index = 0

    print_board(board)
    print_score(players)
    if round_count == 0:
        print("-------------FINAL SCORE------------------")
        print_score(players)
        exit_game = 'X'
    else:
        exit_game = input("To continue, press any key. To exit press x: ")
