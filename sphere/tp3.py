import threading
from threading import Thread
from pynput import keyboard
import copy
import time
import os


class simul:
	def __init__(self):
		self.width = 100
		self.height = self.width*2

		self.radius = 100**(1/2)
		self.centerPos = [self.width/2, self.height/2]
		self.centerVel = [0.0, 0.0]
		self.centerAcc = [9.80, 0.0]
		self.e = 0.0
		self.template = [[' ' for j in range(0, self.height)] for i in range(0, self.width)]

	def jump(self, key):
		if key == keyboard.Key.space:
			with self.lock:
				self.centerVel = [-20.0, self.centerVel[1]]
		elif key == keyboard.Key.d:
			with self.lock:
				self.centerVel = [self.centerVel[0], 20.0]
		elif key == keyboard.Key.a:
			with self.lock:
				self.centerVel = [self.centerVel[0], -20.0]

	def run(self):
		with keyboard.Listener(on_press=self.jump) as s:
			s.join()

	def start(self):
		thread = Thread(target=self.run)
		self.lock = threading.Lock()
		thread.start()

		while True:
			temp = copy.deepcopy(self.template)
			t = 0.1
			self.centerPos[0] = self.centerPos[0] + self.centerVel[0]*t
			self.centerPos[1] = self.centerPos[1] + self.centerVel[1]*t

			self.centerVel[0] = self.centerVel[0] + self.centerAcc[0]*t
			self.centerVel[1] = self.centerVel[1] + self.centerAcc[1]*t

			self.centerAcc[1] = (-1)*self.centerVel[1]/10

			if self.centerPos[0] > self.width-self.radius:
				self.centerPos[0] = self.width-self.radius
				self.centerVel[0] = int((-1)*self.centerVel[0]*self.e)
			if self.centerPos[1] > self.height-self.radius:
				self.centerPos[1] = self.height-self.radius
				self.centerVel[1] = int((-1)*self.centerVel[1]*self.e)
			if self.centerPos[1] < 0+self.radius:
				self.centerPos[1] = 0 + self.radius
				self.centerVel[1] = int((-1)*self.centerVel[1]*self.e)

			for i in range(0, self.width):
				for j in range(0, self.height):
					# if i == width/2 or j == height/2:
					# 	printable += ' '
					if 4*(i-self.centerPos[0])**2 + (j-self.centerPos[1])**2 <= self.radius**2:
						temp[i][j] = '*'
					if i == 0 or i == self.width-1 or j == 0 or j == self.height-1:
						temp[i][j] = '+'

			os.system('cls')
			print('\n'.join([''.join(i) for i in temp]))

		thread.join()

	# os.system('cls')

	# if os.path.exists('lol.txt'):
	# 	with open('lol.txt', 'r+') as f:
	# 		print(f.read())
	# 		f.seek(0)
	# 		print(f.readline())
	# 		f.seek(0)
	# 		print(f.readlines())
	# 		f.seek(0)
	# 		f.write('lol\nline2\nnvm\n\n')

	# print('\n')

if __name__ == '__main__':
	sim = simul()
	sim.start()