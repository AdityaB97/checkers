# checkers
A simple implementation of a game of checkers.

To play, first ensure that you have Python 3.6 installed. If you have conda, one way to do this is by running

```conda env create -f environment.yml```

The code does not use any external packages.

In order to play the game, run

```python play_game.py```

You will see the current state of the board, as well a prompt where you can alternately enter actions for each player. Please enter actions in the following format:

Each action should be written as a sequence of tuples, separated by spaces. Each of the tuples should contain 2 positions, separated by a comma but no space. Each position should consist of 2 characters, where the first is a lowercase letter between 'a' and 'h' indicating the column, and the second is an integer between '1' and '9' indicating the row. I have used the row and column labelling from the image provided in the spec.
