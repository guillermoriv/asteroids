import pygame
from typing import List
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS


class Player(CircleShape):
    rotation: int

    def __init__(self, x: int, y: int):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> List[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
