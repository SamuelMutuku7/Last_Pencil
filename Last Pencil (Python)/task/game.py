import random


def initialise_pencil_count():
    while True:
        pencil_count = input("How many pencils would you like to use: \n")
        if not pencil_count.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencil_count = int(pencil_count)
        if pencil_count == 0:
            print("The number of pencils should be positive")
            continue
        return pencil_count


def determine_first_turn():
    while True:
        players = ["Jelani", "Jerome"]
        first_turn = input("Who will be the first (Jelani, Jerome): \n")
        if first_turn not in players:
            print("Choose between Jelani and Jerome")
            continue
        second_turn = players[1] if first_turn == players[0] else players[0]
        return first_turn, second_turn


def validate_draw_input(pencil_count):
    legal_draw = [1, 2, 3]
    while True:
        draw = input()
        if not draw.isdigit():
            print("Possible values: '1', '2' or '3'")
            continue
        draw = int(draw)
        if draw not in legal_draw:
            print("Possible values: '1', '2' or '3'")
            continue
        if draw > pencil_count:
            print("Too many pencils were taken")
            continue
        return draw


def bot_turn(pencil_count):
    if pencil_count % 4 == 1:
        return random.randint(1, 3)
    elif pencil_count % 4 == 2:
        return 1
    elif pencil_count % 4 == 3:
        return 2
    elif pencil_count % 4 == 0:
        return 3


def print_pencils(pencil_count):
    print("|" * pencil_count)


def player_turn(player_name, pencil_count):
    print(f"{player_name}'s turn:")
    move = validate_draw_input(pencil_count)
    return pencil_count - move


def bot_turn_logic(player_name, pencil_count):
    print(f"{player_name}'s turn:")
    move = bot_turn(pencil_count)
    print(move)
    return pencil_count - move


def bot_first_turn(pencil_count, first_turn, second_turn):
    print_pencils(pencil_count)
    while pencil_count > 0:
        if pencil_count == 1:
            print(f"{second_turn} won!")
            break
        pencil_count = bot_turn_logic(first_turn, pencil_count)
        print_pencils(pencil_count)
        pencil_count = player_turn(second_turn, pencil_count)
        if pencil_count == 0:
            print(f"{first_turn} won!")
            break
        print_pencils(pencil_count)


def bot_second_turn(pencil_count, first_turn, second_turn):
    print_pencils(pencil_count)
    while pencil_count > 0:
        pencil_count = player_turn(first_turn, pencil_count)
        if pencil_count == 0:
            print(f"{second_turn} won!")
            break

        print_pencils(pencil_count)
        print(f"{second_turn}'s turn:")

        if pencil_count == 1:
            print(1)
            print_pencils(0)
            print(f"{first_turn} won!")
            break
        else:
            bot_move = bot_turn(pencil_count)
            print(bot_move)
            pencil_count -= bot_move

        print_pencils(pencil_count)
        if pencil_count == 0:
            print(f"{first_turn} won!")
            break


def main():
    pencil_count = initialise_pencil_count()
    first_turn, second_turn = determine_first_turn()

    if first_turn == "Jerome":
        bot_first_turn(pencil_count, first_turn, second_turn)
    else:
        bot_second_turn(pencil_count, first_turn, second_turn)


if __name__ == "__main__":
    main()

