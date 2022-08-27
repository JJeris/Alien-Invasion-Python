import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main class for the games assets and behavior."""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        # Settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion v1.0")
        self.ship = Ship(self)
        
        # Set the background color.
        # self.bg_color = (230,230,230)
    
    def run_game(self):
        """Start the games main loop."""
        while True:
            self._check_events()  
            self.ship.update()          
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._key_up_events(event)
            
             # elif event.key == pygame.K_w:
                #     # Move the ship up.
                #     self.ship.rect.y -= 10
                # elif event.key == pygame.K_s:
                #     # Move the ship down.
                #     self.ship.rect.y += 10
            
    def _key_down_events(self, event):
        """Respond to keypasses"""
        if event.key == pygame.K_d:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            # Stop moving the ship to the right.
            self.ship.moving_left = True
          
    def _key_up_events(self, event):
        """Respond to keypasses"""
        if event.key == pygame.K_d:
            # Move the ship to the left.
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            # Stop moving the ship to the left.
            self.ship.moving_left = False
               
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass thorugh the loop.
            # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        # ship rect placed on the correct position on the screen.
        self.ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
if __name__=='__main__':
    # Make a game insance, and run the game.
    ai = AlienInvasion()
    ai.run_game()