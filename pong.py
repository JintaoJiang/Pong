from ball import *
from paddle import *
import math
import random 

epoch = 100000
alpha = 0.5
gamma = 0.9
epsilon = 0.1
action_list = ['down', 'no', 'up']
unit_grid = 1 / 12

class pong():
	

	def __init__(self):
		self.ball = ball(0.5, 0.5, 0.005, 0.003)
		self.paddle = paddle(0.4)
		self.state = (0.5, 0.5, 0.005, 0.003, 0.4) #initial state
		self.q = {}

	def discretizeAndUpdate(self):
		ball_x = math.floor(self.ball.x / unit_grid)
		ball_y = math.floor(self.ball.y / unit_grid)
		v_x = -1
		v_y = -1
		if self.ball.v_x > 0:
			v_x = 1
		if self.ball.v_y > -0.0015 and self.ball.v_y < 0.0015:
			v_y = 0
		if self.ball.v_y > 0.0015:
			v_y = 1
		paddle_y = math.floor(self.paddle.y / (1 - self.paddle.height) / unit_grid)
		#self.state = (ball_x, ball_y, v_x, v_y, paddle_y)
		return (ball_x, ball_y, v_x, v_y, paddle_y)

	def move(self):
		#prepare
		self.state = self.discretizeAndUpdate()
		#choose action
		action = self.chooseAction()
		#get successor state
		nextState = self.state ############################
		#TDupdate
		self.TDupdate(action, nextState)
		#perform action
		self.ball.move()
		self.paddle.move(action)

	#Qlearning algorithm
	def TDupdate(self, action, nextState):
		state = (self.state, action)
		maxQ = max([self.q.get((nextState, act), 0) for act in action_list])
		self.q[state] = self.q.get(state, 0) + alpha * (self.reward() + gamma * maxQ - self.q.get(state, 0))

	def chooseAction(self):
		a = random.random()
		#exploit
		if(a < epsilon):
			best_action = 'down'
			best_value = 0
			for action in action_list:
				value = self.q.get((self.state, action), 0)
				if value > best_value:
					best_action = action
					best_value = value
			return best_action
		#explore
		else:
			return random.choice(action_list)

	#reward is based on continuous world not the discrete world, this may be problematic as the Q matrix may fluctuate
	def reward(self):
		if self.checkHit():
			return 1
		elif self.checkPass():
			return -1
		else:
			return 0

	def checkHit(self):
		if self.ball.x >= 1 and self.ball.y >= self.paddle.y and self.ball.y <= self.paddle.y + self.paddle.height:
			self.ball.x = 2 - self.ball.x
			self.ball.v_x = -self.ball.v_x 
			return True
		else:
			return False

	def checkPass(self):
		if self.ball.x > 1 and (self.ball.y < self.paddle.y or self.ball.y > self.paddle.y + self.paddle.height):
			self.restart()
			return True
		else:
			return False

	def restart(self):
		self.state = (0.5, 0.5, 0.005, 0.003, 0.4)





