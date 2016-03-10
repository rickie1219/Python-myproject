#-*- coding:utf-8 -*-

# https://docs.python.org/3/library/curses.html#curses.start_color
# https://docs.python.org/3/howto/curses.html
import curses
import os
class  Ui:
	"""docstring for  """
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.clear()

		#self.screen.timeout(100)
		curses.cbreak()
		curses.noecho()
		self.screen.keypad(1)

		curses.start_color()
		curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
		curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
		curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
		curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
		curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)

		size = os.get_terminal_size()
		self.x = max(size[0],20)
		self.y = max(size[1],15)
		self.startcol = int(float(self.x) / 2 - 8)
		self.width_index_dict = {0:2,1:9,2:16,3:23}
		self.height_index_dict = {0:3,1:5,2:7,3:9}

	# draw table
	def draw_table(self):
		self.screen.addstr(1,self.startcol+12,"2048             score:00", curses.color_pair(5))
		self.screen.addstr(2,self.startcol,"+------+------+------+------+")
		self.screen.addstr(3,self.startcol,"|      |      |      |      |")
		self.screen.addstr(4,self.startcol,"+------+------+------+------+")
		self.screen.addstr(5,self.startcol,"|      |      |      |      |")
		self.screen.addstr(6,self.startcol,"+------+------+------+------+")
		self.screen.addstr(7,self.startcol,"|      |      |      |      |")
		self.screen.addstr(8,self.startcol,"+------+------+------+------+")
		self.screen.addstr(9,self.startcol,"|      |      |      |      |")
		self.screen.addstr(10,self.startcol,"+------+------+------+------+")
		self.screen.addstr(11,self.startcol,"(W)Up (S)Down (A)Left (D)Right")
		self.screen.addstr(12,self.startcol,"     (R)Restart (Q)Exit")
		self.screen.refresh()

	
	def draw_num(self,field,score):
		self.draw_table()
		for height_index in range(4):
			for width_index in range(4):
				self.screen.addstr(self.height_index_dict[height_index], self.startcol + self.width_index_dict[width_index],"    ")
				if field[height_index][width_index] != 0:
					self.screen.addstr(self.height_index_dict[height_index], self.startcol + self.width_index_dict[width_index],str(field[height_index][width_index]),curses.color_pair(1))
		self.screen.addstr(1,self.startcol+35,str(score), curses.color_pair(5))
		self.screen.move(13, 1)
		self.screen.refresh()
	def draw_info(self,state):
		if state == 'Win':
			self.screen.addstr(6,self.startcol+32,"YOU WIN!")
		if state == "Gameover":
			self.screen.addstr(6,self.startcol+32,"GAME OVER!")
		self.screen.refresh()
	
	def get_user_action(self):
		letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
		actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
		actions_dict = dict(zip(letter_codes, actions * 2))
		char = "N"
		while char not in actions_dict:
			char = self.screen.getch()
		return actions_dict[char]





	



	



		