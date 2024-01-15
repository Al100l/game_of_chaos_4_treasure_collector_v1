# Функции всплывающих окон
def generate_pause(current_screen):
    pygame.display.set_caption('Пауза')
    screen.blit(background_image_to_pause, (0, 0))
    pygame.display.flip()
    paused = True
    while paused:
        screen.blit(background_image_to_pause, (0, 0))
        # print_text("также продолжить игру можно зажав  ESCAPE", 450, 600, font_color=WHITE, font_type= pygame.font.Font('AlgerianBasD [Rus by me] Regular.otf', 18))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                paused = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                magic_book_button.is_hovered = magic_book_button.position.collidepoint(pos)
                quests_button.is_hovered = quests_button.position.collidepoint(pos)
                equipment_button.is_hovered = equipment_button.position.collidepoint(pos)
                back_to_level_button.is_hovered = back_to_level_button.position.collidepoint(pos)
                exit_button_2.is_hovered = exit_button_2.position.collidepoint(pos)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "pause":
                    if magic_book_button.check_click(event.pos):
                        current_screen = generate_magic_book(cards_compilation=all_cards, current_screen="magic_book")
                    if quests_button.check_click(event.pos):
                        current_screen = generate_quests(current_screen="quests")

                    if equipment_button.check_click(event.pos):
                        current_screen = generate_equipment(current_screen="equipment")
                    if exit_button_2.check_click(event.pos):
                        current_screen = "main"
                        return (current_screen)
                    elif back_to_level_button.check_click(event.pos):
                        current_screen = "training"
                        return (current_screen)

        if current_screen == "pause":
            magic_book_button.draw(screen)
            quests_button.draw(screen)
            equipment_button.draw(screen)
            back_to_level_button.draw(screen)

            exit_button_2.draw(screen)
        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen="training")
        elif current_screen == "magic_book":
            pygame.display.set_caption('Книга заклинаний')
            generate_magic_book(cards_compilation=all_cards, current_screen="magic_book")

        elif current_screen == "equipment":
            pygame.display.set_caption('Инвентарь')
            generate_equipment(current_screen="equipment")
        pygame.display.flip()

    pygame.display.set_caption('First level')
    pygame.display.update()
def generate_magic_book(cards_compilation, current_screen):
    pygame.display.set_caption('Книга заклинаний')
    current_screen = "magic_book"
    spells_book_generating = True
    while spells_book_generating:
        screen.blit(background_image_to_magic_book, (-100, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spells_book_generating = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                activate_card_button_1.is_hovered = activate_card_button_1.position.collidepoint(pos)
                activate_card_button_2.is_hovered = activate_card_button_2.position.collidepoint(pos)
                activate_card_button_3.is_hovered = activate_card_button_3.position.collidepoint(pos)
                activate_card_button_4.is_hovered = activate_card_button_4.position.collidepoint(pos)
                activate_card_button_5.is_hovered = activate_card_button_5.position.collidepoint(pos)
                activate_card_button_6.is_hovered = activate_card_button_6.position.collidepoint(pos)
                activate_card_button_7.is_hovered = activate_card_button_7.position.collidepoint(pos)
                activate_card_button_8.is_hovered = activate_card_button_8.position.collidepoint(pos)
                activate_card_button_9.is_hovered = activate_card_button_9.position.collidepoint(pos)
                activate_card_button_10.is_hovered = activate_card_button_10.position.collidepoint(pos)
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "magic_book":
                    if activate_card_button_1.check_click(event.pos):
                        print("1")
                    if activate_card_button_2.check_click(event.pos):
                        print("2")
                    if activate_card_button_3.check_click(event.pos):
                        print("3")
                    if activate_card_button_4.check_click(event.pos):
                        print("4")
                    if activate_card_button_5.check_click(event.pos):
                        print("5")
                    if activate_card_button_6.check_click(event.pos):
                        print("6")
                    if activate_card_button_7.check_click(event.pos):
                        print("7")
                    if activate_card_button_8.check_click(event.pos):
                        print("8")
                    if activate_card_button_9.check_click(event.pos):
                        print("9")
                    if activate_card_button_10.check_click(event.pos):
                        print("10")
                    elif back_button2.check_click(event.pos):
                        current_screen = "pause"
                        return (current_screen)
        if current_screen == "magic_book":
            activate_card_button_1.draw(screen)
            activate_card_button_2.draw(screen)
            activate_card_button_3.draw(screen)
            activate_card_button_4.draw(screen)
            activate_card_button_5.draw(screen)
            activate_card_button_6.draw(screen)
            activate_card_button_7.draw(screen)
            activate_card_button_8.draw(screen)
            activate_card_button_9.draw(screen)
            activate_card_button_10.draw(screen)
            back_button2.draw(screen)

        elif current_screen == "training":
            pygame.display.set_caption('Обучение')
            generate_training(current_screen="training")
            break
        pygame.display.flip()

    # for i in cards_compilation:
    #    if i.active == 1:
def generate_equipment(current_screen):
    screen.blit(background_image_to_equipment, (0, 0))
    equipment_oppened = True
    while equipment_oppened:
        screen.blit(background_image_to_equipment, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                equipment_oppened = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "equipment":
                    if back_button2.check_click(event.pos):
                        current_screen = "pause"
                        return (current_screen)
        if current_screen == "equipment":
            back_button2.draw(screen)

        pygame.display.flip()
def generate_quests(current_screen):
    screen.blit(background_image_to_quests, (0, 0))
    quests_table = True
    while quests_table:
        screen.blit(background_image_to_quests, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quests_table = False
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                back_button2.is_hovered = back_button2.position.collidepoint(pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "quests":
                    if back_button2.check_click(event.pos):
                        current_screen = "pause"
                        return (current_screen)
        if current_screen == "quests":
            back_button2.draw(screen)

        pygame.display.flip()