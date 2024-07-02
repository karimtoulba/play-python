########################################################
### Code: Coding Challenge
### Author: Karim Toulba
### Date: 02/07/2024
########################################################


# understanding the board as a 2d list = [[0,0,0,0], [0,0,0,0]]
board = [[]]
m = len(board) # Find rows length of the bord
n = len(board[0]) # Find columns length of the board

# Check if tiles are connected to the origin.
######################################################
# A tile is connected to the origin (the tile in the upper left corner) if:
# it has the same color as the origin 
# AND 
# there is a connected path to the origin (consisting only of tiles of this color).
######################################################
def is_connected(board, tile, m, n, x, y):

    old_positions = set() # creating an empty set for old tiles that are not connected
    queue = [tile] # initialize queue list
    origin_color = board[0][0] # origin color

    while queue:
# define x and y as old-tile and new-tile
        x = queue.pop(0)
        y = queue.pop(0)
        
# defining old_positions as the moves that were not connected: adding failed moves to this list
# if connected, return True
        if (x, y) in old_positions or board[x][y] != origin_color:
            continue
        
        old_positions.add((x, y))

        if x == 0 and y == 0:
            return True
    
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                queue.append((nx, ny))

    return False

######################################################
# tiles are changed to the chosen new color
# The game proceeds until all tiles of the board have the same color
######################################################
def flood_fill(board, origin, new_color, x, y):

    old_positions = set() # creating an empty set for old tiles that are not connected
    old_color = board[origin[0]][origin[1]] # old color tile
    queue = [origin] # starting queue

    while queue:
    # define x and y as old-tile and new-tile
        x = queue.pop(0)
        y = queue.pop(0)

        # if statement to fill flood the correct tile according to the move
        if board[x][y] != old_color:
        # skip the loop if tile is not equal to the old color
            continue
        else:
        # fill flood the tile with the new color
            board[x][y] = new_color
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                queue.append((nx, ny))

        # adding old positions to the set (old_positions)
        old_positions.add((x, y))

    return board

######################################################
# A player does a move by choosing one of the m colors.  
# After the choice is made, all tiles that are connected to the origin are changed to the chosen color.
# The game proceeds until all tiles of the board have the same color.
# Each tile is connected to up to four adjacent tiles
######################################################

def play_game(board, m, n):

    colors = set(color for row in board for color in row) #colors set -immutable
    moves = [] #empty list for moves

    while len(set(row[0] for row in board)) != 1:
        
        # using guess and check to define variables for max_connected and best_color
        max_connected_tiles = 0
        
        # iterate throug the colors set
        for color in colors:
        # guess and check connected tiles equal 0
            connected_tiles = 0

        # Nested for loops to iterate through rows/columns (m, n) 
            for i in range(m):
                for j in range(n):
                    if board[i][j] == color and is_connected(board, (i, j)):
                        connected_tiles += 1
            
        # Connected tiles equal or greater than maximum connected tiles? then, max_connected = connected
            if connected_tiles >= max_connected_tiles:
                max_connected_tiles = connected_tiles
        
        #apply flood_fill function
        board = flood_fill(board, (0, 0), color)

        #add picked color to the moves list
        moves.append(color)

    return moves

######################################################
# Testing Classes (Assisted with ChatGPT)
######################################################

import unittest
from collections import Counter

class TestFloodFill(unittest.TestCase):

    def test_flood_fill(self):
        # board equal to the following values
        board = [
            ['R', 'G', 'B'],
            ['R', 'R', 'B'],
            ['R', 'R', 'B']
        ]
        # generate the new board based on flood fill function
        new_board = flood_fill(board, (0, 0), 'G')
        self.assertEqual(new_board, [
            ['G', 'G', 'B'],
            ['G', 'G', 'B'],
            ['G', 'G', 'B']
        ])
    

    def test_is_connected(self):
        board = [
            ['R', 'G', 'B'],
            ['R', 'R', 'B'],
            ['R', 'R', 'B']
        ]
        self.assertTrue(is_connected(board, (0, 0)))
        self.assertTrue(is_connected(board, (1, 0)))
        self.assertTrue(is_connected(board, (1, 1)))
        self.assertFalse(is_connected(board, (0, 1)))
        self.assertFalse(is_connected(board, (0, 2)))
    

    def test_play_game(self):
        board = [
            ['R', 'G', 'B'],
            ['R', 'R', 'B'],
            ['R', 'R', 'B']
        ]
        moves = play_game(board)
        self.assertEqual(moves, ['G'])
        self.assertEqual([[color] * 3 for color in 'GGG'], board)

        board = [
            ['R', 'G', 'B', 'Y'],
            ['R', 'R', 'B', 'Y'],
            ['R', 'R', 'B', 'Y'],
            ['R', 'R', 'B', 'Y']
        ]
        moves = play_game(board)
        self.assertEqual(moves, ['R', 'Y'])
        self.assertEqual([[color] * 4 for color in 'RRRR'], board)



if __name__ == '__main__':
    unittest.main()
