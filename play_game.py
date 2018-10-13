from checkers import CheckersGame

if __name__ == "__main__":
	checkers_game = CheckersGame()
	print('Welcome to this game of checkers!.')
	while True:
		try:
			print('\nHere is the current board:')
			checkers_game.print_board()
			print(f"\nPlease input player {checkers_game.turn}'s next actions")
			input_from_user = input()
			actions = [(action[:2], action[3:]) for action in input_from_user.split()]
			checkers_game.take_turn(actions)
		except KeyboardInterrupt:
			print('\nYou have terminated the game\n')
			break
		except AssertionError as e:
			print(e)