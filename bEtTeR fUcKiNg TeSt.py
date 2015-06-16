#All Imports we need
import os
import sys
import random
import pygame
#Handle any special Initalizations
pygame.init()

height = 800
width = 800
size = (width, height) #here I am setting the size of the window
#background colors
black = (0, 0, 0)
white = (255, 255, 255)
#create a clock and a gameover variable
clock = pygame.time.Clock()
game_over = False #conditional that determines if game is playing
asteroid_list = [] #list where my astroid objects are stored
screen = pygame.display.set_mode(size)#this creates the window with the size specified
pygame.display.set_caption("Asteroids Errywhere")#sets the display to show the string
background = pygame.image.load("StarField.gif").convert() #sets background

class Asteroid(pygame.sprite.Sprite):#two function class for astroids
	def __init__(self): #constructs my astroids, and sets position and speed maybe add 
		pygame.sprite.Sprite.__init__(self)# call the parent class(sprite) constructor
		self.speed = random.randrange(5, 25)
		self.image = pygame.image.load("Asteroid.gif").convert() #Hard coded astroid value sets the image
		self.x_coord = random.randrange(0, width)#this line and the y below generate random start coordinates for each
		self.y_coord = random.randrange(0, height)#astroid based on the window size
		#self.position = (self.x_coord, self.y_coord)
		self.position = self.image.get_rect().move(self.x_coord, self.y_coord)###trial

	def get_location(self):
		return self.position

	def move(self):
		self.position = self.position.move(0, self.speed)
		if self.position.right > 800:
			self.position.left = 0
		elif self.position.left > 800:
			self.position.right = 0
		elif self.position.top > 800:
			self.position.bottom = 0
		elif self.position.bottom > 800:
			self.position.top = 0
		#elif self.position.bottom > 800:
		#	self.position = self.position.right and self.position.left



def spawn_astroids(): #this function spawns astroids and acts as main
	#screen.blit(background, (0, 0))
	for asteroid in range(10): #this line spawns the number in the range	
		individual_asteroid = Asteroid() #this creates an astroid object from the class
		asteroid_list.append(individual_asteroid) #this line appends it to the list above
	
	while game_over == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		for individual_asteroid in asteroid_list:
			screen.fill(black)#this line clears the screen so all the astroids will appear and move in the for loop below
			screen.blit(individual_asteroid.image, individual_asteroid.position)
			#screen.blit(background, (individual_asteroid.x_coord, individual_asteroid.y_coord))
		for individual_asteroid in asteroid_list:
			individual_asteroid.move()
			screen.blit(individual_asteroid.image, individual_asteroid.position)

		
		pygame.display.update()#brings all the changes of the while loop into effect
		pygame.time.delay(100)#waits a 1/10th of a second

spawn_astroids()

