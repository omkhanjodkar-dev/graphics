print("[DEPRECATED]\n\nAn experiment to display lighting using 3D lighting coordinates as an animation on a sphere.\n\n")

import time

time.sleep(5)

import pygame

pygame.init()

l=1920
b=1080
z=35*3*3

td=0.125

screen = pygame.display.set_mode((l, b))

for i in range(l):
	for j in range(b):
		screen.set_at((i, j), (0, 0, 0))

def drawcircle(posx, posy, lightx, lighty, lightz):
	for i in range(int(posx-z/3)-1, int(posx+z/3)+2):
		for j in range(int(posy-z/3)-1, int(posy+z/3)+2):
			if (i-posx)**2+(j-posy)**2 <= (z/3)**2:
				k=z/3

				k=((z/3)**2-(i-posx)**2-(j-posy)**2)**(1/2)

				k=((z/3)**2-(posy-j)**2)**(1/2)
				# lx, ly, lz = (k/(z/3)*255, k/(z/3)*255, k/(z/3)*255)

				vectorx, vectory, vectorz = lightx-posx, lighty-posy, lightz-k

				vectorx, vectory, vectorz = vectorx/((vectorx**2+vectory**2+vectorz**2)**(1/2)), vectory/((vectorx**2+vectory**2+vectorz**2)**(1/2)), vectorz/((vectorx**2+vectory**2+vectorz**2)**(1/2))

				posix, posiy, posiz = posx/((posx**2+posy**2+k**2)**(1/2)), posy/((posx**2+posy**2+k**2)**(1/2)), k/((posx**2+posy**2+k**2)**(1/2))

				new_vector = (vectorx*posix+vectory*posiy+vectorz*posiz)

				# max_vector = abs((z/3)*(vectorx**2+vectory**2+vectorz**2)**(1/2))

				max_vector=1/2

				# print(new_vector, max_vector)

				new_vector = 1-abs(new_vector)

				# screen.set_at((i, j), (k/(z/3)*255, k/(z/3)*255, k/(z/3)*255))
				screen.set_at((i, j), (abs(new_vector)*255, abs(new_vector)*255, abs(new_vector)*255))

def erasecircle(posx, posy):
	for i in range(int(posx-z/3)-1, int(posx+z/3)+2):
		for j in range(int(posy-z/3)-1, int(posy+z/3)+2):	
			screen.set_at((i, j), (0, 0, 0))

density = 1
mass=((4/3)*3.14*((z/300)**3))/density
print(mass)

px=l/2
py=b/2

dpy=0

t=0

u=0
e=3/4

uh=0

g=0

while True:
	t+=td
	
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
		uh*=9.9/10
	if px > l-(z/3):
		px=l-(z/3)
		uh*=-e
	if px < 0+(z/3):
		px=0+(z/3)
		uh*=-e


	drawcircle(px, py, l/2, b/4, 1000)


	# screen.set_at((i, j), (lx, ly, lz))


	pygame.display.flip()

	erasecircle(px, py)



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()