import pygame
from pygame.sprite import Sprite

class AdvFighter(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(AdvFighter, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('images/adv-fighter-left.JPEG')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien right or left."""
        
        self.y += self.ai_settings.adv_fighter_speed_factor
        self.x += self.ai_settings.adv_fighter_speed_factor
        self.rect.y = self.y
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)
