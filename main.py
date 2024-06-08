import os
from colorama import init, Fore, Back, Style

# _______f(x)____________________________________________________________________________________________________________________
def list_files():
    '''makes a list of avalible json files for study'''
    files =[]
    for file in os.listdir("./json"):
        files.append(file)
    files_dict = {}
    for i, file in enumerate(files):
        files_dict[i+1] = file
    return(files_dict)

def check_input(input):
    try:
        val = int(input)
        print('wut')
    except:
        print("Invalid input, try again")
        check_input(initialize())

def initialize():
    val = input(Fore.GREEN + Back.BLACK + "Please select a file number from the following options:\n" + Style.RESET_ALL + str(files).replace("{","").replace("}","") +"\n")
    return val
files = list_files()

# lets user to pick a file to study

check_input(initialize())
