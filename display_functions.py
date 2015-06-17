from random import *
import pygame
import sys
from pygame.locals import *

pygame.init()

'''
#TESTING CLASSES
class Ship():
    def __init__(self):
        self.pos = [100, 100]
        self.angle = 230

    def get_position(self):
        return self.pos

    def get_angle(self):
        return self.angle

class Asteroid():
    def __init__(self, id, locX, locY):
        self.id = id
        self.location = [locX, locY]

    def get_location(self):
        return self.location
'''

def rot_center(image, angle):
    '''rotate an image while keeping its center and size'''
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def displayGameScreen(objectList, gameScreen):
<<<<<<< HEAD
    #SET BACKGROUND
    bg = pygame.image.load("Graphics_Assets\space_background.bmp")
    gameScreen.blit(bg, (0,0))
    pygame.display.update()

    #SET SHIP
    ship = objectList[0]
    shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
    shipLoc = ship.get_position()
    shipAngle = ship.get_angle()
    rotShip = rot_center(shipImg, shipAngle)

    shipImg.set_colorkey((0,0,0))
    gameScreen.blit(rotShip, (shipLoc))
    pygame.display.update()

    #SET ASTEROIDS
    asteroids = objectList[1:]
    for a in asteroids:
        aImg = pygame.image.load("Graphics_Assets\meteor.png")
        aLoc = a.get_location()
        a.rect = aImg.get_rect()
        a.rect.x = a.x
        a.rect.y = a.y
        gameScreen.blit(aImg, (aLoc))

    asteroid_list = list(objectList[1:])
    for asteroid in asteroid_list:
            if pygame.sprite.collide_rect(ship,asteroid):
                objectList.remove(asteroid)

    #DISPLAY UPDATE
    pygame.display.update()
=======

	#SET BACKGROUND
	bg = pygame.image.load("Graphics_Assets\star_ground.bmp")
	gameScreen.blit(bg, (0,0))
	
	#SET SHIP
	ship = objectList[0]
	shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
	shipLoc = ship.get_position()
	shipAngle = ship.get_angle()
	rotShip = rot_center(shipImg, shipAngle)

	shipImg.set_colorkey((0,0,0))
	gameScreen.blit(rotShip, (shipLoc))
	
	#SET ASTEROIDS or BULLET
	'''
	for index, each in enumerate(objectList)
		if isininstance(each, Asteroid):
			aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
			aLoc = a.get_location()
			gameScreen.blit(aImg, (aLoc))
		
		elif isininstance(each, Bullet):
			bImg = pygame.image.load("Graphics_Assets\##########")
			bLoc = each.get_position()
			bAngle = each.get_angle()
			rotBullet = rot_center(bImg, (bLoc))

			bImg.set_colorkey((0,0,0))
			gameScreen.blit(rotBullet, (bLoc))
			pygame.display.update()
	'''
	asteroids = objectList[1:]
	for a in asteroids:
		aImg = pygame.image.load("Graphics_Assets\meteor_retro_3.png")
		aLoc = a.get_location()
		gameScreen.blit(aImg, (aLoc))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#DISPLAY UPDATE
	pygame.display.update()
>>>>>>> 953313d17a8e29042d9660338075343a492d8c30

    #SET BACKGROUND
    bg = pygame.image.load("Graphics_Assets\space_background.bmp")
    gameScreen.blit(bg, (0,0))
    pygame.display.update()

    #SET SHIP
    ship = objectList[0]
    shipImg = pygame.image.load("Graphics_Assets\ship_1.png")
    shipLoc = ship.get_position()
    shipAngle = ship.get_angle()
    rotShip = rot_center(shipImg, shipAngle)

    shipImg.set_colorkey((0,0,0))
    gameScreen.blit(rotShip, (shipLoc))
    pygame.display.update()

    #SET ASTEROIDS
    asteroids = objectList[1:]
    for a in asteroids:
        aImg = pygame.image.load("Graphics_Assets\meteor.png")
        aLoc = a.get_location()
        a.rect = aImg.get_rect()
        a.rect.x = a.x
        a.rect.y = a.y
        gameScreen.blit(aImg, (aLoc))

    asteroid_list = list(objectList[1:])
    for asteroid in asteroid_list:
            if pygame.sprite.collide_rect(ship,asteroid):
                objectList.remove(asteroid)

    #DISPLAY UPDATE
    pygame.display.update()



'''
#TESTING PURPOSES
s = Ship()
objectList = [s]


for a in range(10):
    locX = randint(10,290)
    locY = randint(10,290)
    
    asteroid = Asteroid(a, locX, locY)
    objectList.append(asteroid)


gameScreen = pygame.display.set_mode((300, 300))
while True:
    displayGameScreen(objectList, gameScreen)
'''