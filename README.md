# Conway's Game of Life

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

The Game of Life is a cellular automaton developed by the British mathematician John Horton Conway in 1970. The game was created in order to reproduce, through simple rules, alterations and changes in groups of living beings, having applications in several areas of science.

It starts with a certain configuration of pieces, distributed throughout the cells. In each cell there is either a piece or there is no piece. This rule is valid at the beginning and throughout the game. Then Conway's "genetic laws" are applied, which determine the pattern of births, deaths, and survivals.

The defined rules are applied to each new "generation"; thus, from an image on a two-dimensional board defined by the player, changes are perceived that are often unexpected and beautiful with each new generation, ranging from fixed to chaotic patterns.

## Rules
1. Any living cell with fewer than two live neighbors dies of loneliness.
2. Any living cell with more than three live neighbors dies of overpopulation.
3. Any cell with exactly three live neighbors becomes a live cell.
4. Any cell with two live neighbors remains in the same state for the next generation.

The dependencies to run this script are:

1. Numpy
2. Pygame
