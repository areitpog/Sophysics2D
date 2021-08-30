from Sophysics2D import *
import pygame
pygame.init()
# This is a dummy application to test the functionality of Sophysics2D
display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sophysics 2D")

rm = RenderManager(display)
env = DefaultEnvironment(components=(rm, ))

ball_transform = Transform(pygame.Vector2(0, 0))
ball1 = get_circle_body(0.5, (255, 0, 0), 1, (ball_transform,))

# ball2 = CircleObject(radius=0.5, color=(0, 255, 0), layer=1)

border = get_border_object(4, -4, -7.5, 7.5, layer=3)

env.attach_object(ball1)
env.attach_object(border)
# env.attach_object(ball2)
env.start()
running = True
clock = pygame.time.Clock()

while(running):
    clock.tick(60)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    env.advance()
    env.render()
    ball_transform.position.x += 0.01
    pygame.display.update()
