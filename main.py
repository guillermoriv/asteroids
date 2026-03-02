import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        # render probably here
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # 60FPS -> convert to seconds from milliseconds

    pygame.quit()


if __name__ == "__main__":
    main()
