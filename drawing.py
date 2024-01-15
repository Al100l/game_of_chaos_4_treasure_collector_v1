


class Drawing:
    def __init__(self, sc, sc_map):

        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.Font('Mediteran.ttf', 36)
    def fps_drawing(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, YELLOW)
        self.sc.blit(render, FPS_POSITION)


    def draw_walls(self,sc, cur_map):
        for x, y in cur_map:
            pygame.draw.rect(sc, RED, (x, y, TILE, TILE), TILE)

    def draw_player(self, sc, player_pos, cur_player_pos):
        elf_image1 = pygame.image.load('elf sprites/tile020.png')
        x, y = player_pos
        for x, y in cur_player_pos:
            screen.blit(elf_image1, (x-2, y-6) )
            #pygame.draw.circle(sc, GREEN, (x+TILE//2, y+TILE//2), TILE//2)
            #pygame.draw.circle(sc, BLACK, (x+TILE//2, y+TILE//2), TILE//2, 2)
    def draw_player_vision(self, sc, cur_player_vis_map):
        for x, y in cur_player_vis_map:
            pygame.draw.rect(sc,(BLACK), (x, y, TILE, TILE), TILE)
    def draw_NPC (self, sc, cur_NPC_pos_map):
        for x, y in cur_NPC_pos_map:
            pygame.draw.circle(sc, RED, (x+TILE//2, y+TILE//2), TILE//2)
            pygame.draw.circle(sc, BLACK, (x+TILE//2, y+TILE//2), TILE//2, 2)
    def draw_decor(self,sc,cur_dec_pos_map):
        for x, y in cur_dec_pos_map:
            pygame.draw.circle(sc, BLUE, (x + TILE // 2, y + TILE // 2), TILE // 2)
            pygame.draw.circle(sc, BLACK, (x + TILE // 2, y + TILE // 2), TILE // 2, 2)
    def draw_rect(self, screen):
        # Отрисовка фона статус бара
        pygame.draw.rect(screen, color=(220,220,220),rect=(0,0,1200,800))