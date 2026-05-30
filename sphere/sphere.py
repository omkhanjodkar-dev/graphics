import time
import pygame

pygame.init()

l=200
b=200
z=35*3

td=0.25

screen = pygame.display.set_mode((l, b))

density = 1
mass=((4/3)*3.14*((z/300)**3))/density
print(mass)

px=l/2
py=0

dpy=0

t=0

u=0
e=1/2

uh=10

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
		uh*=9.5/10
	if px > l-(z/3):
		px=l-(z/3)
		uh*=-e
	if px < 0+(z/3):
		px=0+(z/3)
		uh*=-e

	for i in range(0, l):
		for j in range(0, b):
			# 3D

			# a = 0
			# for k in range(z, 0, -1):
			# 	if (i-px)**2+(j-py)**2+k**2<=(z/3)**2:
			# 		a = k
			# 		break
			# lx, ly, lz = (a/(z/2)*255, a/(z/2)*255, a/(z/2)*255)
			# if lx > 255:
			# 	lx=255
			# if ly>255:
			# 	ly=255
			# if lz>255:
			# 	lz=255

			# 3D mid

			lx, ly, lz = (0, 0, 0)
			if (i-px)**2+(j-py)**2<=(z/3)**2:
				k = ((z/3)**2-(i-px)**2-(j-py)**2)**(1/2)
				lx, ly, lz = (k/(z/3)*255, k/(z/3)*255, k/(z/3)*255)

			# 2D

			# lx, ly, lz = (0, 0, 0)
			# if (i-px)**2+(j-py)**2<=(z/3)**2:
			# 	lx, ly, lz = (255, 255, 255)

			# print((255-lx, 255-ly, 255-lz))
			screen.set_at((i, j), (lx, ly, lz))


	pygame.display.flip()



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()