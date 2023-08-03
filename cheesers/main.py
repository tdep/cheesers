import os
import sys
from time import sleep
from itertools import cycle
from threading import Thread
import title
from resources.Player import Player

cheesers = title.cheesers

done = False

terminal = sys.stdout

def animate():
    # Loading text animation
    for c in cycle([' ','.','_','/','|','\\','_','.',' ']):
        if done:
            break
        terminal.write('\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()


def titleCard():
    # Print the title card
    print()
    print("Welcome to Primitive")
    print('<--------------------')
    for list in cheesers:
        i = 0
        print(list[i])
        i += 1
    print('                                     -------------------->')


def start():
    # Initialize the program
    print()
    input("Press ENTER to start.")
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win32'):
        os.system('cls')
    titleCard()
    
player_1 = Player("", [], [])
player_2 = Player("", [], [])

def playerSelect():
    # Call the color selector for the player objects
    player_1.colorPicker(player_1, player_2)


# GO!
playerSelect()
t = Thread(target=animate)
t.start()
sleep(5)
done = True
start()
