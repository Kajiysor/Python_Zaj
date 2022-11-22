# **CONNECT4 WITH "AI" - PYTHON PROJECT**

## _Author: **Jonasz Gawlik**_

## **Project info:**

The point of this project was to make the connect4 game with an AI opponent.

The game itself was built using pygame.

The AI is utilizing the minimax algorithm to predict the best move it can make.

## **Connect Four**

Connect Four is a two-player connection board game, in which the players choose a color and then take turns dropping colored tokens into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens.

If you want to read more about the Connect Four game, you can look it up [here](https://en.wikipedia.org/wiki/Connect_Four)

## **More about minimax:**

Minimax is a decision rule for minimizing the possible loss for a worst case scenario.

In this particular game, minimax is used to calculate the best possible move for the AI player.  
It is given a depth paramater which tells it how many moves ahead it should take into account.  
The algorithm plays out that many moves ahead for the human and AI players and then determines which move will be the best for the AI considering all the moves that can be made before.   
To do that, in this case, it uses the predetermined weights for moves that are hardcoded in the algorithm itself.

These are just simple explanations of what is roughly going on.  
If you want to read more about minimax, feel free to visit this [wiki page](https://en.wikipedia.org/wiki/Minimax)

## **Running the game:**

### Required:

 - Python > 3.0
 - pygame
 - numpy

### Launching the game itself:

Run the game with python from the shell: `python3 connect4.py`

You could also import the game module inside your own code: `from connect4 import Connect4`

From there you can create the `Connect4` object inside you code.   
It takes three parameters when creating: `ai_depth (required), row_count (optional), column_count (optional)`  

`ai_depth` is responsible for the amount of moves, that dictate how far ahead should the minimax algorithm look

`row_count` and `column_count` are responsible for the dimensions of the Connect4 game board. By default these are set to be 6x7 which are the dimensions of real Connect Four board game.
However, you can change these if you want to experiment with the game 😊
