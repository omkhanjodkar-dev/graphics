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

density = 1
mass=((4/3)*3.14*((z/300)**3))/density
print(mass)

px=l/2
py=0

dpy=0

t=0

u=0
e=3/4

uh=50

while True:
	t+=td
	
	dpy=u*(td)+0.5*9.8*td*td
	py+=dpy

	px+=td*uh

	# u=(u**2+2*9.8*(dpy))**(1/2)
	u+=9.8*td
	
	if py < 0+(z/3):
		py=0+(z/3)
		u*=-e
	if py > b-(z/3):
		py=b-(z/3)
		u*=-e
		uh*=9.9/10
	if px > l-(z/3):
		px=l-(z/3)
		uh*=-e
	if px < 0+(z/3):
		px=0+(z/3)
		uh*=-e


	drawcircle(px, py)


	# screen.set_at((i, j), (lx, ly, lz))


	pygame.display.flip()

	erasecircle(px, py)



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()