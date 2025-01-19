import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other_shape):
        """
        Checks for collision between two circular shapes.
        Args:
            other_shape: Another CircleShape object to check collision with
        Returns:
            bool: True if shapes are colliding, False otherwise
        """
        return pygame.math.Vector2.distance_to(self.position, other_shape.position) <= (self.radius + other_shape.radius)

