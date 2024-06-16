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
    selection_str = Fore.GREEN + "Please select a file " + Fore.YELLOW + "number" + Fore.GREEN + " from the following options: "
    files_str = Style.RESET_ALL + Fore.YELLOW + str(files).replace("{","").replace("}","") + Style.RESET_ALL
    print(selection_str.center(screen_size))
    print(files_str.center(screen_size))
    val = input((screen_size//2 - 10) * " ")
    
    while not val.isdigit() or int(val) > len(filez):
        clean()
        invalid_str = Fore.RED + "INVALID ENTRY!! " + Fore.GREEN + "Try again:"
        print( invalid_str.center(screen_size))
        print( (Style.RESET_ALL + Fore.YELLOW + str(filez).replace("{","").replace("}","")).center(screen_size))
        val = input((screen_size//2 - 10) * " ")
   
    return val


def main_loop():
    '''renders screens, sets logic'''
    prev_answer = Fore.RED + Style.BRIGHT + "none"
    while len(working_dict) > 0:
        clean()
        question = random.choice(list(working_dict.keys()))
        prev_answ_update = working_dict[question]

        # rht_answ = "The right answer for the previous question is: " + prev_answer
        rht_answ = "The right answer for the previous question is: " + prev_answer
        qw_remains = Style.RESET_ALL + "There are " + Fore.YELLOW + str(len(working_dict))+ Style.RESET_ALL + " questions left"
        
        stat_bar = stat_str.format(left = rht_answ, right = qw_remains).center(screen_size)
        underline = stat_str.format(left ="_" * 80, right ="_" * 80)
        qw_str = Fore.BLUE + Style.BRIGHT + ask + Fore.GREEN + question + Fore.WHITE + Style.NORMAL 

        print(stat_bar)
        print(underline.center(screen_size) +"\n")
        answer = input(qw_str.center(screen_size) + "\n" + (screen_size//2 - 10) * " ").lower()
        prev_answer = Fore.RED + Style.BRIGHT + prev_answ_update
        if answer == working_dict[question]:
            del working_dict[question]
            prev_answer = Fore.GREEN + Style.BRIGHT + prev_answ_update
    end_str = Fore.GREEN + "YOU MADE IT!"
    print(end_str.center(screen_size))


def whats_the_question():
    '''extracts the question var from the dictionary and makes it separate variable'''
    global ask
    ask = working_dict["question"]
    del working_dict['question']


# ___var___
files = list_files()
ask=""
working_dict = {} 
key_nums = {}
score = 0
screen_size = shutil.get_terminal_size().columns
input_str ="{center:^20}"
stat_str ="{left:<80}{right:>80}"
#___flow___
clean()

# populates dictionary using selected file
with open(f'./json/{files[int(initialize(files))]}', 'r') as f:
    raw_data = f.read()
    working_dict = json.loads(raw_data)

whats_the_question()

main_loop()
        
        
