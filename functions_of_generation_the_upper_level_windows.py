

#Функции окон первого уровня
def choose_window_generation(current_screen):
    match current_screen:
        case "main":
            print('generate_main(current_screen = "main")')
            current_screen_inside_choose_window_generation =generate_main(current_screen = "main")
            return(current_screen_inside_choose_window_generation)
        case "menu":
            print('generate_menu(current_screen = "menu")')
            current_screen_inside_choose_window_generation = generate_menu(current_screen = "menu")
            return (current_screen_inside_choose_window_generation)
        case "about_game":
            print('generate_about_game(current_screen = "about_game")')
            current_screen_inside_choose_window_generation = generate_about_game(current_screen = "about_game")
            return (current_screen_inside_choose_window_generation)
        case "training":
            print('generate_training(current_screen = "training", player_position = player_position, last_player_position=last_player_position')
            current_screen_inside_choose_window_generation = generate_training(current_screen = "training",
                                                                               player_position = player_position,
                                                                               last_player_position=last_player_position)
            return (current_screen_inside_choose_window_generation)
        case "first_level":
            print('generate_first_level(current_screen="first_level", player_position = player_position, last_player_position=last_player_position, matrix_walls_map=matrix_walls_position_map_first_level, matrix_player_vision_map=np.ones(map_height, map_width))')
            current_screen_inside_choose_window_generation = generate_first_level(current_screen="first_level",
                                                                                  player_position = player_position,
                                                                                  last_player_position=last_player_position)
            return (current_screen_inside_choose_window_generation)
        case"exit":
            print('generate_exit(current_screen = "exit")')
            current_screen_inside_choose_window_generation = generate_exit(current_screen = "exit")
            return (current_screen_inside_choose_window_generation)
