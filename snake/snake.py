import os
os.system("pip install pygame")
import random
import pyautogui
import time
import pygame

pygame.init()

time_def = 0.4

l = 500
b = 500

div = 10

d=l/div

screen = pygame.display.set_mode((l, b))


def fill(pixel, color=(0, 0, 255)):
	pixel[0] = pixel[0]%div
	pixel[1] = pixel[1]%div
	if pixel[0] == 0:
		pixel[0] = 10
	if pixel[1] == 0:
		pixel[1] = 10
	for i in range(int(d*(pixel[0]-1)), int(d*pixel[0])):
		for j in range(int(d*(pixel[1]-1)), int(d*pixel[1])):
			screen.set_at((i, j), color)


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

fruit = [random.randint(1, 10), random.randint(1, 10)]


noerase=False
while True:
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
			fruit = [random.randint(1, 10), random.randint(1, 10)]
			noerase = True

		



		if head in snake:
			break
		fill(head)
		snake.append(head)
		
		if not noerase:
			fill(snake[0], (0,0,0))
			snake.pop(0)
			print(snake)
		
		noerase=False



		fill(fruit, (255, 0, 0))


		pygame.display.flip()



pygame.quit()