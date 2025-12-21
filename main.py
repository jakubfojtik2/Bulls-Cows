# Bulls & Cows
# functions and support values:
SEPARATOR = "-" * 47
TEXT_GAME_START = f"""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{SEPARATOR}
Enter a number:"""
TEXT_USER_CHOICE = f"""{SEPARATOR}
If you want to play again, type in "again"
or if you want to exit, type in "exit".
{SEPARATOR}"""

def number_generation(number_length : int = 4) -> str: 
    """
    Docstring for number_generation
    This function generates special game number.
    The baseline rules:
    1) the first digit can not be 0
    2) no digit can be the same
    (the baseline length of the number are 4 digits)"""
    
    import random
    
    # generation of first digit
    game_number = random.randint(1, 9) # first digit -> != 0
    available_numbers = list(range(10))
    available_numbers.remove(game_number)
    game_number = str(game_number)

    # generation of other digits
    for i in range(1, number_length):
        number = random.choice(available_numbers)
        available_numbers.remove(number)
        game_number += str(number)
    return(game_number)


def user_number_input(game_number : str):
    """
    Docstring for user_number_input
    It asks user for number.
    The function does not accept input that 
    go against number generation rules.
    It returns the user input as str or 
    False in this case it prints error message."""

    print(SEPARATOR)
    user_guess = input(">>> ")
    # check if there are only digits
    if not user_guess.isdigit():
        print("Your guess needs to be only numbers, try again.")
    else:
        # check if the length is OK
        if not len(user_guess) == len(game_number):
            print(f"Lenght of your guess needs to be {len(game_number)} digits, try again.")
        else:
            # check if it starts with 0
            if user_guess[0] == "0":
                print(f"Your guess mustn't start with 0, try again.")
            else:
                # check if there are same digits
                if len(set(user_guess)) < len(user_guess):
                    print("Your guess mustn't contain duplicate digits, try again.")
                else:
                    return(user_guess) 
    return(False)


def plural(number : int) -> str:
    """
    Docstring for plural
    It returns '' if the form needs to be singular.
    It returns 's' if the form needs to be plural."""
    if number == 1:
        return('')
    else:
        return('s')


def number_verification(game_number : str, user_guess : str, attempts_number : int) -> bool:
    """
    Docstring for number_verification
    The function compares user's guess with the target number. 
    It prints the bulls and cows for user.
    If user guessed correctly, it prints message
    and number of attempts it took to find it.
    It returns True or False."""

    # if the guess is correct
    if game_number == user_guess:
        print("Correct, you've guessed the right number,")
        if (plural_form := plural(attempts_number)):
            plural_form = "e" + plural_form
        print(f"in {attempts_number} guess{plural_form}!")
        return(True)
    
    # the message if the guess is not correct 
    bulls = 0
    cows = 0
    for digit in user_guess:
        if digit in game_number:
            if user_guess.index(digit) == game_number.index(digit):
                bulls += 1
            else:
                cows += 1
    
    print(f"{bulls} bull{plural(bulls)}, {cows} cow{plural(cows)}")
    return(False)


# the game
print("Hi there!")
print(SEPARATOR)
running = True
# the game while loop
while running:

    attempts_number = 0
    game_number = number_generation()
    print(TEXT_GAME_START)
    
    # the while loop for guessing one number
    while True:
        attempts_number += 1
        if not (user_guess := user_number_input(game_number)):
            continue
        if not number_verification(game_number, user_guess, attempts_number):
            continue
        break

    # question after successful guess -> play again or exit
    print(TEXT_USER_CHOICE)
    while True:
        command = input(">>> ")
        print(SEPARATOR)
        if command == "again":
            break
        elif command == "exit":
            running = False 
            break
        else:
            print('Please type "again" or "exit".')

exit("terminating the program...")