def generate_main(current_screen):
    screen.blit(background_image_to_start_screen, (0, 0))
    running_main_page = True
    while running_main_page:
        screen.blit(background_image_to_start_screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_main_page = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                menu_button.is_hovered = menu_button.position.collidepoint(pos)
                start_button.is_hovered = start_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "main":
                    if start_button.check_click(event.pos):
                        pygame.display.set_caption('Об игре')
                        current_screen="about_game"
                        running_main_page = False
                        return (current_screen)
                        #screen.blit(background_image_to_lor, (0, 0))
                    elif menu_button.check_click(event.pos):
                        current_screen = "menu"
                        running_main_page = False
                        return (current_screen)

        if current_screen == "main":
            start_button.draw(screen)
            menu_button.draw(screen)

        elif current_screen == "menu":
            back_button.draw(screen)
            settings_button.draw(screen)
            exit_button.draw(screen)
            about_button.draw(screen)
        elif current_screen == "about_game":
            font = pygame.font.Font('Mediteran.ttf', 25)

            text_introduction = ["Приветствую тебя, путник!",
                                 " ",
                                 "В многолетних воинах был истреблён народ арисшеев.",
                                 "Всё, что осталось от разумных, поклонявшихся богу Смерти - это величественные могильники, ",
                                 "простирающиеся на тысячи километров под землёй победителей.",
                                 " ",
                                 "Смельчаки. называющие себя искателями, отваживаются спускаться в скепы мертвого народа, ",
                                 " ",
                                 "а везунчики ещё и возвращаться с уникальной добычей",
                                 " ",
                                 "Подземные гробницы аритшеев полны ловушек и опасностей, "
                                 "орды нежити и мертвецов поджидают в лабиринтах темных коридоров тех, ",
                                 "кто отважится туда спуститься. ",
                                 "",
                                 "Армии воинов, даже после своей смерти хранящих покой своих владык"]
            movement = 0
            for i in text_introduction:
                text_surf_1 = font.render(i, True, WHITE)
                screen.blit(text_surf_1, (25, 400 + movement))
                movement += 20

            back_button2.draw(screen)
            next_button.draw(screen)

        pygame.display.flip()
def generate_menu(current_screen):
    pygame.display.set_caption('Меню')
    screen.blit(background_image_to_about_game, (0, 0))
    running_menu = True
    while running_menu:
        '''
        screen.blit(pygame.image.load("nemeron_gates.jpg"), (-100, 0))
        print_text("Для выхода из меню нажмите Escape", 400, 150, font_color=WHITE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                settings_button.is_hovered = settings_button.position.collidepoint(pos)
                exit_button.is_hovered = exit_button.position.collidepoint(pos)
                back_button.is_hovered = back_button.position.collidepoint(pos)
                back_button3.is_hovered = back_button3.position.collidepoint(pos)
                about_button.is_hovered = about_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "menu":

                    if back_button.check_click(event.pos):
                        current_screen = "main"
                        return (current_screen)
                    elif exit_button.check_click(event.pos):
                        current_screen = "exit"
                        return (current_screen)
                    elif back_button3.check_click(event.pos):
                        current_screen = "training"
                        return (current_screen)
                    elif settings_button.check_click(event.pos):
                        print("Открыть окно настроек")
                    elif about_button.check_click(event.pos):
                        print("Студенты группы ББСО-01-22")
                        print("Дубинин И. П.")
                        print("Концов С. А.")

        if current_screen == "menu":
            back_button.draw(screen)
            settings_button.draw(screen)
            exit_button.draw(screen)
            about_button.draw(screen)
            back_button3.draw(screen)
        elif current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            generate_main (current_screen="main")
        elif current_screen == "exit":
            pygame.display.set_caption('Выход')
            generate_exit(current_screen = "exit")
        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen = "training")

        pygame.display.flip()
def generate_about_game(current_screen):
    screen.blit(background_image_to_about_game, (0, 0))
    running_about_game = True
    while running_about_game:
        screen.blit(background_image_to_about_game, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_about_game = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
                next_button.is_hovered = next_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "about_game":
                    if back_button2.check_click(event.pos):
                        pygame.display.set_caption('Начальный экран')
                        current_screen = "main"
                        running_about_game = False
                        return (current_screen)
                    elif next_button.check_click(event.pos):
                        pygame.display.set_caption('Обучение')
                        current_screen = "training"
                        running_about_game = False
                        return (current_screen)
        if current_screen == "about_game":
            background_field = pygame.Surface((1200, 300))  # the size of your rect
            background_field.set_alpha(128)  # alpha level
            screen.blit(background_field, (0, 380))
            font = pygame.font.Font('Mediteran.ttf', 12)
            # '''
            text_introduction = ["Приветствую тебя, путник!",
                                 " ",
                                 "В многолетних воинах был истреблён народ арисшеев.",
                                 "Всё, что осталось от разумных, поклонявшихся богу Смерти - это величественные могильники, ",
                                 "простирающиеся на тысячи километров под землёй победителей.",
                                 " ",
                                 "Смельчаки. называющие себя искателями, отваживаются спускаться в скепы мертвого народа, ",
                                 " ",
                                 "а везунчики ещё и возвращаться с уникальной добычей",
                                 " ",
                                 "Подземные гробницы аритшеев полны ловушек и опасностей, "
                                 "орды нежити и мертвецов поджидают в лабиринтах темных коридоров тех, ",
                                 "кто отважится туда спуститься. ",
                                 "",
                                 "Армии воинов, даже после своей смерти хранят покой своих Владык"]
            movement = 0
            for i in text_introduction:
                text_surf_1 = font.render(i, True, WHITE)
                screen.blit(text_surf_1, (25, 400 + movement))
                movement += 20
            # '''
            back_button2.draw(screen)
            next_button.draw(screen)
        if current_screen == "main":
            start_button.draw(screen)
            menu_button.draw(screen)
        elif current_screen == "training":
            generate_training(current_screen = "training", player_position = player_position, last_player_position=last_player_position)
        pygame.display.flip()
def generate_training(current_screen="training", player_position = player_position, last_player_position=last_player_position, matrix_walls_map=matrix_walls_position_map_training_level):
    pygame.display.set_caption('Тренировка')
    screen.blit(background_image_to_training_level, (0, 0))

    (current_player_position_map,
     current_walls_position_map,
     current_player_vision_map,
     current_decor_position_map,
     current_NPC_position_map,
     matrix_player_position_map,
     matrix_walls_position_map_training_level,
     matrix_player_vision_map,
     matrix_decor_position_map,
     matrix_NPC_position_map,
     any_NPC_position,
     enemies_of_Level) = level_layers_generate(map_width=map_width,
                                                      map_height=map_height,
                                                      vis_distance=Player.vision_distance,
                                                      map_name= 'matrix_walls_map_training_level',
                                                      file='matrix_walls_map_training_level.json')

    running_training = True

    running_W_training = True
    running_S_training = False
    running_A_training = False
    running_D_training = False
    running_P_training = False
    running_F_training = False
    running_T_training = False
    running_M_training = False
    running_B_training = False
    running_I_training = False
    running_Q_training = False

    stop_training = False
    current_screen = "training"
    while running_training:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running_training = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_q]:
                pygame.display.set_caption('Квесты')
                current_screen=generate_quests("quests")
            if keys[pygame.K_m]:
                pygame.display.set_caption('Меню')
                current_screen = generate_menu(current_screen="menu")

            if keys[pygame.K_b]:
                pygame.display.set_caption('Книга заклинаний')
                current_screen=generate_magic_book(cards_compilation= all_cards,current_screen="magic_book")

            if keys[pygame.K_p]:
                pygame.display.set_caption('Пауза')
                current_screen = generate_pause(current_screen="pause")
            if keys[pygame.K_i]:
                pygame.display.set_caption('Снаряжение')
                current_screen = generate_equipment(current_screen="equipment")
            if keys[pygame.K_f]:
                Player.deal_damage(enemies_of_Level)


            (current_walls_position_map,
             current_player_map,
             current_player_vision_map,
             matrix_player_position_map,
             matrix_walls_map,
             matrix_player_vision_map) = update_major_level_layers(last_player_pos=last_player_position,
                                                                   player_position=player_position,
                                                                   matrix_walls_map=matrix_walls_map,
                                                                   matrix_player_vision_map=matrix_player_vision_map,
                                                                   vis_distance=Player.vision_distance)
            '''Отрисовка'''
            # clock.tick(60)
            screen.fill(BLACK)
            screen.blit(background_image_to_training_level, (0, 0))
            # drawing.draw_walls(sc= screen, cur_map = current_walls_position_map)
            drawing.draw_player(sc=screen,
                                player_pos=player_position,
                                cur_player_pos=current_player_map)
            drawing.draw_decor(sc=screen, cur_dec_pos_map=current_decor_position_map)
            drawing.draw_NPC(sc=screen, cur_NPC_pos_map=current_NPC_position_map)
            drawing.draw_player_vision(sc=screen, cur_player_vis_map=current_player_vision_map)
            drawing.fps_drawing(clock)

            player_on_stages=Player.movement(matrix_walls_map, matrix_decor_position_map, matrix_NPC_position_map)
            if player_on_stages:
                Player.x , Player.y = start_position_on_first_level
                player_position = start_position_on_first_level
                drawing.draw_player_vision(sc=screen, cur_player_vis_map=current_player_vision_map)
                current_screen = "first_level"
                return(current_screen)
            player_position = (Player.x, Player.y)

            background_field = pygame.Surface((400, 90))  # the size of your rect
            background_field.set_alpha(234)  # alpha level
            screen.blit(background_field, (training_text_location_x-64, training_text_location_y - 35))


            '''обучение перемещению'''

            if (running_W_training == 1):
                print_text(message="Чтобы двинуться вперёд, нажмите W", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_w]:
                    running_W_training = False
                    running_S_training = True
                    pass
            if (running_S_training == 1):
                print_text(message="Чтобы двинуться назад, нажмите S", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_s]:
                    running_S_training = False
                    running_A_training = True
                    pass
            if (running_A_training == 1):
                print_text(message="Чтобы двинуться влево, нажмите A",x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_a]:
                    running_A_training = False
                    running_D_training = True
                    pass
            if (running_D_training == 1):
                print_text(message="Чтобы двинуться вправо, нажмите D", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_d]:
                    running_D_training = False
                    #running_F_training = True #comment after pause editing
                    running_P_training = True
                    pass

            #обучение вариантам взаимодействия с окружением
            if (running_F_training == 1):
                print_text(message="F позволит нанести удар", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_f]:
                    running_F_training = False
                    running_T_training = True
                    pass
            if (running_T_training == 1):
                print_text(message="Чтобы взять предмет, нажмите  T", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_t]:
                    running_T_training = False
                    running_M_training = True
                    pass

            #обучение открытию окон
            if (running_P_training == 1):
                print_text(message="Чтобы остановить игру, нажмите P", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_p]:
                    running_P_training = False
                    running_F_training = True
            if (running_M_training == 1):
                print_text(message="Чтобы открыть меню, нажмите  M", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_m]:
                    running_M_training = False
                    running_B_training = True
                    pygame.display.set_caption('Меню')
                    current_screen = "menu"
                    pass
            if (running_B_training == 1):
                print_text(message="Чтобы открыть книгу заклинаний, нажмите  B", x=training_text_location_x-40, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_b]:
                    running_B_training = False
                    running_I_training = True
                    pygame.display.set_caption('Книга заклинаний')
                    current_screen = "magic_book"
                    pass
            if (running_I_training == 1):
                print_text(message="Чтобы открыть инвентарь, нажмите  I", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_i]:
                    running_I_training = False
                    running_Q_training = True
                    pygame.display.set_caption('Инвентарь')
                    current_screen = "equipment"
                    pass
            if (running_Q_training == 1):
                print_text(message="Чтобы открыть квесты, нажмите  Q", x=training_text_location_x, y=training_text_location_y, font_color=WHITE)
                if keys[pygame.K_q]:
                    running_Q_training = False
                    running_training = True
                    pygame.display.set_caption('Инвентарь')
                    current_screen = "equipment"
                    pass

            if (stop_training == False):
                print_text(message="Чтобы пропустить обучение, нажмите Backspace", x=training_text_location_x-60, y=training_text_location_y-25, font_color=WHITE)
                if keys[pygame.K_BACKSPACE]:
                    current_screen = "first_level"
                    Player.x, Player.y = start_position_on_first_level
                    player_position = start_position_on_first_level
                    drawing.draw_player_vision(sc=screen, cur_player_vis_map=current_player_vision_map)
                    return (current_screen)
        if current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            return(current_screen)
        health_bar.draw(screen)
        damage_bar.draw(screen)
        vision_distance_bar.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
