# Simulator-of-simple-reflex-agent-for-the-vacuum-cleaner-environment
This code is only for basic functionality understanding and is not an optimal solution. 

Aim: To implement a simulator of simple reflex agent for the vacuum cleaner
environment, run the simulator for all the possible initial dirt configurations and agent
locations and show the performance score for each configuration. Also, display the
state-space search graph.

Design details :
● The language used is python.
● There are 2 cells, each of which can be clean or dirty, hence 8 different configuration
scenarios. The performance score increases by 1 when the bot cleans a cell.
● A implies the left cell, and B implies the right cell. Additionally, in
this code, position 0 implies left cell or A, and position 1 implies right cell or B.
● For states, 0 implies clean and 1 implies dirty. For example, If the current state is 0 0,
this implies that both cells are clean. If the state is 0 1, A is clean and B is dirty, etc.
● For the purpose of drawing the state space graph, the convention followed is as
follows -
○ A0B0PosA - Current state is 0 0 , i.e. left cell (A) is clean and right cell (B) is
clean, current position is A (left cell)
○ A1B0PosB - Current state is 1 0, i.e. left cell (A) is dirty and right cell (B) is
clean, current position is B (right cell)
● Once the bot is in a cell it checks if it is clean. If not it sucks the dirt. if yes, then using
the random function, a new position is generated and it moves to the new position.
If it already is in a new position, the action is to stay in the cell.
● The lifetime of the cleaner is at 1000 timesteps. State space graph is displayed at the end of every scenario.

