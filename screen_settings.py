
import game_settings
#screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

screen_map = pygame.Surface((SCREEN_WIDTH // MAP_SCALE, SCREEN_HEIGHT//MAP_SCALE))

pygame.display.set_caption('Начальный экран')

pygame.display.set_icon(pygame.image.load('icon.jpg'))

current_screen ="main"