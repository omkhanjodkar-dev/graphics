import keyboard
import os
os.system("pip install pygame pyautogui")
import random
import pyautogui
import time
import pygame



# for the end screen getting pixels from end.png
from PIL import Image

im = Image.open("end.png")

w, h = im.size

pixels = im.load()

im2 = Image.open("start_play.png")

w2, h2 = im2.size

pixels2 = im2.load()

im3 = Image.open("start_exit.png")

w3, h3 = im3.size

pixels3 = im3.load()
#end ends here

direction_dict = {1: "right", 2:"left", 3:"up", 4:"down"}

pygame.init()

time_def = 0

l = 1000
b = l

div = l/50

d=int(l/div)

screen = pygame.display.set_mode((l, b))


def fill(pixel, color=(0, 0, 255)):
	pixel[0] = pixel[0]%div
	pixel[1] = pixel[1]%div
	if pixel[0] == 0:
		pixel[0] = div
	if pixel[1] == 0:
		pixel[1] = div
	for i in range(int(d*(pixel[0]-1)), int(d*pixel[0])):
		for j in range(int(d*(pixel[1]-1)), int(d*pixel[1])):
			screen.set_at((i, j), color)

def clear():
	for i in range(0, l):
		for j in range(0, b):
			screen.set_at((i, j), (0, 0, 0))


global direction
direction = "right"
head = [5, 5]
# tail = [int(i) for i in head]

t = time.time()
n=1
# ctr=0

snake = [[head[0]-1, head[1]], head, [head[0]+1, head[1]]]
head=[6, 5]
for i in snake:
	fill(i)
print(snake)

fruit = [random.randint(1, d), random.randint(1, d)]

global go_up
go_up = False

global live
live = 1

def w1(event):
	global direction
	direction = 'up'
	global live
	if live == 2:
		live = 1
	global active
	active = True
	# print("w")

def a(event):
	global direction
	direction = 'left'

def s(event):
	global direction
	global live
	direction = 'down'
	if live == 1:
		live = 2
	global active
	active = True

def d1(event):
	global direction
	direction = 'right'

def enter_func(event):
	global go_up
	go_up = True

keyboard.on_press_key("w", w1)
keyboard.on_press_key("up", w1)

keyboard.on_press_key("a", a)
keyboard.on_press_key("left", a)

keyboard.on_press_key("s", s)
keyboard.on_press_key("down", s)

keyboard.on_press_key("d", d1)
keyboard.on_press_key("right", d1)

keyboard.on_press_key("enter", enter_func)


clear()

k = 0
for i in range(int(l/2-w2/2), int(l/2+w2/2)):
	l1 = 0
	for j in range(int(b/2-h2/2), int(b/2+h2/2)):
		screen.set_at((i, j), pixels2[k, l1])
		l1+=1
	k+=1

pygame.display.flip()

global active
active = True

while True:
	if go_up:
		break
	if live == 1 and active:
		# clear()

		k = int(w2/2-75)
		for i in range(int(l/2-75), int(l/2+75)):
			l1 = int(h2/2)
			for j in range(int(b/2), int(b/2+200)):
				screen.set_at((i, j), pixels2[k, l1])
				l1+=1
			k+=1

		pygame.display.flip()

		active = False

	elif live == 2 and active:
		# clear()

		k = int(w3/2-75)
		for i in range(int(l/2-75), int(l/2+75)):
			l1 = int(h3/2)
			for j in range(int(b/2), int(b/2+200)):
				screen.set_at((i, j), pixels3[k, l1])
				l1+=1
			k+=1

		pygame.display.flip()

		active = False


clear()


if live == 2:
	quit()


def simulate(snake, dir1, head):
	h=head
	if dir1 == "right":
		# head[0]+=1
		h = [h[0]+1, h[1]]
	elif dir1 == "left":
		# head[0]-=1
		h = [h[0]-1, h[1]]
	elif dir1 == "up":
		# head[1]-=1
		h = [h[0], h[1]-1]
	elif dir1 == "down":
		# head[1]+=1
		h = [h[0], h[1]+1]
	if h in snake:
		return False
	elif h[0] < 1 or h[0] > int(l/d) or h[1] < 1 or h[1] > int(b/d):
		return False
	else:
		return True

win = False

noerase=False
while True:
	# print(direction)
	cx, cy = pyautogui.position()

	# print(cx, cy)

	if cy == 1079:
		direction = "down"
	elif cy == 0:
		direction = "up"
	elif cx == 0:
		direction = "left"
	elif cx == 1919:
		direction = "right"

	if time.time() - t > time_def:
		# head_old=[int(i) for i in head]
		# ctr+=1
		t = time.time()
		
		if direction == "right":
			# head[0]+=1
			head = [head[0]+1, head[1]]
		elif direction == "left":
			# head[0]-=1
			head = [head[0]-1, head[1]]
		elif direction == "up":
			# head[1]-=1
			head = [head[0], head[1]-1]
		elif direction == "down":
			# head[1]+=1
			head = [head[0], head[1]+1]
		# print(tail, head)

		if fruit in snake:
			fill(fruit)
			fruit = [random.randint(1, int(div)), random.randint(1, int(div))]
			noerase = True

		# auto algo
		hx, hy = head[0], head[1]
		fx, fy = fruit[0], fruit[1]

		nogo = []
		while True:
			direction_backup = direction
			if not simulate(snake, direction, head):
				for i in range(1, 5):
					direction = direction_dict[i]
					if not direction in nogo:
						break
			if fx-hx>0 and not "right" in nogo:
				direction = "right"
			elif fx-hx<0 and not "left" in nogo:
				direction="left"
			elif fy-hy>0 and not "down" in nogo:
				direction="down"
			elif fy-hy<0 and not "up" in nogo:
				direction="up"
			print(simulate(snake, direction, head), snake, head, direction)
			if simulate(snake, direction, head):
				break
			else:
				nogo.append(direction)
				print(direction, direction_backup)
				direction = direction_backup
			if (len(nogo)) == 4:
				break

		print(head, fruit, direction)




		# filling stuff
		if head in snake:
			pass
			# break
		fill(head)
		snake.append(head)
		
		if not noerase:
			fill(snake[0], (0,0,0))
			snake.pop(0)
			print(snake)
		
		noerase=False



		fill(fruit, (255, 0, 0))


		pygame.display.flip()

# while True:
# 	pass

clear()
# print(l, b)
pygame.display.flip()

if not win:
	k = 0
	for i in range(int(l/2)-int(w/2), int(l/2)+int(w/2)):
		l1 = 0
		for j in range(int(b/2)-int(h/2), int(b/2)+int(h/2)):
			screen.set_at((i, j), pixels[k, l1])
			l1+=1
		k+=1
pygame.display.flip()


while True:
	pass

pygame.quit()