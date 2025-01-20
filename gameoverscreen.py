import pygame

class GameOverScreen:

    def __init__(self, screen, current_score):
        self.screen = screen
        self.current_score = current_score
        self.font_over = pygame.font.Font(None, 48)
        self.font_small =pygame.font.Font(None, 36)
        self.restart_triggered = False # Initialize the restart flag

    def update(self):
        keys =pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.restart_triggered = True # Restart wanted

    def render(self):
        """Render the Game Over screen"""
        self.screen.fill((0, 0, 0))

        # "Game Over!"
        game_over_text = self.font_over.render("Game Over!", True, (255, 255, 255))
        self.screen.blit(
            game_over_text,
            (
                (self.screen.get_width() - game_over_text.get_width()) // 2,
                self.screen.get_height() // 4,
            ),
        )
        # "Final Score"
        score_text =self.font_small.render(f"Your Score: {self.current_score}", True, (255, 255, 255))
        self.screen.blit(
            score_text,
            (
                (self.screen.get_width() - score_text.get_width()) // 2,
                self.screen.get_height() // 2,
            ),
        )
        # "Restart"
        restart_text = self.font_small.render("Press 'r' to Restart", True, (255, 255, 255))
        self.screen.blit(
            restart_text,
            (
                (self.screen.get_width() - restart_text.get_width()) // 2,
                self.screen.get_height() - self.screen.get_height() // 4,
            ),
        )

        pygame.display.flip()
        
