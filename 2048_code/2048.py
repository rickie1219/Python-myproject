from ui import Ui
from gamefield import Gamefiled
import curses

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

ui = Ui()
gamefield = Gamefiled()


def init():
	# 重置游戏
	gamefield.reset()
	ui.draw_num(gamefield.field, gamefield.score)
	return 'Game'

def not_game_win():
	#画出gameover or win
	ui.draw_info('Win')
	action = ui.get_user_action()
	if action == 'Restart':
		return 'Init'
	if action == 'Exit':
		return 'Exit'

def not_game_gameover():
	#画出gameover or win
	ui.draw_info('Gameover')
	action = ui.get_user_action()
	if action == 'Restart':
		return 'Init'
	if action == 'Exit':
		return 'Exit'

def game():
	ui.draw_num(gamefield.field,gamefield.score)	
	action = ui.get_user_action()

	if action == 'Restart':
		return 'Init'
	if action == 'Exit':
		return 'Exit'
	if gamefield.update_field(action):
		if gamefield.is_win():
			return 'Win'
		if gamefield.is_gameover():
			return 'Gameover'
	return 'Game'

state_actions = {
            'Init': init,
            'Win': not_game_win,
            'Gameover': not_game_gameover,
            'Game': game
        }

state = 'Init'

while state != 'Exit':
	state = state_actions[state]()

curses.endwin()














