

# создание кнопок
#начальный экран
start_button = Button("Начать игру", (260, 260))
start_button.width, start_button.height = 400 ,100
start_button.position = pygame.Rect((80, 140), (start_button.width, start_button.height))
menu_button = Button("Меню", (80, 220))
menu_button.width, menu_button.height = 200 ,80
menu_button.position = pygame.Rect((180, 260), (menu_button.width, menu_button.height))

#об игре
back_button2 = Button("Назад", (50, 700))
next_button = Button("Далее", (950, 700))

#меню
back_button = Button("На начальный экран", (40, 700))
back_button.font = pygame.font.Font('Mediteran.ttf', 12)
about_button = Button("Об авторах", (260, 700))
back_button3 = Button("К игре", (500, 700))
settings_button = Button("Настройки", (720, 700))
exit_button = Button("Выйти", (940, 700))

#выход
back_exit_button = Button("Остаться", (60, 350))
back_exit_button.font = pygame.font.Font('AlgerianBasD [Rus by me] Regular.otf', 26)
real_exit_button = Button("Выйти", (560, 350))
real_exit_button.font = pygame.font.Font('AlgerianBasD [Rus by me] Regular.otf', 26)

#пауза
magic_book_button   = Button("Книга заклинаний", (500, 200))
magic_book_button.font = pygame.font.Font('Mediteran.ttf', 16)
quests_button       = Button("Квесты", (500, 300))
equipment_button    = Button("Инвентарь", (500, 400))
exit_button_2       = Button("Выйти в главное меню", (500, 700))
exit_button_2.font = pygame.font.Font('Mediteran.ttf', 12)
back_to_level_button = Button("Продолжить игру", (500, 500))
back_to_level_button.font = pygame.font.Font('Mediteran.ttf', 16)

#книга заклинаний
activate_card_button_1 = Button("Активировать", (40, 240))
activate_card_button_1.width , activate_card_button_1.height = 200, 40
activate_card_button_2 = Button("Активировать", (270, 240))
activate_card_button_2.width , activate_card_button_2.height = 200, 40
activate_card_button_3 = Button("Активировать", (500, 240))
activate_card_button_3.width , activate_card_button_3.height = 200, 40
activate_card_button_4 = Button("Активировать", (730, 240))
activate_card_button_4.width , activate_card_button_4.height = 200, 40
activate_card_button_5 = Button("Активировать", (960, 240))
activate_card_button_5.width , activate_card_button_5.height = 200, 40
activate_card_button_6 = Button("Активировать", (40, 620))
activate_card_button_6.width , activate_card_button_6.height = 200, 40
activate_card_button_7 = Button("Активировать", (270, 620))
activate_card_button_7.width , activate_card_button_7.height = 200, 40
activate_card_button_8 = Button("Активировать", (500, 620))
activate_card_button_8.width , activate_card_button_8.height = 200, 40
activate_card_button_9 = Button("Активировать", (730, 620))
activate_card_button_9.width , activate_card_button_9.height = 200, 40
activate_card_button_10 = Button("Активировать", (960, 620))
activate_card_button_10.width , activate_card_button_10.height = 200, 40