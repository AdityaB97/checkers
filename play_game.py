from checkers import CheckersGame

if __name__ == "__main__":
	checkers_game = CheckersGame()
	print('Welcome to this game of checkers!.')
	while True:
		try:
			print('Here is the current board:')
			checkers_game.print_board()
			print(f"Please input player {checkers_game.turn}'s next actions")
			# print(input().split())
			# break
			actions = [(action[1:3], action[4:-1]) for action in input().split()]
			print(actions)
			checkers_game.take_turn(actions)
		except KeyboardInterrupt:
			print('You have terminated the game')
			break