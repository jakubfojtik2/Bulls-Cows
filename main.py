#Bulls & Cows
#functions and support values:
Separator = "-" * 47
Text_game_start = f"""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{Separator}
Enter a number:"""
Text_user_choise = f"""{Separator}
If want to play again type in "again"
or if you want exit type in "exit".
{Separator}"""

def number_generation(number_lenght : int = 4) -> str: 
    """
    Docstring for number_generation
    This funcion geterates special game number.
    The baseline rules:
    1) the first digit can not be 0
    2) no digict can be the same
    (the baseline lenght of the number is 4 digits)"""
    
    import random
    
    #generation of first digit
    game_number = random.randint(1,9) #first digit -> != 0
    avalable_numbers = list(range(10))
    avalable_numbers.remove(game_number)
    game_number = str(game_number)

    #genneration of other digits
    for i in range(1,number_lenght):
        number = random.choice(avalable_numbers)
        avalable_numbers.remove(number)
        game_number += str(number)
    return(game_number)

def user_number_input(game_number : str):
    f"""
    Docstring for user_number_input
    It asks user for number.
    The function does not accept input that 
    go against number generation rules:
    {number_generation.__doc__}\n 
    It returns the user input as str or 
    False if the input does not match the rules
    and in this case it prints error mesage."""

    print(Separator)
    user_guess = input(">>> ")
    if user_guess == "help": #only for testing
        print(game_number)
    #check if there are only digits
    if not user_guess.isdigit():
        print("Your guess need to be from numbers, try again.")
    else:
        #check if the length is OK
        if not len(user_guess) == len(game_number):
            print(f"Lenght of your guess need to be {len(game_number)} digits, try again.")
        else:
            #check if it starts with 0
            if user_guess[0] == 0:
                print(f"Your guess mustn't start with 0, try again.")
            else:
                #check if there are same digits
                if len(set(user_guess)) < len(user_guess):
                    print("Your guess mustn't contain same digits, try again.")
                else:
                    return(user_guess) 
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
    If user guested correctly, it prints message
    and number of attemps it took to find it.
    It returns True or False."""

    #if the guess is correct
    if game_number == user_guess:
        print("Correct, you've guessed the right number,")
        if (plural_form := plural(attemps_number)):
            plural_form = "e" + plural_form
        print(f"in {attemps_number} guess{plural_form}!")
        return(True)
    
    #the message if the guess is not correct 
    bulls = 0
    cows = 0
    for digit in user_guess:
        if digit in game_number:
            if user_guess.index(digit) == game_number.index(digit):
                bulls += 1
                #print(f"for {digit} +1 bull") #only for testing
            else:
                cows += 1
                #print(f"for {digit} +1 cow") #only for testing
        else:
            #print(f"for {digit} nothing") #only for testing
            pass
    
    print(f"{bulls} bull{plural(bulls)}, {cows} cow{plural(cows)}")

#the game
print("Hi there!")
print(Separator)
attemps_number = 0
running = True

#the game while loop
while running:

    game_number = number_generation()
    #print(game_number) #only for testing  
    print(Text_game_start)

    #the while loop for guessing one number
    while True:
        attemps_number += 1
        if not (user_guess := user_number_input(game_number)):
            continue
        if not number_verification(game_number, user_guess, attemps_number):
            continue
        break

    #question after succecful guess -> play again or exit
    print(Text_user_choise)
    while (command := input(">>> ")) !=  "again" or "exit":
        print(Separator)
        if command == "again":
            break
        elif command == "exit":
            running = False 
            break

exit("terminating the program...")