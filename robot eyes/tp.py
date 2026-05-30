import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

padx = 0
pady = 0

def inrange(eq, i, d):
	return eq >= i-d and eq <= i+d

def white(x, y, color=(255, 255, 255)):
	screen.set_at((x+padx, y+pady), (min(color[0], 255), min(color[0], 255), min(color[2], 255)))



r = 300
max_color = 255
d = 10

for i in range(200, 300, d):
	for j in range(300, 500, d):
		for x in range(int(i-r**(1/2)), int(i+r**(1/2))):
			for y in range(int(j-r**(1/2)), int(j+r**(1/2))):
				if (x-i)**2+(y-j)**2 <= r:
					white(x, y, color = (max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2))), max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2))), max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2)))))
					

for i in range(500, 600, d):
	for j in range(300, 500, d):
		for x in range(int(i-r**(1/2)), int(i+r**(1/2))):
			for y in range(int(j-r**(1/2)), int(j+r**(1/2))):
				if (x-i)**2+(y-j)**2 <= r:
					white(x, y, color = (max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2))), max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2))), max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2)))))

pygame.display.flip()

#d=3
#ji=60
#jf=635
#i=300-20
#ff=500+20


#for j in range(ji, jf, d):
	#for i in range(int(ii+(j-ji)/(jf-ji)*((iff-ii)/2)), int(iff-(j-ji)/(jf-ji)*((iff-ii)/2)), d):
#		for x in range(int(i-r**(1/2)), int(i+r**(1/2))):
			#for y in range(int(j-r**(1/2)), int(j+r**(1/2))):
#				if (x-i)**2+(y-j)**2 <= r:
					#white(x, y, color = (max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2))), max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2))), max(screen.get_at((x, y))[0], max_color-max_color*((x-i)**2+(y-j)**2)**(1/2)/((r)**(1/2)))))

pygame.display.flip()

print("done!")

while True:
	pass		
