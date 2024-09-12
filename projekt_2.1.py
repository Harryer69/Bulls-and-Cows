"""projekt_2.1.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Rossmanith
email: rossmanith.tomas@email.cz
discord: tomasrossmanith
"""


import random
import time

start_time = time.time()

def gen_secret_number():
    
    """Funkce pro generování náhodného čtyřmístného kódu"""

    number = list(range(0,10))
    random.shuffle(number)
    return number[:4]

def bulls_cows (secret, guess):
    
    """ Funkce pro vyhodnocení správných čísel na správném místě (bulls) a správných čísel na nesprávném místě (cows).
        Proměnná bulls pomocí for cyklu zjistí počet uhodnutých čísel na správné pozici
        Proměnná cows zjistí počet správně uhodnutých čísel na nesprávné pozici"""
    
    bulls = sum(sec == gue for sec, gue in zip(secret, guess))
    cows = sum(gue in secret for gue in guess) - bulls

    return bulls, cows

def main():

    """Tato funkce slouží jako hlavní funkce pro hru Bulls and Cows. Funkce nejprve vyžádá 4 místný číselný kód od uživatele.
       Následně zkontroluje, jestli zadaný kód odpovídá požadavkům a poté porovná zadaný kód od uživatele s náhodně vygenerovaným kódem.
       Konec této funkce vypíše počet Bulls a počet Cows. Je-li kód uhádnut, funkce vypíše text s gratulací a ukončí se. Funkce také vypíše
       počet pokusů a čas potřebný k dosažení správného kódu."""
    
    secret_number = gen_secret_number()
    attempts = 0
    underline = "-" * 47

    print("Hi there!")
    print(underline)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(underline)

    while True:
        guess = input("Enter 4 number: ")
        
        if len(guess) != 4:
            print("Invalid entry. Code must have 4 numbers")
            print(underline)
            continue
        elif guess[0] == "0":
            print("Invalid entry. 0 can not be on start")
            print(underline)
            continue
        elif len(guess) != len(set(guess)):
            print("Invalid entry. Code must contain unique numbers")
            print(underline)
            continue
        elif not guess.isdigit():
            print("Invalid entry. Code must contain only numbers")
            print(underline)
            continue

    
        guess = [int(digit) for digit in guess]
        attempts += 1
        

        bulls, cows = bulls_cows(secret_number, guess)
        print("Bulls:", bulls, "Cows:", cows)
        print(underline)

        if bulls == 4:
            print("Correct, you have guessed the right number")
            print(underline)
            end_time = (time.time())
            elapsed_time = round(end_time - start_time, 2)
            print("Your time is:", elapsed_time, "sec")
            print("Number of attempts: ", attempts)
            break
       

if __name__ == "__main__":
    main()



    
    

    









        


    
        
      
        





