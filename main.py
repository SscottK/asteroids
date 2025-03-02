# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateables, drawables)
    Player.containers = (updateables, drawables)
    AsteroidField.containers = (updateables)
    Shot.containers = {shots, updateables, drawables}
    player = Player(x, y)
    asteroidfield = AsteroidField()



    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        
        dt = clock.tick(60) / 1000
        


        updateables.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                running = False
                break
            

            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()


        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        
            

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()