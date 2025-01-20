import pygame

class Score:
    def __init__(self):
        self.high_score = 0
        self.current_score = 0
        
    def add_points(self, points):
        """Add points to the current score."""
        self.current_score += points

    def reset_score(self):
        """Reset the current score and upadte high score if necessary."""
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0

    def display_score(self, screen):
        """Render and display the score on the game screen.""" #got this from Boot at boot.dev / how to work with the stuff that pygame provides
        font = pygame.font.Font(None, 36) # Default font, size 36
        font_hight = font.get_height() # Height of the font in pxels / because i want to calculate the height dynamically

        score_text_current = font.render(f"Score: {self.current_score}", True, (255, 255, 255))
        score_text_high = font.render(f"High Score: {self.high_score}", True, (255, 255, 255))

        screen.blit(score_text_high, (10, 10)) # Top-left corner of the screen / blit ~draw
        screen.blit(score_text_current, (10, 10 + font_hight + 5)) # Add 5 pxels for spacing
