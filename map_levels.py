from game_settings import *

text_map_test_level = [
    "WWWWWWWWWWWWW",
    "W...........W",
    "W.WWWWWWWWW.W",
    "W.W.......W.W",
    "W.WWWWWWW.W.W",
    "W.........W.W",
    "WWWWWWWWWWWWW"
    ]

text_map_first_level = [
        "WWWWWWWWWWWWWWWWWWWW",
        "W..................W",
        "W.........WWWW.W...W",
        "W....W............WW",
        "W....W....WWWWW...WW",
        "W....W..W..W..W...WW",
        "W....W........W...WW",
        "W.......W..W..W..WWW",
        "W....W....W...W...WW",
        "W....WWW..W...W...WW",
        "W.........W........W",
        "WWWWWWWWWWWWWWWWWWWW"
    ]

text_map_second_level = [
        "WWWWWWWWWWWWWWWWWWWW",
        "W..................W",
        "WWWWWW....WWWW.W...W",
        "W....W............WW",
        "W....W....WWWWW...WW",
        "W....W..W..W..W...WW",
        "W....W........W...WW",
        "W.......W..W..W..WWW",
        "W....W....W...W...WW",
        "W....WWW..W...W...WW",
        "W.........W........W",
        "WWWWWWWWWWWWWWWWWWWW"
    ]

#TODO
'''
Сделать карты оставшихся уровней
'''
#


world_map = set()
for j, row in enumerate(text_map_test_level):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*TILE, j*TILE))
        
