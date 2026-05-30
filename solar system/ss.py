import math
import pygame

pygame.init()

w = 1980
h = 1080

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
kclock = 10

d = 10

sunx = w/2
suny = h/2
sunr = 50
sunc = (255, 211, 61)

earthx = 150
earthy = 150
earthr = 15
rearth = 200
earthc = (50, 50, 250)
kearth = d/365

moonx = 185
moony = 185
moonr = 5
rmoon = 35
moonc = (50, 59, 50)
kmoon = d

mercuryx = 100
mercuryy = 100
mercuryr = 7.5
rmercury = 75
mercuryc = (177,173,173)
kmercury = d/88

venusx = 125
venusy = 125
venusr = 10
rvenus = 125
venusc = (248, 226, 176)
kvenus = d/225

marsx = 175
marsy = 175
marsr = 8
rmars = 250
marsc = (193, 68, 14)
kmars = d/687

jupiterx = 350
jupitery = 350
jupiterr = 25
rjupiter = 350
jupiterc = (201,144,57)
kjupiter = d/4380

saturnx = 450
saturny = 450
saturnr = 20
rsaturn = 450
saturnc = (234, 214, 184)
ksaturn = d/10756

uranusx = 500
uranusy = 500
uranusr = 10
ruranus = 525
uranusc = (172, 229, 238)
kuranus = d/30687

neptunex = 600
neptuney = 600
neptuner = 8
rneptune = 600
neptunec = (124, 183, 187)
kneptune = d/60190

def color(r, x, y, c):
	for i in range(int(x-r), int(x+r)):
		for j in range(int(y-r), int(y+r)):
			if (i-x)**2+(j-y)**2<=r**2:
				screen.set_at((i, j), c)

def clear():
	screen.fill((0, 0, 0))

theta_deg = 0

running = True
while running:
	# theta += 10
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			running = False
	"""
	for x in range(0, w):
		for y in range(0, h):
			if (x-sunx)**2+(y-suny)**2<=sunr**2:
				screen.set_at((x, y), sunc)
			elif (x-earthx)**2+(y-earthy)**2<=earthr**2:
				screen.set_at((x, y), earthc)
			elif (x-moonx)**2+(y-moony)**2<=moonr**2:
				screen.set_at((x, y), moonc)
			elif (x-mercuryx)**2+(y-mercuryy)**2<=mercuryr**2:
				screen.set_at((x, y), mercuryc)
			elif (x-venusx)**2+(y-venusy)**2<=venusr**2:
				screen.set_at((x, y), venusc)
			elif (x-marsx)**2+(y-marsy)**2<=marsr**2:
				screen.set_at((x, y), marsc)
			else:
				screen.set_at((x, y), (0,0,0))
				#pass
	"""
	clear()
	color(sunr, sunx, suny, sunc)
	color(mercuryr, mercuryx, mercuryy, mercuryc)
	color(venusr, venusx, venusy, venusc)
	color(earthr, earthx, earthy, earthc)
	color(moonr, moonx, moony, moonc)
	color(marsr, marsx, marsy, marsc)
	color(jupiterr, jupiterx, jupitery, jupiterc)
	color(saturnr, saturnx, saturny, saturnc)
	color(uranusr, uranusx, uranusy, uranusc)
	color(neptuner, neptunex, neptuney, neptunec)

	theta = math.radians(theta_deg)

	# sunx = w/2-(100*math.cos(theta))
	# suny = h/2-(100*math.sin(theta))

	earthx = sunx-(rearth*math.cos(kearth*theta))
	earthy = suny-(rearth*math.sin(kearth*theta))

	moonx = earthx-(rmoon*math.cos(kmoon*theta))
	moony = earthy-(rmoon*math.sin(kmoon*theta))

	mercuryx = sunx-(rmercury*math.cos(kmercury*theta))
	mercuryy = suny-(rmercury*math.sin(kmercury*theta))

	venusx = sunx-(rvenus*math.cos(kvenus*theta))
	venusy = suny-(rvenus*math.sin(kvenus*theta))

	marsx = sunx-(rmars*math.cos(kmars*theta))
	marsy = suny-(rmars*math.sin(kmars*theta))

	jupiterx = sunx-(rjupiter*math.cos(kjupiter*theta))
	jupitery = suny-(rjupiter*math.sin(kjupiter*theta))

	saturnx = sunx-(rsaturn*math.cos(ksaturn*theta))
	saturny = suny-(rsaturn*math.sin(ksaturn*theta))

	uranusx = sunx-(ruranus*math.cos(kuranus*theta))
	uranusy = suny-(ruranus*math.sin(kuranus*theta))

	neptunex = sunx-(rneptune*math.cos(kneptune*theta))
	neptuney = suny-(rneptune*math.sin(kneptune*theta))

	pygame.display.flip()
	theta_deg += kclock*clock.tick(165)

pygame.quit()