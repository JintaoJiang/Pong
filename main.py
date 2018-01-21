import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from pong import *

#Macros
WIDTH = 500


pong = pong()
mode = 'training'


def draw(c):
	c.draw_circle((pong.ball.x * WIDTH, pong.ball.y * WIDTH), 10, 1, 'White', 'Green')
	c.draw_line((pong.paddle.x * WIDTH, pong.paddle.y * WIDTH), (pong.paddle.x * WIDTH, (pong.paddle.y + pong.paddle.height) * WIDTH), 5, 'Green')
	
	if mode == 'training':
		pong.move()


if __name__ == '__main__':
	frame = simplegui.create_frame('Pong', WIDTH, WIDTH)
	frame.set_draw_handler(draw)
	frame.start()

	#Game Loop
	#while True:
