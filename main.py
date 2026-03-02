import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # 60FPS -> convert to seconds from milliseconds

    pygame.quit()


if __name__ == "__main__":
    main()
