import pandas as pd
from colorama import Fore,Style
import sys

currentLevel=0
digitCount=4
dataFileName="99-4Digit.csv"

def readPassword(currentLevel):
    df=pd.read_csv(f"Data/{dataFileName}")
    return df['password'][currentLevel]

def createSpace(lineCount):
    for i in range(0,lineCount):
        print('\n')


def getInput():
    while 1:
        inp = input("")
        if not (len(inp) == digitCount):
            print(f"{Fore.LIGHTBLACK_EX}WARNING You didn't write {digitCount} digit number {Style.RESET_ALL}")
        else:
            break
    return inp

def checkInput(inp,currentPassword,i):
    if currentPassword[i]==inp[i]:
        return Fore.GREEN
    elif inp[i] in currentPassword:
        return Fore.YELLOW
    elif inp[i] not in currentPassword:
        return Fore.RED



for levelID in range(0,99):
    currentLevel=levelID
    currentPassword=str(readPassword(currentLevel))
    print(f"Your current level is {Fore.RED}{currentLevel+1} {Style.RESET_ALL}")
    for row in range(1,7):


        inp=getInput()

        print(f"{row}st Row: {checkInput(inp,currentPassword,0)}{inp[0]}{Style.RESET_ALL}{checkInput(inp,currentPassword,1)}{inp[1]}{Style.RESET_ALL}{checkInput(inp,currentPassword,2)}{inp[2]}{Style.RESET_ALL}{checkInput(inp,currentPassword,3)}{inp[3]}{Style.RESET_ALL}")
        if (inp==currentPassword):
            print("Congrats You WON!")
            print("*****************")
            break

