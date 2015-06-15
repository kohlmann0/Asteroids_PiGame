# Michael Kohlmann
# devCodeCamp - Team Helium
# Asteroids Clone
# 6/15/2015

# This is the main game engine loop for our asteroids clone.

# Main Loop consists of Reading User inputs from the Ship class.
# Iterating through each game object for the time increment (ie, movement, shooting, whatever might happen in one game cyle)
# Iterating through each game object for collision detection
# Iterating through each game object and displaying it to the screen.


import datetime
import time
import pygame
import os
#from ship import *              # Ryan
#from asteroidsftw import *      # Rob
#from display import *           # Matt

def debug(message):
    DEBUG = True
    if DEBUG:
        print("DEBUG: " + str(message))
    return
    
   

####### Debugging Section Stub-Out (IGNORE THIS, THIS IS JUST TO PREVENT ERRORS WHILE DEBUGGING)
####### WILL BE REPLACED WITH ACTUAL CLASSES
class Ship:
    def __init__(self):
        pass
        return

    def processUserInputs(self):
        pass
        return
        
    def ProcessTimeIncrement(self, timeStamp):
        pass
        return
        
    def checkCollision(self, location, size):
        pass
        return
        
class Asteroid:
    def __init__(self):
        pass
        return
        
    def ProcessTimeIncrement(self, timeStamp):
        pass
        return
        
    def getLocation(self):
        pass
        return
        
    def getSize(self):
        pass
        return

def displayGameScreen(object):
    pass
    return
        
        
def main(objectList):
    endOfRound = False
    while not endOfRound:
        timeStamp = time.clock()
        debug("TIME is: " + str(timeStamp))
        # Read User Inputs
        ship = objectList[0]
        ship.processUserInputs()

        # Process Time Increment
        debug("STARTING PROCESS TIME INCREMENT")
        for each in objectList:
            each.ProcessTimeIncrement(timeStamp)


        # Process Collision Detect
        debug("STARTING COLLISION DETECT")
        for each in objectList[1:]:
            Asteroid_Center_Location = each.getLocation()
            Asteroid_Size = each.getSize()
            collisionDetected = ship.checkCollision(Asteroid_Center_Location, Asteroid_Size)
            if collisionDetected:
                endOfRound = True
                break

        # Process Graphics
        debug("STARTING GRAPHICS ENGINE")
        displayGameScreen(objectList)
            
    return






if __name__ == "__main__":
    os.system("cls")
    objectList = []
    
    numberOfAsteroids = 5
    
    # Create the ship object
    ship = Ship()
    objectList.append(ship)
    
    # Create the asteroids
    for i in range(0, numberOfAsteroids + 1):
        asteroid = Asteroid()
        objectList.append(asteroid)
    
    
    main(objectList)