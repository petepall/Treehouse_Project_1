import random


LOWER_NUMBER = 1
HIGHEST_NUMBER = 10


def print_header():
    print("-" * 40)
    print("Welcome to the number guessing game")
    print("-" * 40)


def UserInput():
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


def GenerateGuessNumber(lower_number, higher_number):
    return random.randint(lower_number, higher_number)


def start_game():
    highscore = 0

    while True:
        print_header()
        numberToGuess = GenerateGuessNumber(LOWER_NUMBER, HIGHEST_NUMBER)
        guess = 0
        count = 0

        while guess != numberToGuess:
            guess = UserInput()
            count += 1
            if guess < numberToGuess:
                print("It's higher")
            elif guess > numberToGuess:
                print("It's lower")
        else:
            print(f'\nYou geussed the right number and needed {count} tries')
            if count < highscore or highscore == 0:
                highscore = count

            play_again = input("Would you like to play again? [y]es/[n]o: ")
            if play_again.lower() == 'y':
                print(f"\n\nThe HIGHSCORE is {highscore}")
                continue
            elif play_again.lower() == 'n':
                print("\n Thanks for playing, see you next time!")
                break
            else:
                print('Wrong entry please use y or n')
                play_again = input(
                    "Would you like to play again? [y]es/[n]o: ")


if __name__ == "__main__":
    start_game()
