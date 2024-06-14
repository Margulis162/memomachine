import os
import globals
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
    val = input(Fore.GREEN + Back.BLACK + "Please select a file " + Fore.YELLOW + "number" + Fore.GREEN + " from the following options:\n" + Style.RESET_ALL + Fore.YELLOW + str(files).replace("{","").replace("}","") +"\n")
   
    while not val.isdigit() or int(val) > len(filez):
        globals.clean()
        val = input(Fore.RED + Back.BLACK + "INVALID ENTRY!! " + Fore.GREEN + "Try again:\n" + Style.RESET_ALL + Fore.YELLOW + str(filez).replace("{","").replace("}","") +"\n")
   
    return val

# flow

files = list_files()
globals.clean()
initialize(files)