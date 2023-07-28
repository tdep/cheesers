import os
import sys
from time import sleep
from itertools import cycle
from threading import Thread
import title

cheesers = title.cheesers

done = False

terminal = sys.stdout

def animate():
    for c in cycle([' ','.','_','/','|','\\','_','.',' ']):
        if done:
            break
        terminal.write('\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()




def titleCard():
    print()
    print("Welcome to Primitive")
    print('<--------------------')
    for list in cheesers:
        i = 0
        print(list[i])
        i += 1
    print('                                     -------------------->')


def start():
    print()
    input("Press ENTER to start.")
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win32'):
        os.system('cls')
    titleCard()

t = Thread(target=animate)
t.start()
sleep(5)
done = True
start()
