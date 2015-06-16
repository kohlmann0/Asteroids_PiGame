import pygame
import random
import math


#intializes pygame
#pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE = (800,800)
#screen = pygame.display.set_mode(SIZE)
#pygame.display.set_caption("Asteroids")
#initializes clock and gameOver state
#clock = pygame.time.Clock()
#gameOver = False

# class Asteroid(pygame.sprite.Sprite):
#     def __init__(self,position,image,image_info):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = position[0]
#         self.y = position[1]
#         self.image = pygame.image.load(image).convert()
#         self.image_center = image_info[1]
#         self.image_size = image_info[0]
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

#     def update(self):
#         #if self.y > SIZE[0]/2:
#         self.y -= .25
#         self.x = random.randrange(0,400)

#     def draw(self):
#         self.image.set_colorkey(BLACK)
#         screen.blit(self.image,[self.x,self.y])


#sets 10 asteroids to fall from the screen.


#used for calculating forward direction based on angle provided
def angle_to_vector(ang):
    return [math.cos(ang), -math.sin(ang)]
 
def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
 
 #pygame function used to take in image and angle and rotate it
 #image must be a square to work.
def rot_center(image, angle):
    '''rotate an image while keeping its center and size'''
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
 
# Ship class - child class of pygame sprite class
# currently image is name of file
class Ship(pygame.sprite.Sprite):
    def __init__(self, pos, vel, angle):
        pygame.sprite.Sprite.__init__(self)#
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = angle
        self.thrust = False
        self.angle_vel = 0
        self.image = pygame.image.load("Graphics_Assets\ship_1.png")
        #self.image_center = image_info[1]
        #self.image_size = image_info[0]
        self.rect = self.image.get_rect()
        #x,y coordinates used for determing what the forward direction is
        self.forward = [0,0]
    
    def get_position(self):
        return (self.pos[0],self.pos[1])

    def get_angle(self):
        return self.angle
    #sets thrust to true if up arrow is pressed.
    def set_thrust(self, thrust):
        self.thrust = thrust
 
    #color value is used to set the background color of the image to black so the background image is transparent.
    def draw(self,screen):
        self.image.set_colorkey(BLACK)
        screen.blit(rot_center(self.image, self.angle),self.pos)
 
    def ProcessTimeIncrement(self,size):
        #added a friction element so ship will stop moving if key is not pressed.
        acc = 0.5
        fric = acc / 20
        
        self.angle += self.angle_vel
 
        self.forward = angle_to_vector(math.radians(self.angle))
 
        if self.thrust:
            self.vel[0] += self.forward[0] * acc
            self.vel[1] += self.forward[1] * acc
 
        self.vel[0] *= (1 - fric)
        self.vel[1] *= (1 - fric)
 
        # update position, right now my screen dimensions are 
        self.pos[0] = (self.pos[0] + self.vel[0]) % (size[0])
        self.pos[1] = (self.pos[1] + self.vel[1]) % (size[1])
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def set_angle_vel(self, vel):
        self.angle_vel = vel

    def processUserInputs(self,event):
        self.keydown(event)
        self.keyup(event)

    def checkCollision(self,asteroid_center, asteroid_location):
        pass

    def keydown(self,event):
#     ang_vel is how fast the ship will rotate
        ang_vel = 4.5
        if event.key == pygame.K_LEFT:
            self.set_angle_vel(ang_vel)
        if event.key == pygame.K_RIGHT:
            self.set_angle_vel(-ang_vel)
        if event.key == pygame.K_UP:
            self.set_thrust(True)
        if event.key == pygame.K_SPACE:
            self.shoot()

    def keyup(self,event):
        if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
            self.set_angle_vel(0)
        if event.key == pygame.K_UP:
            self.set_thrust(False)

 

#hardcoded ship values. 40 x 40 is image size, 20 is image center
# ship_info = ([40, 40], 20)
# ship_image = 'ship.png'

# #ship starts in center of screen with initial velocity of [0,0]
# #ship starts with initial angle of 0


# def keydown(event,ship_object):
#     #ang_vel is how fast the ship will rotate
#     ang_vel = 4.5
#     raw_input("Hello")
#     if event.key == pygame.K_LEFT:
#         ship_object.set_angle_vel(ang_vel)
#         print "Left"
#     if event.key == pygame.K_RIGHT:
#         ship_object.set_angle_vel(-ang_vel)
#     if event.key == pygame.K_UP:
#         ship_object.set_thrust(True)
#         print "Up"
#     if event.key == pygame.K_SPACE:
#         ship_object.shoot()
            
 
# #keyup handler
# def keyup(event,ship_object):
 
#     if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
#         ship_object.set_angle_vel(0)
#     if event.key == pygame.K_UP:
#         ship_object.set_thrust(False)



# #asteroid_info = ([40, 40], 20)
# #asteroid_image = 'asteroid.png'
# #asteroid_list = []
# #ship = Ship([SIZE[0]/2, SIZE[1]/2], [0,0], 0, ship_image, ship_info)


# # for i in range(50):
# #     x = random.randrange(0,800)
# #     y = random.randrange(0,800)
# #     position_asteroid = [x,y]
# #     print position_asteroid
# #     i = Asteroid(position_asteroid,asteroid_image, asteroid_info)
# #     asteroid_list.append(i)


# while gameOver == False:
#     for event in pygame.event.get():#user does something
#         #if user clicked close
#         if event.type == pygame.QUIT:
#             gameOver = True
#         elif event.type == pygame.KEYDOWN:
#             keydown(event)
#         elif event.type == pygame.KEYUP:
#             keyup(event)
    #screen.fill(BLACK)#clears the screen and sets the screen background
    #needs to be done before any drawing command is issued.
    #asteroid_list.update()
#     ship.update(SIZE)
#     for asteroid in asteroid_list:

#         if pygame.sprite.collide_rect(ship,asteroid):
#             print "Collide",ship.rect,asteroid.rect
#             asteroid_list.remove(asteroid)
#     ship.draw(screen)
#     for asteroid in asteroid_list:
#         asteroid.draw()
#     #asteroid_list.draw(screen)
#     #for asteroid in asteroid_hit_list:
#         #asteroid.draw()

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()