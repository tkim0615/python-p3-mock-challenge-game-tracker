#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game = Game("Skribbl.io")
    player = Player("Nick")
    player2= Player('t')
    player3=Player('B')
    av= Result(player, game, 5000)
    bv= Result(player, game, 4999)
    c= Result(player, game, 5000)
    d= Result(player, game, 4999)
    e=Result(player2, game, 1000)
    f= Result(player2, game, 1000)
    
    





    ipdb.set_trace()
