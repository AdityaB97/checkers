from checkers import CheckersGame

if __name__ == "__main__":
	checkers_game = CheckersGame()
	print('Welcome to this game of checkers!.')
	while True:
		try:
			print('\nHere is the current board:')
			checkers_game.print_board()
			print(f"\nPlease input player {checkers_game.current_player}'s next actions")
			while True:
				try:
					input_from_user = input()
					actions = [(action[:2], action[3:]) for action in input_from_user.split()]
					checkers_game.take_turn(actions)
					break
				except AssertionError as e:
					print(e)
		except KeyboardInterrupt:
			print('\nYou have terminated the game\n')
			break