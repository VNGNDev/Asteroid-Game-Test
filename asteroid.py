import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame

from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        random_grade = random.uniform(20.0, 50.0)
        new_ast_vel_1 = self.velocity.rotate(random_grade)
        new_ast_vel_2 = self.velocity.rotate(-random_grade)
        new_ast_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position[0], self.position[1], new_ast_rad)
        new_ast_2 = Asteroid(self.position[0], self.position[1], new_ast_rad)
        new_ast_1.velocity = new_ast_vel_1 * 1.2
        new_ast_2.velocity = new_ast_vel_2 * 1.2
