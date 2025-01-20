import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from gameoverscreen import GameOverScreen

def main():
    pygame.init()
    game_over = False
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()
    score = Score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if not game_over:
            screen.fill((0, 0, 0))
            score.display_score(screen)

            for sprite in updatable:
                sprite.update(dt)

            for asteroid in asteroids:
                if asteroid.collision(player):
                    game_over = True # Stop game updates
                    break
                for shot in shots:
                    if shot.collision(asteroid):
                        asteroid.split()
                        shot.kill()
                        score.add_points(1)               
                    
            for sprite in drawable:
                sprite.draw(screen)


            pygame.display.flip()
            dt = clock.tick(60) / 1000
        
        if game_over:
            current_score = score.current_score
            game_over_screen = GameOverScreen(screen, current_score)
            game_over_screen.update() # Handles input Logic in the GameOverScreen
            game_over_screen.render() # Draws GameOverScreen

            # Check if restart was triggerd in the GameOverScreen
            if game_over_screen.restart_triggered:
                # Reset Game
                game_over = False
                score.reset_score()
                

                # Clear all sprite groups (to ensure no lingering sprites)
                updatable.empty()
                drawable.empty()
                asteroids.empty()
                shots.empty()

                updatable.add(player)
                drawable.add(player)
                
                player.reset()
                asteroid_field = AsteroidField() # Reinitialize AsteroidField to regenerate the asteroids
                game_over_screen.restart_triggered = False # Reset the flag
                


if __name__ == "__main__":
    main()
