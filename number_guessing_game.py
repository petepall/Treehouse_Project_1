import random


LOWER_NUMBER = 1
HIGHEST_NUMBER = 10


def print_header():
    print("-" * 40)
    print("Welcome to the number guessing game")
    print("-" * 40)


def User_input():
    """This function manages the user input and validation for the guesses

    Returns:
        int -- return the validated guess entry
    """
    while True:
        try:
            guess = int(
                input(f'Enter your Guess of a number between '
                      f'{LOWER_NUMBER} - {HIGHEST_NUMBER}: '))
            if guess < LOWER_NUMBER or guess > HIGHEST_NUMBER:
                print("The entered number is out of range, try again.")
                continue
        except ValueError:
            print('you did not enter a number, please try again.')
            continue
        else:
            break
    return guess


def Generate_guess_number(lower_number, higher_number):
    """Generated a random integer number and returns this

    Arguments:
        lower_number {int} -- This is the lower number for the random generator
        higher_number {int} -- Thi is the highest number for the random
        generator

    Returns:
        int -- Generated random number within the specified range
    """
    return random.randint(lower_number, higher_number)


def start_game():
    """Main loop of the game
    """
    highscore = 0

    while True:
        print_header()
        number_to_guess = Generate_guess_number(LOWER_NUMBER, HIGHEST_NUMBER)
        guess = 0
        count = 0

        while guess != number_to_guess:
            guess = User_input()
            count += 1
            if guess < number_to_guess:
                print("It's higher")
            elif guess > number_to_guess:
                print("It's lower")
        else:
            print(f'\nYou geussed the right number and needed {count} tries')
            if count < highscore or highscore == 0:
                highscore = count

            # validate the input for a new game
            while True:
                play_again = input(
                    "Would you like to play again? [y]es/[n]o: ")
                if play_again.lower() not in ["n", "y"]:
                    print('Wrong entry please use y or n')
                    continue
                else:
                    break
            if play_again.lower() == 'y':
                print(f"\n\nThe HIGHSCORE is {highscore}")
                continue
            elif play_again.lower() == 'n':
                print("\n Thanks for playing, see you next time!")
                break


if __name__ == "__main__":
    start_game()
