import numpy as np


#Функции взаимодействия с уже созданнными слоями слоями
def update_major_level_layers(last_player_pos, player_position, matrix_walls_map, matrix_player_vision_map, vis_distance):

    # player_pos
    # слой с отображением позиции игрока
    matrix_player_pos_map = np.zeros((map_height, map_width))
    matrix_player_pos_map[last_player_pos] = 0
    matrix_player_pos_map[player_position] = 1
    last_player_pos = player_position
    # print(matrix_player_pos_map, '\n')
    # создаём стек используемых для прорисовки точек
    cur_player_pos_on_map = matrix_player_pos_map
    cur_player_map = set()
    for j, row in enumerate(cur_player_pos_on_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_map.add((i * TILE, j * TILE))

    # wal
    # слой с изображением стен
    # создаём стек используемых для прорисовки квадратиков стен точек
    matrix_wal_map = matrix_walls_map
    cur_matrix_wal_map = matrix_wal_map
    cur_map = set()
    for j, row in enumerate(cur_matrix_wal_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_map.add((i * TILE, j * TILE))

    #vis
    # слой с отображением зрения игрока
    #используем основную матрицу
    matrix_player_vis_map = matrix_player_vision_map

    matrix_player_vis_map[(player_position[0] - vis_distance):(player_position[0]+vis_distance+1),
                          (player_position[1] - vis_distance): (player_position[1] + vis_distance+1):] = 0
    matrix_player_vis_map[(player_position[0] - 1):(player_position[0] + 1 + 1),
    (player_position[1] - 1): (player_position[1] + 1 + 1):] = 0
    matrix_player_vis_map[(player_position[0] - 2):(player_position[0] + 2 + 1),
    (player_position[1] - 2): (player_position[1] + 2 + 1):] = 0
    #print(matrix_player_vis_map)
    last_player_pos = player_position
    #print(matrix_player_vis_map, '\n')
    # создаём стек используемых для прорисовки точек
    cur_pl_vis_map = matrix_player_vis_map
    cur_player_vis_map = set()
    for j, row in enumerate(cur_pl_vis_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_vis_map.add((i * TILE, j * TILE))
    return (cur_map, cur_player_map, cur_player_vis_map, matrix_player_pos_map, matrix_wal_map, matrix_player_vis_map)

def update_NPC_level_layer(matrix_NPC_pos_map, dead_NPC_positions):
    for dead_NPC_position in dead_NPC_positions:
        matrix_NPC_pos_map[dead_NPC_position] = 0

    # создаём стек используемых для прорисовки позиции NPC точек

    cur_NPC_pos_on_map = matrix_NPC_pos_map
    cur_NPC_pos_map = set()
    set_NPC_coordinates = set()
    for j, row in enumerate(cur_NPC_pos_on_map):
        for i, number in enumerate(row):
            if number == 8:
                cur_NPC_pos_map.add((i * TILE, j * TILE))
                set_NPC_coordinates.add((i, j))
    return(cur_NPC_pos_map, matrix_NPC_pos_map, set_NPC_coordinates)