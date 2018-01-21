class paddle():
	def __init__(self, y):
		self.x = 0.99 #for drawing purpose
		self.y = y
		self.height = 0.2

	def move(self, action):
		if action == 'down':
			self.y += 0.04
			if self.y > 1 - self.height:
				self.y = 1 - self.height
		if action == 'up':
			self.y -= 0.04
			if self.y < 0:
				self.y = 0

