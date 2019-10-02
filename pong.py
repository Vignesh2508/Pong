import pygame
#import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

WIDTH = 800
HEIGHT = 600

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80

PADDLE_1_xpos = 0
PADDLE_1_ypos = 300

PADDLE_2_xpos = WIDTH - PADDLE_WIDTH
PADDLE_2_ypos = 300

temp = 0

FPS = 30

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")

gameMode = False
xpos = WIDTH/2
ypos = HEIGHT/2

x_change = -5
y_change = -2.5

score_1 = 0 

score_2 = 0

def boundaries(xpos,ypos,x_change,y_change, gameMode):
	if xpos < 0:
		text = font.render("GAME OVER",1,black)
		win.blit(text, (WIDTH/2,HEIGHT/2))
		pygame.time.delay(100)
		gameMode = True
	if xpos > WIDTH-10:
		text = font.render("GAME OVER",1,black)
		win.blit(text, (WIDTH/2,HEIGHT/2))
		pygame.time.delay(100)
		gameMode = True
	if ypos < 0:
		temp = y_change
		y_change = -1 * temp
	if ypos > HEIGHT-10:
		temp = y_change
		y_change = -1 * temp
	return x_change, y_change, gameMode

def paddle_coll_window(PADDLE_1_ypos, PADDLE_2_ypos):
	if PADDLE_1_ypos < 0: 
		PADDLE_1_ypos = 0
	if PADDLE_1_ypos > HEIGHT - PADDLE_HEIGHT:
		PADDLE_1_ypos = HEIGHT - PADDLE_HEIGHT
	if PADDLE_2_ypos < 0:
		PADDLE_2_ypos = 0 
	if PADDLE_2_ypos > HEIGHT - PADDLE_HEIGHT:
		PADDLE_2_ypos = HEIGHT - PADDLE_HEIGHT
	return PADDLE_1_ypos, PADDLE_2_ypos

def paddle_coll_ball(xpos,ypos,PADDLE_1_xpos,PADDLE_1_ypos,PADDLE_2_xpos,PADDLE_2_ypos,x_change,y_change,score_1,score_2):
	if xpos < PADDLE_1_xpos + PADDLE_WIDTH:
		if ypos >= PADDLE_1_ypos and ypos <= PADDLE_1_ypos + PADDLE_HEIGHT:
			#temp = random.randint(-10,10)
			x_change = 5 + (score_1 * 0.5) # to control the speed to the score
			temp = y_change
			y_change = 1 * temp
			score_1 += 1

	if xpos + 10 > PADDLE_2_xpos:
		if ypos >= PADDLE_2_ypos and ypos <= PADDLE_2_ypos + PADDLE_HEIGHT:
			#temp = random.randint(-10,10)
			x_change = -5 - (score_2 * 0.5) # to control the speed to the score
			temp = y_change
			y_change = 1 * temp
			score_2 += 1

	return x_change, y_change,score_1,score_2

clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 20, True)

while not gameMode:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameMode = True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_w:
			PADDLE_1_ypos += -10
		if event.key == pygame.K_s:
			PADDLE_1_ypos += 10
		if event.key == pygame.K_UP:
			PADDLE_2_ypos += -10
		if event.key == pygame.K_DOWN:
			PADDLE_2_ypos += 10

	xpos = xpos + x_change
	ypos = ypos + y_change
	
	win.fill(white)

	# Print the score on the window
	text = font.render(str(score_1),1,black)
	win.blit(text, (20,20))
	text = font.render(str(score_2),1,black)
	win.blit(text, (WIDTH-20,20))
	

	#Drawing the shapes as rectangles both the ball and the paddles
	pygame.draw.rect(win, red, (xpos,ypos,10,10))
	pygame.draw.rect(win, black, (PADDLE_1_xpos,PADDLE_1_ypos,PADDLE_WIDTH,PADDLE_HEIGHT))
	pygame.draw.rect(win, black, (PADDLE_2_xpos,PADDLE_2_ypos,PADDLE_WIDTH,PADDLE_HEIGHT))

	#Stopping the paddle at the both the end of windows
	PADDLE_1_ypos, PADDLE_2_ypos = paddle_coll_window(PADDLE_1_ypos, PADDLE_2_ypos)
	
	#Collision of ball and paddle
	x_change, y_change, score_1, score_2 = paddle_coll_ball(xpos,ypos,PADDLE_1_xpos,PADDLE_1_ypos,PADDLE_2_xpos,PADDLE_2_ypos,x_change,y_change,score_1,score_2)

	#function to make the collision with the boundaries aka window
	x_change, y_change, gameMode = boundaries(xpos,ypos,x_change,y_change, gameMode)
	

	clock.tick(FPS)
	pygame.display.update()