import os
import json
import random
import shutil
from colorama import init, Fore, Back, Style

# _______f(x)____
def clean():
    '''console cleaner'''
    os.system('cls' if os.name == 'nt' else 'clear')
 

def list_files():
    '''makes a dict of avalible json files for study'''
    files =[]
    for file in os.listdir("./json"):
        files.append(file)
    files_dict = {}
    for i, file in enumerate(files):
        files_dict[i+1] = file
    return(files_dict)


def initialize(filez):
    '''collects initial input from a user to determine which file to open'''
    val = ""
    print(center_str.format(center = Fore.GREEN + "Please select a file " + Fore.YELLOW + "number" + Fore.GREEN + " from the following options:\n"))
    print(center_str.format( center = Style.RESET_ALL + Fore.YELLOW + str(files).replace("{","").replace("}","") +"\n" + Style.RESET_ALL,))
    val = input(center_str.format(center = ""))
    
    while not val.isdigit() or int(val) > len(filez):
        clean()
        print( (Fore.RED + "INVALID ENTRY!! " + Fore.GREEN + "Try again:\n").center(screen_size))
        print( Style.RESET_ALL + Fore.YELLOW + str(filez).replace("{","").replace("}","").center(screen_size))
        val = input().center(screen_size)
   
    return val


def main_loop():
    '''renders screens, sets logic'''
    prev_answer = Fore.RED + Style.BRIGHT + "none"
    while len(working_dict) > 0:
        clean()
        question = random.choice(list(working_dict.keys()))
        prev_answ_update = working_dict[question]
        print(f"The right answer for the previous question is: {prev_answer}")
        answer = input(Fore.BLUE + Style.BRIGHT + ask + question + Fore.WHITE + Style.NORMAL +"\n").lower()
        prev_answer = Fore.RED + Style.BRIGHT + prev_answ_update
        if answer == working_dict[question]:
            del working_dict[question]
            prev_answer = Fore.GREEN + Style.BRIGHT + prev_answ_update
    print(Fore.GREEN + "YOU MADE IT!")


def whats_the_question():
    '''extracts the question var from the dictionary and makes it separate variable'''
    ask = working_dict["question"]
    del working_dict['question']


# ___var___
files = list_files()
ask=""
working_dict = {} 
key_nums = {}
score = 0
screen_size = shutil.get_terminal_size().columns
#___flow___
clean()

# populates dictionary using selected file
with open(f'./json/{files[int(initialize(files))]}', 'r') as f:
    raw_data = f.read()
    working_dict = json.loads(raw_data)

whats_the_question()

main_loop()
        
        
