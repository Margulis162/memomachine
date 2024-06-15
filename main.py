import os
import globals
import json
import random
from colorama import init, Fore, Back, Style

# _______f(x)____
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
    val = input(Fore.GREEN + Back.BLACK + "Please select a file " + Fore.YELLOW + "number" + Fore.GREEN + " from the following options:\n" + Style.RESET_ALL + Fore.YELLOW + str(files).replace("{","").replace("}","") +"\n" + Style.RESET_ALL)
   
    while not val.isdigit() or int(val) > len(filez):
        globals.clean()
        val = input(Fore.RED + Back.BLACK + "INVALID ENTRY!! " + Fore.GREEN + "Try again:\n" + Style.RESET_ALL + Fore.YELLOW + str(filez).replace("{","").replace("}","") +"\n" + Fore.LIGHTWHITE_EX)
   
    return val

def main_loop():
    prev_answer = ""
    while len(working_dict) > 0:
        globals.clean()
        question = random.choice(list(working_dict.keys()))
        prev_answ_update = working_dict[question]
        print(f"The right answer for the previous question is: {prev_answer}")
        answer = input(Back.BLACK + Fore.BLUE + Style.BRIGHT + f"What does {question} stands for?\n" + Fore.YELLOW + Style.NORMAL)
        prev_answer = prev_answ_update
        if answer == working_dict[question]:
            del working_dict[question]
  
    print(Fore.GREEN + "YOU MADE IT!")

# ___var___
files = list_files()
working_dict = {} 
key_nums = {}
score = 0
# flow
globals.clean()

# populates dictionary using selected file
with open(f'./json/{files[int(initialize(files))]}', 'r') as f:
    raw_data = f.read()
    working_dict = json.loads(raw_data)

main_loop()
        
        
