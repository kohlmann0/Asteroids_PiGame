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
from random import *
import math
pygame.init()

# from ship import *              # Ryan
# from AsteroidsFTW import *      # Rob
from display_functions import *           # Matt

def debug(message):
    DEBUG = True
    if DEBUG:
        print("DEBUG: " + str(message))
    return
    
   

##### Debugging Section Stub-Out (IGNORE THIS, THIS IS JUST TO PREVENT ERRORS WHILE DEBUGGING)
##### WILL BE REPLACED WITH ACTUAL CLASSES
class Ship:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.angle = randint(0,360)
        self.speed = 1
        return

    def processUserInputs(self):
        pass
        return
        
    def ProcessTimeIncrement(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        if self.x > 800:
            self.x -= 800
        if self.x < 0:
            self.x += 800
        if self.y > 800:
            self.y -= 800
        if self.y < 0:
            self.y += 800
        return
        
    def checkCollision(self, location, size):
        pass
        return

    def get_position(self):
        pos = (self.x, self.y)
        return pos

    def get_angle(self):
        return self.angle
        
class Asteroid:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.angle = randint(0,360)
        self.speed = 1
        return
        
    def ProcessTimeIncrement(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        if self.x > 800:
            self.x -= 800
        if self.x < 0:
            self.x += 800
        if self.y > 800:
            self.y -= 800
        if self.y < 0:
            self.y += 800
        return
        
    def get_location(self):
        return (self.x, self.y)
        
    def getSize(self):
        pass
        return
'''
def displayGameScreen(objectList, screen):
    backgroundimage = pygame.image.load("StarField.gif")
    background = pygame.transform.scale(backgroundimage,(width,height))
    screen.blit(background, (0,0))
    
    ship = objectList[1]
    shipImage = pygame.image.load("ship.png")
    shipLocation = ship.getLocation()
    screen.blit(shipImage, shipLocation)
    
    asteroidImage = pygame.image.load("Asteroid.gif")
    for each in objectList[1:]:
        asteroidLocation = each.getLocation()
        screen.blit(asteroidImage,asteroidLocation)

    pygame.display.flip()
    
    return
'''
def displayStartupScreen(screen):
    pygame.display.set_caption('Asteroids For The Win!')
    selection = 1    
    while True:
        # Process Menu Selection Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selection += 1
                if event.key == pygame.K_UP:
                    selection -= 1
                if event.key == pygame.K_RETURN:
                    return selection
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            
            if selection > 2:
                selection = 1
            if selection < 1:
                selection = 2
        
        # Setup Background
        backgroundimage = pygame.image.load("StarField.gif")
        background = pygame.transform.scale(backgroundimage,(width,height))
        
        # Setup "ASTEROIDS" Title
        font = pygame.font.Font(None, 100)
        asteroidText = font.render("ASTEROIDS", 1, (255,255,255), (0,0,0))
        asteroidTextPos = asteroidText.get_rect()
        asteroidTextPos.centerx = background.get_rect().centerx
        asteroidTextPos.centery = (background.get_rect().centery - 50)
        
        # Setup "START" Menu button
        font = pygame.font.Font(None, 36)
        if selection == 1: 
            startText = font.render("START GAME", 1, (255,255,255), (100,100,100))
        else:
            startText = font.render("START GAME", 1, (255,255,255), (0,0,0))
        startTextPos = startText.get_rect()
        startTextPos.centerx = background.get_rect().centerx
        startTextPos.centery = (background.get_rect().centery + 20)
            
        # Setup "OPTIONS" Menu button
        if selection == 2: 
            optionsText = font.render("OPTIONS", 1, (255,255,255), (100,100,100))
        else:
            optionsText = font.render("OPTIONS", 1, (255,255,255), (0,0,0))
        optionsTextPos = optionsText.get_rect()
        optionsTextPos.centerx = background.get_rect().centerx
        optionsTextPos.centery = (background.get_rect().centery + 50) 
        
        # Blit Screen
        screen.blit(background, (0,0))
        screen.blit(asteroidText, asteroidTextPos)
        screen.blit(startText, startTextPos)
        screen.blit(optionsText, optionsTextPos)
        pygame.display.flip()
    
    #raw_input("Press Enter to continue")
    return screen



# Single Round of the main game loop    
def main(objectList, screen, lives):
    endOfRound = False
    clock = pygame.time.Clock()
    while not endOfRound:
        clock.tick(60) # Game will render at 60 frames per second
        timeStamp = time.clock()
        debug("TIME is: " + str(timeStamp))
        # Read User Inputs
        debug("")
        ship = objectList[0]
        ship.processUserInputs()

        # Process Time Increment
        debug("STARTING PROCESS TIME INCREMENT")
        for each in objectList:
            each.ProcessTimeIncrement()


        # Process Collision Detect
        debug("STARTING COLLISION DETECT")
        for each in objectList[1:]:
            Asteroid_Center_Location = each.get_location()
            Asteroid_Size = each.getSize()
            collisionDetected = ship.checkCollision(Asteroid_Center_Location, Asteroid_Size)
            if collisionDetected:
                lives -= 1
                # Reset 
                break

        # Process Graphics
        debug("STARTING GRAPHICS ENGINE")
        displayGameScreen(objectList, screen)
        if lives == 0:
            return True
    
        
    return False # Change this to a gameOver test (No more lives, not more, whatever)





# Game Starting point
if __name__ == "__main__":
    # Clear Console Screen
    os.system("cls")
    
    # Set Screen parameters
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    
    # Display Startup Screen, and return menu selection (Start Game = 1, Options = 2)
    menuSelection = displayStartupScreen(screen)
    
    # Start Game Menu Option Selected
    if menuSelection == 1:
        lives = 3
        gameOver = False
        while not gameOver:
            # Hard coded number of asteroids. May change later depending on difficulty/level/rounds.
            numberOfAsteroids = 20
        
            # Initialize our Object list
            objectList = []
            
            # Create the ship object
            ship = Ship()
            objectList.append(ship)
            
            # Create the asteroids
            asteroidImage = pygame.image.load("sgilogo2.gif").convert() #set player image
            for i in range(0, numberOfAsteroids + 1):
                asteroid = Asteroid()
                objectList.append(asteroid)
            
            # Start the main game loop        
            gameOver = main(objectList, screen, lives)
            
    
    # Options Menu Selected
    if menuSelection == 2:
        pass
     
        
        
        
        
        
        
        
        