#Функции инициализации
def level_layers_initialization (map_width, map_height, vis_distance, map_name, file):

    #player_pos
    #слой с отображением позиции игрока
    matrix_player_pos_map = np.zeros((map_height,map_width))
    matrix_player_pos_map[player_position] = 1
    last_player_position = player_position
    #print(matrix_player_pos_map, '\n')
    ''''''
    # создаём стек используемых для прорисовки позиции игрока точек
    cur_player_pos_on_map = matrix_player_pos_map
    cur_player_pos_map = set()
    for j, row in enumerate(cur_player_pos_on_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_pos_map.add((i * TILE, j * TILE))

    #wal
    #слой с изображением стен
    #matrix_wal_map = np.ones((map_height,map_width))
    #внешняяя стена вокруг
    #matrix_wal_map[1:-1,1:-1:] = 0
    #внутренние стены
    #matrix_wal_map[5:-5,5:-5:] = 1
    matrix_wal_map = load_map_array_from_file(map_name, file)
    #print(matrix_wal_map, '\n')
    ''''''
    #создаём стек используемых для прорисовки квадратиков стен точек
    cur_matrix_wal_map = matrix_wal_map
    cur_wal_map = set()
    for j, row in enumerate(cur_matrix_wal_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_wal_map.add((i*TILE, j*TILE))

    #vis
    #создаём слой видимости игроком
    # слой с отображением позиции игрока
    matrix_player_vis_map = np.ones((map_height, map_width))

    matrix_player_vis_map[(player_position[0] - vis_distance):(player_position[0] + vis_distance+1),
                            (player_position[1] - vis_distance): (player_position[1] + vis_distance+1):] = 0
    matrix_player_vis_map[(player_position[0] - 1):(player_position[0] + 1 + 1),
    (player_position[1] - 1): (player_position[1] + 1 + 1):] = 0
    matrix_player_vis_map[(player_position[0] - 2):(player_position[0] + 2 + 1),
    (player_position[1] - 2): (player_position[1] + 2 + 1):] = 0
    last_player_position = player_position
    # print(matrix_player_vis_map, '\n')
    # создаём стек используемых для прорисовки зрения игрока точек
    cur_pl_vis_map = matrix_player_vis_map
    cur_player_vis_map = set()
    for j, row in enumerate(cur_pl_vis_map):
        for i, number in enumerate(row):
            if number == 1:
                cur_player_vis_map.add((i * TILE, j * TILE))

    # dec
    # создаём наполнение/декор
    matrix_dec_pos_map = np.zeros((map_height, map_width))
    matrix_dec_pos_map[16, 17] = 4
    ''''''
    # создаём стек используемых для прорисовки позиции декора точек
    cur_dec_pos_on_map = matrix_dec_pos_map
    cur_dec_pos_map = set()
    for j, row in enumerate(cur_dec_pos_on_map):
        for i, number in enumerate(row):
            if number == 4:
                cur_dec_pos_map.add((i * TILE, j * TILE))

    #NPC
    # создаём слой расположения всех NPC уровня и экземпляр класса NPC на каждую точку создаём NPC
    matrix_NPC_pos_map = np.zeros((map_height, map_width))
    matrix_NPC_pos_map[13, 17] = 8
    #load_from_file_NPC_map
    enemy_1 = NPC_initialization(NPC_position=(17, 17), NPC_type=8)
    enemies_of_level = [enemy_1]  # Список экземпляров класса Student
    enemies_of_level = sorted(enemies_of_level, key=operator.attrgetter('name'))  # Сортировка по атрибуту name
    for enemy in enemies_of_level:
        print("enemy.healthpoints = ",enemy.healthpoints)

    for i in range(len (matrix_NPC_pos_map)):
        for j in range(len( matrix_NPC_pos_map[i])):
            if matrix_NPC_pos_map[i][j] !=0:
                enemies_of_level.append(NPC_initialization(NPC_position = (i, j), NPC_type = matrix_NPC_pos_map[i][j] ))
                print("enemy_of_level", NPC_initialization(NPC_position = (i, j), NPC_type = matrix_NPC_pos_map[i][j] ))

    # создаём стек используемых для прорисовки позиции NPC точек

    cur_NPC_pos_on_map = matrix_NPC_pos_map
    cur_NPC_pos_map = set()
    set_NPC_coordinates = set()
    for j, row in enumerate(cur_NPC_pos_on_map):
        for i, number in enumerate(row):
            if number == 8:
                cur_NPC_pos_map.add((i * TILE, j * TILE))
                set_NPC_coordinates.add((i , j))



    return(cur_player_pos_map,
           cur_wal_map,
           cur_player_vis_map,
           cur_dec_pos_map,
           cur_NPC_pos_map,

           matrix_player_pos_map,
           matrix_wal_map,
           matrix_player_vis_map,
           matrix_dec_pos_map,
           matrix_NPC_pos_map,

           set_NPC_coordinates,
           enemies_of_level)
def cards_initialization():
    mythryl_sword=Cards(                card_name ='Мифриловый меч',                discription="",     number = 1      ,image=""       ,card_form="")
    fog_lion=Cards(                     card_name ="Туманный лев",                  discription="",     number = 2      ,image=""       ,card_form="")
    grakula=Cards(                      card_name="Гракула",                        discription="",     number = 3      ,image=""       ,card_form="")
    sprigan=Cards(                      card_name="Сприган. мастер ловушек",        discription="",     number = 4      ,image=""       ,card_form="")
    crystal_mole=Cards(                 card_name="Кристаллический крот",           discription="",     number = 5      ,image=""       ,card_form="")
    kayrun_hammer=Cards(                card_name="Молот Кайруна",                  discription="",     number = 6      ,image=""       ,card_form="")
    wind_of_ice_debris=Cards(           card_name="Ветер ледяных осколков",         discription="",     number = 7      ,image=""       ,card_form="")
    breath_of_dragons_ancestors=Cards(  card_name="Дыхание прародителей драконов",  discription="",     number = 8      ,image=""       ,card_form="")
    giant_eye=Cards(                    card_name="Глаз исполина",                  discription="",     number = 9      ,image=""       ,card_form="")
    armor_of_rapid_strikes=Cards(       card_name="Доспех стремительных ударов",    discription="",     number =10      ,image=""       ,card_form="")
    '''
    =Cards(card_name="", discription="")
    '''
    all_cards = [   mythryl_sword,
                    fog_lion,
                    grakula,
                    sprigan,
                    crystal_mole,
                    kayrun_hammer,
                    wind_of_ice_debris,
                    breath_of_dragons_ancestors,
                    giant_eye,
                    armor_of_rapid_strikes]
    '''
    for i in all_cards:
        i.print_card()
    '''
    return(all_cards)
def status_bar_initialization():
    # Создаем отбражение здоровья
    health_bar = StatusBar(20, 20, 50, 20, 0, 50, current_value=Player.healthpoints, text="HP",
                           color=STATUS_BAR_HP_BACKGROUND_COLOR)
    # Создаем отбражение атаки
    damage_bar = StatusBar(20, 40, 50, 20, 0, 30, current_value=Player.damage, text="Attack",
                           color=STATUS_BAR_DAMAGE_BACKGROUND_COLOR)
    # Создаем отбражение дальности зрения
    vision_distance_bar = StatusBar(20, 60, 50, 20, 0, 10, current_value=Player.vision_distance, text="vision",
                                    color=STATUS_BAR_VISION_BACKGROUND_COLOR)
    return(health_bar, damage_bar, vision_distance_bar)
def hero_initialization():
    Player = Hero(name=players_nick,
                  player_position=player_position,
                  healthpoints=25,
                  damage=5,
                  armor=0,
                  attack_range=1,
                  movement_speed=1,
                  vision_distance=3)
    return(Player)

def NPC_initialization(NPC_position = (17,17), NPC_type=8):
    if NPC_type == 8:
        NPC_of_level = NPC(name="Пепельник",
                           NPC_position = NPC_position,
                           healthpoints=30,
                           damage=4,
                           armor=2,
                           attack_range=3,
                           movement_speed=1,
                           vision_distance=3)
        return (NPC_of_level)
def decor_initialization ():
    pass