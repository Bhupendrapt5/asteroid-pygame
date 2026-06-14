import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
       pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x = self.position.x
        y = self.position.y

        as_1 = Asteroid(x, y, new_radius)
        as_2 = Asteroid(x, y, new_radius)

        angle = random.uniform(20, 50)
        as_1.velocity = self.velocity.rotate(angle) * 1.2
        as_2.velocity = self.velocity.rotate(-angle) * 1.2


            