import random
import sys


LOWER_NUMBER = 1
HIGHEST_NUMBER = 10


def print_header():
    print("-" * 40)
    print("Welcome to the number guessing game")
    print("-" * 40)


def print_exit_message():
    print("\n Thanks for playing, see you next time!")


def check_exit(leave_game):
    if leave_game.lower() == 'y':
        print_exit_message()
        sys.exit(1)


def user_input():
    """Collect and validate the entries made by the users

    Returns
    -------
    int
        Gives back the validated number entered by the user.
    """
    while True:
        try:
            guess = int(
                input(f'Enter your Guess of a number between '
                      f'{LOWER_NUMBER} - {HIGHEST_NUMBER}: '))
        except ValueError:
            print('you did not enter a number, please try again.')
            continue
        else:
            break

        if guess < LOWER_NUMBER or guess > HIGHEST_NUMBER:
            print("The entered number is out of range, try again.")
            continue

    return guess


def generate_number_to_guess(lower_number, higher_number):
    """Generates a random number between the given lowest and highest number

    Parameters
    ----------
    lower_number : int
        Lowest number for the generator

    higher_number : int
        highest number for the generator

    Returns
    -------
    int
        returns the generated random number that is in the given range.
    """
    return random.randint(lower_number, higher_number)


def play_again():
    """Perform and validate entry for a next game

    Returns
    -------
    string
        returns the validated user entry for a next game.
    """
    while True:
        # capture the ctrl-c interupt.
        # https://stackoverflow.com/questions/15318208/capture-control-c-in-python
        try:
            new_game = input(
                "Would you like to play again? [y]es/[n]o: ")
        except KeyboardInterrupt:
            leave_game = input("Do you really want to quit? (y/n) ")
            if not check_exit(leave_game):
                continue

        if new_game.lower() not in ["n", "y"]:
            print('Wrong entry please use y or n')
            continue
        else:
            break

    return new_game.lower()


def start_game():
    """This is the main loop that runs the app.
    """
    highscore = 0
    while True:
        print_header()
        number_to_guess = generate_number_to_guess(LOWER_NUMBER,
                                                   HIGHEST_NUMBER)
        guess = 0
        count = 0

        while guess != number_to_guess:
            # capture the ctrl-c interupt.
            # https://stackoverflow.com/questions/15318208/capture-control-c-in-python
            try:
                guess = user_input()
            except KeyboardInterrupt:
                leave_game = input("Do you really want to quit? (y/n) ")
                if not check_exit(leave_game):
                    continue

            count += 1
            if guess < number_to_guess:
                print("It's higher")
            elif guess > number_to_guess:
                print("It's lower")

        else:
            print(
                f'\nYou geussed the right number and needed {count} tries')
            if count < highscore or highscore == 0:
                highscore = count

            # validate the input for a new game
            another_game = play_again()
            if another_game == 'y':
                print(f"\n\nThe HIGHSCORE is {highscore}")
                continue
            elif another_game == 'n':
                print_exit_message()
                break


if __name__ == "__main__":
    start_game()
