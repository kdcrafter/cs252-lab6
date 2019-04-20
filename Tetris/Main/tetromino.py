import random
import enum

Z = [
    [[1,1,0],[0,1,1],[0,0,0]],
	[[0,0,1],[0,1,1],[0,1,0]],
	[[0,0,0],[1,1,0],[0,1,1]],
	[[0,1,0],[1,1,0],[1,0,0]]
]

S = [[[0,1,1],[1,1,0],[0,0,0]],
	[[0,1,0],[0,1,1],[0,0,1]],
	[[0,0,0],[0,1,1],[1,1,0]],
	[[1,0,0],[1,1,0],[0,1,0]]]

J = [[[0,1,0],[0,1,0],[1,1,0]],
	[[1,0,0],[1,1,1],[0,0,0]],
	[[0,1,1],[0,1,0],[0,1,0]],
	[[0,0,0],[1,1,1],[0,0,1]]]

T = [[[0,0,0],[1,1,1],[0,1,0]],
	[[0,1,0],[1,1,0],[0,1,0]],
	[[0,1,0],[1,1,1],[0,0,0]],
	[[0,1,0],[0,1,1],[0,1,0]]]

L = [[[0,1,0],[0,1,0],[0,1,1]],
	[[0,0,0],[1,1,1],[1,0,0]],
	[[0,1,1],[0,0,1],[0,0,1]],
	[[0,0,0],[0,0,1],[1,1,1]]]

I = [[[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],
	[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
	[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],
	[[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]]]

O = [[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]]

PIECES = [Z, S, J, T, L, I, O]

class Piece():
    def __init__(self):
        self.tetromino = PIECES[random.randint(0, len(PIECES)-1)]
        self.orientation = 0
        self.x = 4
        self.y = 0

    #def rotate(self):
    #    self.orientation = (self.orientation + 1) % len(self.tetromino)
