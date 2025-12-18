#Bulls & Cows
#functions and support values:
Separator = "-" * 47
Text_game_start = f"""{Separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game."""
Text_user_choise = f"""{Separator}
That's amazing!
{Separator}
You've just guess correctly,
if want to play again type in 'continue',
or if you want exit type in 'exit'.
{Separator}"""

def number_generation(number_lenght : int = 4) -> str: 
    """
    Docstring for number_generation
    This funcion geterates special game number.
    The baseline rules:
    1) the first digit can not be 0
    2) no digict can be the same"""
    
    import random
    
    game_number = random.randint(1,9) #first digit -> != 0
    avalable_numbers = list(range(10))
    avalable_numbers.remove(game_number)
    game_number = str(game_number)

    for i in range(1,number_lenght):
        number = random.choice(avalable_numbers)
        avalable_numbers.remove(number)
        game_number += str(number)

    return(game_number)

def user_number_input(game_number : str):
    f"""
    Docstring for user_number_input
    Asks user for number for one try in game.
    The function does not accept input that go against number generation rules:
    {number_generation.__doc__}\n 
    It returns the user input as str or 
    nothing if the input does not match the rules - 
    it this case it prints error mesage."""

    #chyba - nepozna to ze v pokusu je vice stejnych cisel a pom 
    #to prida vice cows etc.
    print(Separator)
    user_guess = input(">>> ")
    if user_guess.isdigit() and len(user_guess) == len(game_number) and user_guess[0] != 0:
        return(user_guess) 
    else:
        print("Your input does not work, try again.")
        return(False)
    
def plural(number : int) -> str:
    """
    Docstring for plural
    It returns '' if the form need to be singular.
    It returns 's' if the form need to be plural."""
    if number == 1:
        return('')
    else:
        return('s')
    
def number_verification(game_number : str, user_guess : str, attemps_number : int) -> bool:
    """
    Docstring for number_verification
    The function compares user's guess with the target number. 
    It prints the bulls and cows for user.
    If user guested correctly it prints message and number of attemps it took to find it.
    It returns True or False."""

    if game_number == user_guess:
        print("Correct, you've guessed the right number,")
        if (plural_form := plural(attemps_number)):
            plural_form = "e" + plural_form
        print(f"in {attemps_number} guess{plural_form}!")
        return(True)
    
    #nevim jestli chyba ale divne to pocita
    bulls = 0
    cows = 0
    for digit in user_guess:
        if digit in game_number:
            if user_guess.index(digit) == game_number.index(digit):
                bulls += 1
        else:
            cows += 1

    print(f"{bulls} bull{plural(bulls)}, {cows} cow{plural(cows)}")

#the game
print("Hi there!")
print(Text_game_start)
attemps_number = 0
game_number = number_generation()
print(game_number)
#the game while loop
running = True
while running: 

    #the while loop for guessing one number
    print(Separator)
    print("Enter a number:")  
    while True:
        attemps_number += 1
        if not (user_guess := user_number_input(game_number)):
            continue
        if not number_verification(game_number, user_guess, attemps_number):
            continue
        break

    print(Text_user_choise)
    while (command := input(">>> ")) !=  "continue" or "exit":
        print(Separator)
        if command == "continue":
            break
        elif command == "exit":
            running = False 
            break
        
exit("terminating the program...")
#end of the game