#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


g1 = Game('starcraft')
g2 = Game('WOW')
g3 = Game('LOL')

p1 = Player('TK')
p2 = Player('JS')
p3 = Player('YJ')

r1 = Result(p1, g1, 200)
r2 = Result(p2,g2, 456)
r3 = Result(p3, g1, 233)
r4=Result(p2, g2, 1)
r5 = Result(p2, g1, 1111)



ipdb.set_trace()
