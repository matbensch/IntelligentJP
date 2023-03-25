# Useful tool for setting up your base locations: https://www.kevinbai.design/terminal-map-maker
# More community tools available at: https://terminal.c1games.com/rules#Download

import gamelib
import math
import json
import sys

from .navigation import ShortestPathFinder
from .util import send_command, debug_write
from .unit import GameUnit
from .game_map import GameMap

class Defense:
    def __init__(self,config,left_end=9,width=1):
        self.config = config
        global WALL, SUPPORT, TURRET, REMOVE, UPGRADE
        WALL = config["unitInformation"][0]["shorthand"]
        SUPPORT = config["unitInformation"][1]["shorthand"]
        TURRET = config["unitInformation"][2]["shorthand"]
        REMOVE = config["unitInformation"][6]["shorthand"]
        UPGRADE = config["unitInformation"][7]["shorthand"]

        right_start = left_end+width+1

        # PHASE 1: LEFT/RIGHT WALLS
        self.BASE_TEMPLATE = [([i,13], WALL) for i in range(left_end+1)] + [([i,13], WALL) for i in range(left_end+width+1,28)]
        
        # PHASE 2: 2-LAYER TURRETS
        self.BASE_TEMPLATE += [
            ([left_end,12], TURRET),
            ([right_start,12], TURRET),
            ([left_end,11], TURRET),
            ([right_start,11], TURRET)
        ]

        

        # PHASE 4: SUPPORT LAYER
        self.BASE_TEMPLATE += [([i,12], WALL) for i in range(left_end-1)] + [([i,12], WALL) for i in range(right_start+2,28)]

        # PHASE 4: SUPPORT LAYER
        self.BASE_TEMPLATE += [
            ([left_end-1,12], SUPPORT),
            ([right_start+1,12], SUPPORT)
        ]

        self.BASE_TEMPLATE += [
            #([2,11], TURRET),
            #([25,11], TURRET),
            ([8,8], TURRET),
            ([19,8], TURRET)
        ]

        # PHASE 5: 1ST LAYER TURRET UPGRADE
        self.BASE_TEMPLATE += [
            ([left_end,12], UPGRADE),
            ([right_start,12], UPGRADE)
        ]

        # ???
        

        # PHASE 4: 3RD LAYER TURRETS
        self.BASE_TEMPLATE += [
            ([left_end,10], TURRET),
            ([right_start,10], TURRET)
        ]

        

        # PHASE 6: SUPPORT UPGRADE
        self.BASE_TEMPLATE += [
            ([left_end-1,12],UPGRADE),
            ([right_start+1,12],UPGRADE)
        ]