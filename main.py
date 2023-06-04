import pygame
import sys
import time
from functions import *
from CONSTANCE import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    
    animate = False

    mod_n = 720
    #x_n = 361

    i = 0

    active = True
    while active:

        screen.fill((BLACK))
        x_n = Nice_multipliers(mod_n)

        x = x_n[i]
      
        Show_numbers(screen, mod_n, x)
        #print(len(x_n))


        if animate == True:
            Draw_TimesTable(screen, mod_n, x, RED) 
             
            if i < len(x_n)-1: 
                time.sleep(1.5)
                i += 1
            else:
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
        

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    animate = True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
