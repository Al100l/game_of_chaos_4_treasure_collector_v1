import pygame
import json
def save_map_array_to_file(map_name, matrix_map, file):
    a = {}
    a.update({map_name: matrix_map})
    level_jsn = json.dumps(a)
    with open(file, 'w') as f:
        json.dump(level_jsn, f)
def load_map_array_from_file(map_name, file):
    f = open(file)
    buffer = json.load(f)
    map_dictionary = json.loads(buffer)
    matrix_map = map_dictionary[map_name]
    return(matrix_map)
