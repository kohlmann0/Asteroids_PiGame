#import all modules and libraries needed
import os, sys
import random
import pygame
#from pygame.locals import * optional line that puts a limited set of constants and functions into global namespace
pygame.init() #here we initalize pygame
'''
size = width, height = 800, 850 #here I am setting the size of the window
speed = [1,1]#lower number == slower speed [horizontal axis, vertical axis]
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)#this creates the window with the size specified

cube = pygame.image.load("sgilogo2.gif")
#cube2 = pygame.image.load("sgilogo2.gif")
cube_rect = cube.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	cube_rect = cube_rect.move(speed)
	if cube_rect.left < 0 or cube_rect.right > width:
		speed[0] = -speed[0]
	if cube_rect.top < 0 or cube_rect.bottom > height:
		speed[1] = -speed[1]

		screen.fill(black)
		screen.blit(cube, cube_rect)
		pygame.display.flip()#this makes everything I have created on the screen become visible
'''


class Asteroid(pygame.sprite.Sprite):#two function class for astroids
	def __init__(self, image, height, speed): #constructs my astroids, and sets position and speed maybe add 
		pygame.sprite.Sprite.__init__(self)
		self.speed = speed
		self.image = image
		self.position = image.get_rect().move(0, height)

	def movement(self):#this moves the object one step
		self.position = self.position.move(0, self.speed)
		if self.position.right > 600:#here if it goes to far then it moves object back to the left
			self.position.left = 0


screen = pygame.display.set_mode((800, 800)) #set screen size
player = pygame.image.load("sgilogo2.gif").convert() #set player image
background = pygame.image.load("graph_paper.gif").convert() #set background image
screen.blit(background, (0,0)) #draw the background
objects = [] #list of objects/asteroids

#cube_rect = player.get_rect()

for x in range(3): #this line determines the number of objects/asteroids to be created
	o = Asteroid(player, x*.5, x)
	objects.append(o) #add my asteroid objects to the list above

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	for o in objects:
		screen.blit(background, o.position, o.position)
	for o in objects:
		o.movement()
		screen.blit(o.image, o.position)
	pygame.display.update()
	pygame.time.delay(100)


