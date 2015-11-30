import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)


####################################
######GAME IS NOT WORKING (YET)#####
####################################
def Main():

#A board represents a reference to your city
  board = build_square_matrix(10, 30)
  start = time.time()
  position = 1
  car = Node(position, car)
  while True:    

    screen.fill(green)  
    board.Reset()
    board.Draw(screen)

    #MAIN_LOOP
#TODO: your code below (mind data structures go outside this function)

#   ....

    pygame.display.flip()
    time.sleep(1.0)
    
Main()