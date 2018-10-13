# checkers
A simple implementation of a game of checkers.

To play, first ensure that you have Python 3.6 installed. If you have conda, one way to do this is by running

```conda env create -f environment.yml```

The code does not use any external packages.

In order to play the game, run

```python play_game.py```

You will see the current state of the board, as well a prompt where you can alternately enter actions for each player. Please enter actions in the following format:

Each action should be written as a sequence of pairs, separated by spaces. Each of the pairs should contain 2 positions, separated by a comma but no space. Each position should consist of 2 characters, where the first is a lowercase letter between 'a' and 'h' indicating the column, and the second is an integer between '1' and '9' indicating the row. I have used the row and column labelling from the image provided in the spec.

The convention used is that Player 0 is the red player, and Player 1 is the white player.

So, for example, if you want to move Player 0's piece from b7 to b, you would type:

```b7,b6```

And if you wanted to jump Player 0's piece from c7 to a5, and then from a5 to c3 (assuming these moves are legal), you would type:

```c7,a5 a5,c3```
