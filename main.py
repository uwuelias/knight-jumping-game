import pygame
from sys import exit

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
score = 0
gravity = 1

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font("assets/press2start.ttf", 15)

ground_surface = pygame.Surface((900, 150))
ground_surface.fill("#268b07")
sprite_surface = pygame.transform.scale(pygame.image.load("assets/sprite.png").convert_alpha(), (90, 120))
sprite_rect = sprite_surface.get_rect(bottomleft = (55, 350))
opp_surface = pygame.transform.scale(pygame.image.load("assets/opp.png"), (100, 100))
opp_rect = opp_surface.get_rect(bottomright = (900, 350))
score_surface = font.render(f"score:{score}", False, "Black")
sprite_velocity = 0
jumping = False
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and sprite_rect.bottom == 350:
                sprite_velocity = -20
                jumping = True

    if not paused:
        opp_rect.x -= 10
        if opp_rect.right <= 0: opp_rect.left = 900

        sprite_velocity += gravity
        sprite_rect.y += sprite_velocity

        if sprite_rect.bottom >= 350:
            sprite_rect.bottom = 350
            sprite_velocity = 0
        if jumping and sprite_rect.right > opp_rect.left:
            score += 1
            jumping = False

        window.fill((135, 206, 250))
        window.blit(ground_surface, (0, 350))
        score_surface = font.render(f"score:{score}", False, "Black")
        window.blit(score_surface, (10, 10))
        window.blit(sprite_surface, sprite_rect)
        window.blit(opp_surface, opp_rect)

        if sprite_rect.colliderect(opp_rect):
            font = pygame.font.Font("assets/press2start.ttf", 30)
            ending_surface = font.render("Game Over!", False, "Black")
            ending_rect = ending_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            font = pygame.font.Font("assets/press2start.ttf", 15)
            ending_score_surface = font.render(f"score: {score}", False, "Black")
            ending_score_rect = ending_score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
            window.blit(ending_surface, ending_rect)
            window.blit(ending_score_surface, ending_score_rect)
            pygame.display.update()
            paused = True  

        pygame.display.update()
        clock.tick(60)    