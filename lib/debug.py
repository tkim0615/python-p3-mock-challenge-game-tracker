#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


chess = Game('Chess')
go = Game('Go')
tetris = Game('Tetris')
soccer = Game('Soccer')

tyler = Player('tyler')
jeff = Player('jeff')
minor = Player('minor')
messi = Player('messi')

r1 = Result(tyler, soccer, 100)
r2 = Result(messi, soccer, 4999)
r3 = Result(jeff, tetris, 140)
r4 = Result(minor, go, 20)
r5 = Result(tyler, go, 222)
r6 = Result(messi, chess, 233)
r7 = Result(tyler, soccer, 200)
r8 = Result(messi, soccer, 2000)
r9 = Result(tyler, soccer, 500)
r10 = Result(messi, soccer, 100)

print(soccer.average_score(tyler))
ipdb.set_trace()
