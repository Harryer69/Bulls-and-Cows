""" This script is Bulls and Cows game. Player must to guess right code number.
Code has four numbers. If the player guess right number on right position computer say Bull.
If the player guess write number on wrong position, computer say Cow. Enjoy your game """

import random

from typing import Callable

import time




# Variable for secret code
comp_code = random.sample(range(1,10), k=4)
underline = "_" * 30

def player_code_check(code: str) -> bool:

    """ This function check player code. """

    check_code = True
    
    if not code.isdecimal():
        print("Code must not contain alphabet characters.")
        check_code = False
    if len(code) != 4:
        print("Code must have 4 digits.")
        check_code = False
    if len(code) != len(set(code)):
        print("Code must contain unique digits.")
        check_code = False
    if "0" in code:
        check_code = False
        print("Code must not contain 0.")
    

    return check_code


def cows(player: list[int], comp: list[int])-> int:

    """ This function search right number in player code"""
    
    count = 0
    
    for number in player:
        if number in comp:
            count += 1
    
    return count

def bulls(player: list[int], comp: list[int]) -> int:

    """ This function search right number on right place in player code"""
    
    count = 0

       
    for number in range(len(player)):      
        
        if player[number] == comp[number]:
            count += 1

    return count

def bulls_cows() -> None:

    """ This function is main function for Bulls and Cows game. Function compare counts Bulls and Cows. If Bulls cout equal 4. Function print Win.
        If not Bulls equal 4, function print count Bulls and Cows. Function can measure time. """
    
    while True:
        
        player = input("Enter number: ")
        player_check = player_code_check(player)
               
        
        if player_check:

            split_code = [int(number) for number in player]            
            cows_count = cows(split_code, comp_code)
            bulls_count = bulls(split_code, comp_code)

            if bulls_count == 4:
                print()
                print("You won. Congratulation!!!!")
                return
            else:
                cows_only = cows_count - bulls_count
                print(f"Bulls  {bulls_count}  Cows   {cows_only}")

def game_data(game_time: str, name: str) -> None:

    """ This function writes game data (player name and game time) to the file game_times.txt and sort this game data acc. game time.
     Finally print sorted game data """

    with open("game_times.txt", mode="a", encoding="utf-8") as game_data:

        game_data.write(f"{game_time} sec:{name}\n")

    
    with open("game_times.txt", mode="r", encoding="utf-8") as read_data:

        data = read_data.read()

        data_list = []

        for str_data in data.splitlines():
            split_str_data = str_data.split(":")
            data_list.append(split_str_data)

        data_list.sort(key=lambda x: x[0])

        for dat in data_list:
            join_data = " : ".join(dat)

            print(f"|{join_data:^40}|")
            




if __name__ == "__main__":

     
    players_name = input("Enter your name: ")

    start_time = time.time()
    
    bulls_cows()

    stop_time = time.time()

    game_time = str(round(stop_time - start_time, 2))

    print()

    print(f"Your game time is {game_time} sec")
    
    print()

    print(f"{'Players':^42}")

    game_data(game_time, players_name)

    

    

    

    

    


    
    
   







        

















