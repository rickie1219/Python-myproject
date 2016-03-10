#-*- coding:utf-8 -*-
from ui import Ui
from random import randrange, choice

#对列表的变化
def transpose(field):
	#return [list(row) for row in zip(*field)]
	return list(map(list, zip(*field)))

def invert(field):
	return [row[::-1] for row in field]

class Gamefiled:
	"""docstring for Gamefiled"""
	def __init__(self):
		self.field = [[0 for i in range(4)] for j in range(4)]
		self.score = 0
		self.win_value = 2048
		#self.ui = Ui()
		self.reset()

	def reset(self):
		self.score = 0
		self.field = [[0 for i in range(4)] for j in range(4)]
		self.spawn()
		self.spawn()
		#self.ui.draw_num(self.field,self.score)

	def spawn(self):
		new_element = 4 if randrange(100) > 89 else 2
		(i,j) = choice([(i,j) for i in range(4) for j in range(4) if self.field[i][j] == 0])
		self.field[i][j] = new_element
		

	def update_field(self,direction):
		def move_row_left(row):
			def tighten(row):
				new_row = [i for i in row if i != 0]
				new_row += [0 for  i in range(len(row) - len(new_row))]
				return new_row
			def merge(row):
				pair = False
				new_row = []
				for i in range(len(row)):
					if pair:
						new_row.append(2 * row[i])
						self.score += 2 * row[i]
						pair = False
					else:
						if i + 1 < len(row) and row[i] == row[i+1]:
							pair = True
							new_row.append(0)
						else:
							new_row.append(row[i])
				assert len(new_row) == len(row)
				return new_row
			return tighten(merge(tighten(row)))
		'''
		def move_left(field):
			return [move_row_left(row) for row in self.field]
		def move_right(field):
			return invert(move_left(invert(field)))
		def move_up(field):
			transpose(move_left(transpose(field)))
		def move_down(field):
			transpose(move_right(transpose(field)))



		if direction == 'Left':
			if self.move_is_possible(direction):
				self.field = move_left(self.field)
				self.spawn()
				return True
			else:
				return False

		if direction == 'Right':
			if self.move_is_possible(direction):
				self.field = move_right(self.field)
				self.spawn()
				return True
			else:
				return False

		if direction == 'Up':
			if self.move_is_possible(direction):
				self.field = move_up(self.field)
				self.spawn()
				return True
			else:
				return False

		if direction == 'Down':
			if self.move_is_possible(direction):
				self.field = move_down(self.field)
				self.spawn()
				return True
			else:
				return False
		self.ui.draw_num(self.field,self.score)
		'''
		moves = {}
		moves['Left']  = lambda field: [move_row_left(row) for row in field]
		moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
		moves['Up']    = lambda field: transpose(moves['Left'](transpose(field)))
		moves['Down']  = lambda field: transpose(moves['Right'](transpose(field)))
		
		if direction in moves:
			if self.move_is_possible(direction):
				self.field = moves[direction](self.field)
				self.spawn()
				return True
			else:
				return False


	#判断是否可以继续移动
	def move_is_possible(self,direction):
		def row_is_left_movable(row):
			def change(i):
				if row[i] == 0 and row[i+1] != 0:
					return True
				if row[i] !=0 and row[i+1] == row[i]:
					return True
				return False
			return any(change(i) for i in range(len(row) - 1))

		check = {}
		check['Left']  = lambda field: any(row_is_left_movable(row) for row in field)

		check['Right'] = lambda field: check['Left'](invert(field))

		check['Up']    = lambda field: check['Left'](transpose(field))

		check['Down']  = lambda field: check['Right'](transpose(field))

		if direction in check:
			return check[direction](self.field)
		else:
 			return False

	def is_win(self):
		return any(any(i >= self.win_value for i in row) for row in self.field)

	def is_gameover(self):
		directions = ['Left','Rigth','Up','Down']
		return not any(self.move_is_possible(direction) for direction in directions)\











		
		