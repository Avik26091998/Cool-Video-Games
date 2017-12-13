import pygame
import random
import time

pygame.init() # Initializes pygame module---(returns tuple)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
display_width = 1200    # window width 
display_height = 600    # window height
gameDisplay = pygame.display.set_mode((display_width, display_height)) # Returns Pygame.surfaceobject
pygame.display.set_caption('Slyther') # Title Name
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
block = 20     # block size
Applethickness = 30
FPS = 35
direction = "right"
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont("comicsansms", 25)     # Pygame text font -- ( , Size)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
img = pygame.image.load('snakehead.jpg')
appleimg = pygame.image.load('apple.jpg')

def pause():
	paused = True

	Msg_To_Screen("Paused", black, -100, "large")
	pygame.display.update()

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
			elif event.type == pygame.QUIT:
				pygame.quit()
				quit()
		#gameDisplay.fill(white)
		clock.tick(5)


def score(score):
	text = smallfont.render("Score : "+str(score), True, black)
	gameDisplay.blit(text, [0, 0])
	pygame.display.update()

def game_intro():

	intro = True

	while intro:

		gameDisplay.fill(white)
		Msg_To_Screen("Welcome To Slyther", green, -100, "large")
		Msg_To_Screen("Eat The Apples, Not Yourself", black, -30)
		Msg_To_Screen("The more Apples you eat the longer you get", black, 10)
		Msg_To_Screen("Press p to play, p during game to pause, c to continue and  q to quit", black, 50)

		pygame.display.update()
		clock.tick(4)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					intro = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
			elif event.type == pygame.QUIT:
				pygame.quit()
				quit()

def snake(block, snakelist):

	if direction == "right":
		head = pygame.transform.rotate(img, 270)
	if direction == "up":
		head = img
	if direction == "left":
		head = pygame.transform.rotate(img, 45 + 45)
	if direction == "down":
		head = pygame.transform.rotate(img, 180)

	gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

	for xny in snakelist[:-1]:
		pygame.draw.rect(gameDisplay, green, [xny[0], xny[1], block, block])

def text_objects(text, color, size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def Msg_To_Screen(msg, color, y_displace = 0, size = "small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (display_width / 2), (display_height / 2) + y_displace 
	gameDisplay.blit(textSurf, textRect) 
	#screen_text = font.render(msg, True, color)
	#gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])  # Put to screen(blit)--(text, coordinates)      # Render Msg. to screen 

def gameloop():
	global direction
	direction = "right"
	gameover = False
	gameexit = False
	lead_x = display_width / 2           # head of snake
	lead_y = display_height / 2          # head of snake
	lead_x_change = 10
	lead_y_change = 0
	snakelist = []
	snakelength = 1
	randAppleX = round(random.randrange(0, display_width - block) / 10.0) * 10.0    # x coordinate apple(rounding to nearest 10 for alignment with snake)
	randAppleY = round(random.randrange(0, display_height - block) / 10.0) * 10.0   # y coordinate apple(rounding to nearest 10 for alignment with snake)
	while not gameover:
		if gameexit == True:
			Msg_To_Screen("Game Over...Bitch!!!", red, -50, size =  "large")
			Msg_To_Screen("p - PlayAgain  q - quit", black, 50, size = "medium")
			pygame.display.update()
		while gameexit == True:
			#gameDisplay.fill(white)
			#Msg_To_Screen("Game Over...Bitch!!!", red, -50, size =  "large")
			#Msg_To_Screen("p - PlayAgain  q - quit", black, 50, size = "medium")
			#pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameover = True
					gameexit = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameover = True
						gameexit = False
					elif event.key == pygame.K_p:
						gameloop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # Events Taking Place In The Console
				gameover = True               # Quitting The Console
			if event.type == pygame.KEYDOWN:   # KEYDOWN - Pressing keyboard and vice-versa
				if event.key == pygame.K_UP:
					lead_y_change = -block
					lead_x_change = 0
					direction = "up"
				elif event.key == pygame.K_DOWN:
					lead_y_change = block
					lead_x_change = 0
					direction = "down"
				elif event.key == pygame.K_LEFT:
					lead_x_change = -block
					lead_y_change = 0
					direction = "left"
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block
					lead_y_change = 0
					direction = "right"
				elif event.key == pygame.K_p:
					pause()
		if lead_x > display_width or lead_y > display_height or lead_y < 0 or lead_x < 0:    # Boundary Checking
			gameexit = True
		lead_x += lead_x_change
		lead_y += lead_y_change
		
		gameDisplay.fill(white)
		#pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, Applethickness, Applethickness])  #position of Appple
		gameDisplay.blit(appleimg, (randAppleX, randAppleY))
		pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, block, block])   #(place, colour, [x, y, width, height])

		
		snakehead = []
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)

		if len(snakelist) > snakelength:        # 
			del snakelist[0]

		for eachelement in snakelist[:-1]:     #
			if eachelement == snakehead:
				gameexit = True

		snake(block, snakelist)
		pygame.display.update()

		score(snakelength - 1)

		# if lead_x >= randAppleX and lead_x <= randAppleX + Applethickness:
		# 	if lead_y >= randAppleY and lead_y <= randAppleY + Applethickness:
		# 		randAppleX = round(random.randrange(0, display_width - Applethickness))      # apple does'nt go out of boundary
		# 		randAppleY = round(random.randrange(0, display_height - Applethickness))     # apple does'nt go out of boundary
		# 		snakelength += 1

		if lead_x > randAppleX and lead_x < randAppleX + Applethickness or lead_x + block > randAppleX and lead_x + block < randAppleX + Applethickness:
			if lead_y > randAppleY and lead_y < randAppleY + Applethickness:
		 		randAppleX = round(random.randrange(0, display_width - Applethickness))      # apple does'nt go out of boundary
		 		randAppleY = round(random.randrange(0, display_height - Applethickness))     # apple does'nt go out of boundary
		 		snakelength += 1
			
			elif lead_y + block > randAppleY and lead_y + block < randAppleY + Applethickness:
				randAppleX = round(random.randrange(0, display_width - Applethickness))      # apple does'nt go out of boundary
		 		randAppleY = round(random.randrange(0, display_height - Applethickness))     # apple does'nt go out of boundary
		 		snakelength += 1


		clock.tick(FPS)
	pygame.quit()
	quit()
game_intro()
gameloop()