def generate_first_level(current_screen = "first_level", player_position = player_position, last_player_position=last_player_position, matrix_walls_map=matrix_walls_position_map_first_level):
    pygame.display.set_caption('1 уровень')
    screen.blit(background_image_to_first_level, (0, 0))

    (current_player_position_map,
     current_walls_position_map,
     current_player_vision_map,
     current_decor_position_map,
     current_NPC_position_map,
     matrix_player_position_map,
     matrix_walls_position_map_first_level,
     matrix_player_vision_map,
     matrix_decor_position_map,
     matrix_NPC_position_map,
     any_NPC_position,
     enemies_of_level) = level_layers_generate(map_width=map_width,
                                                      map_height=map_height,
                                                      vis_distance=Player.vision_distance,
                                                      map_name= 'matrix_walls_map_training_level',
                                                      file='matrix_walls_map_training_level.json')

    running_first_level = True
    while running_first_level:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running_first_level = False
                current_screen = "main"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                pygame.display.set_caption('Квесты')
                current_screen = generate_quests("quests")
            if keys[pygame.K_m]:
                pygame.display.set_caption('Меню')
                current_screen = generate_menu(current_screen="menu")

            if keys[pygame.K_b]:
                pygame.display.set_caption('Книга заклинаний')
                current_screen = generate_magic_book(cards_compilation= all_cards,current_screen="magic_book")

            if keys[pygame.K_p]:
                pygame.display.set_caption('Пауза')
                current_screen = generate_pause(current_screen="pause")
            if keys[pygame.K_i]:
                pygame.display.set_caption('Снаряжение')
                current_screen = generate_equipment(current_screen="equipment")


            (current_walls_position_map,
             current_player_map,
             current_player_vision_map,
             matrix_player_position_map,
             matrix_walls_map,
             matrix_player_vision_map) = update_major_level_layers(last_player_pos=last_player_position,
                                                                   player_position=player_position,
                                                                   matrix_walls_map=matrix_walls_map,
                                                                   matrix_player_vision_map=matrix_player_vision_map,
                                                                   vis_distance=Player.vision_distance)
            '''Отрисовка'''
            # drawing.draw_walls(sc= screen, cur_map = current_walls_position_map)
            # clock.tick(60)
            screen.fill(BLACK)
            screen.blit(background_image_to_first_level, (0, 0))
            drawing.draw_player(sc=screen,
                                player_pos=player_position,
                                cur_player_pos=current_player_map)
            drawing.draw_decor(sc= screen, cur_dec_pos_map = current_decor_position_map)
            drawing.draw_NPC(sc=screen, cur_NPC_pos_map=current_NPC_position_map)
            drawing.draw_player_vision(sc=screen, cur_player_vis_map=current_player_vision_map)
            drawing.fps_drawing(clock)


            player_on_stages = Player.movement(matrix_walls_map, matrix_decor_position_map, matrix_NPC_position_map)
            if player_on_stages:
                current_screen = "first_level"
                player_on_stages = False
                (Player.x, Player.y) = default_first_level_position
                return(current_screen)
            player_position = (Player.x, Player.y)


        if current_screen == "main":
            pygame.display.set_caption('Начальный экран')
            return(current_screen)
        health_bar.draw(screen)
        damage_bar.draw(screen)
        vision_distance_bar.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
def generate_exit(current_screen):
    screen.fill(BLACK)
    pygame.display.set_caption('Выход')
    screen.blit(background_image_to_exit_game, (0, 0))
    running_exit = True
    while running_exit:
        screen.blit(background_image_to_exit_game, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_exit = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_exit_button.is_hovered = back_exit_button.position.collidepoint(pos)
                real_exit_button.is_hovered = real_exit_button.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "exit":
                    if back_exit_button.check_click(event.pos):
                        current_screen = "menu"
                        return(current_screen)
                    elif real_exit_button.check_click(event.pos):
                        pygame.quit()
        if current_screen == "exit":
            pygame.display.set_caption('Подтверждение выхода')
            print_text('Вы уверены, что хотите выйти из игры?', 50, 200, font_color=WHITE, font_type= pygame.font.Font('AlgerianBasD [Rus by me] Regular.otf', 32))
            back_exit_button.draw(screen)
            real_exit_button.draw(screen)
        elif current_screen == "menu":
            generate_menu(current_screen="menu")
        pygame.display.flip()