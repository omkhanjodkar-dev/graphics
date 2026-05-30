import pyautogui
import os
import time
import pygame

pygame.init()

l=1920
b=1080
z=35*3

td=0.125

screen = pygame.display.set_mode((l, b))

for i in range(l):
	for j in range(b):
		screen.set_at((i, j), (0, 0, 0))

def drawcircle(posx, posy):
	# print("ni hao! wo jiao drawcircle.")
	# print(posx, posy)
	# print(int(posy-z/3)-1, int(posy-z/3)+2)
	# print(int(posx-z/3)-1, int(posx+z/3)+2)
	for i in range(int(posx-z/3)-1, int(posx+z/3)+2):
		for j in range(int(posy-z/3)-1, int(posy+z/3)+2):
			# print("shenmyisi?")
			if (i-posx)**2+(j-posy)**2 <= (z/3)**2:
				k=((z/3)**2-(i-posx)**2-(j-posy)**2)**(1/2)
				# print(i, j)
				screen.set_at((i, j), (k/(z/3)*255, k/(z/3)*255, k/(z/3)*255))

def erasecircle(posx, posy):
	for i in range(int(posx-z/3)-1, int(posx+z/3)+2):
		for j in range(int(posy-z/3)-1, int(posy+z/3)+2):	
			screen.set_at((i, j), (0, 0, 0))


def drawboard(posx, posy, sl, sb):
	for i in range(int(posx-sl/2), int(posx+sl/2)):
		for j in range(int(posy-sb/2), int(posy+sb/2)):
			screen.set_at((i, j), (255, 255, 255))

def eraseboard(posx, posy, sl, sb):
	for i in range(int(posx-sl/2), int(posx+sl/2)):
		for j in range(int(posy-sb/2), int(posy+sb/2)):
			screen.set_at((i, j), (0, 0, 0))

def clearscreen():
	for i in range(0, l):
		for j in range(0, b):
			screen.set_at((i, j), (0, 0, 0))

density = 1
mass=((4/3)*3.14*((z/300)**3))/density
print(mass)

px=l/2
py=0

dpy=0

t=0
t_i=time.time()
# t_f=0

u=25
e=1

g=0

uh=25

fr=0

sl=200
sb=10

bx=b/2
by=b-50

while True:
	cx, cy = pyautogui.position()

	bx = cx

	fr+=1

	t_f=time.time()
	t+=t_f-t_i

	try:
		if fr%200==0:
			print("FPS:", 1/(t_f-t_i))
	except Exception as _:
		pass
	t_i=time.time()

	# print(t)

	dpy=u*(td)+0.5*g*td*td
	py+=dpy

	px+=td*uh

	# u=(u**2+2*g*(dpy))**(1/2)
	u+=g*td
	
	if py < 0+(z/3):
		py=0+(z/3)
		u*=-e
	if py > b-(z/3):
		py=b-(z/3)
		u*=-e
		break
		# uh*=9.9/10
	if px > l-(z/3):
		px=l-(z/3)
		uh*=-e
	if px < 0+(z/3):
		px=0+(z/3)
		uh*=-e

	if py > by-sb/2-(z/3) and px < bx+sl/2 and px > bx-sl/2:
		py=by-sb/2-(z/3)
		u*=-e


	drawcircle(px, py)

	drawboard(bx, by, sl, sb)

	# screen.set_at((i, j), (lx, ly, lz))


	pygame.display.flip()

	erasecircle(px, py)

	eraseboard(bx, by, sl, sb)



# running = True
# while running:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False

pygame.quit()