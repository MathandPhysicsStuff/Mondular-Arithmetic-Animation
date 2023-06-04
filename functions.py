import pygame
import time
from math import sin, cos, pi
from CONSTANCE import *


def Draw_TimesTable(screen, mod_n, x_n, color):

    points = (2*pi) / mod_n

    pygame.draw.line(screen, color, (WIDTH, 0), (WIDTH, HEIGHT), 4)
    pygame.draw.line(screen, color, (0, 0), (0, HEIGHT), 4)
    pygame.draw.line(screen, color, (0, HEIGHT), (WIDTH, HEIGHT), 4)
    pygame.draw.line(screen, color, (0, 0), (WIDTH, 0), 4)

    for i in range(mod_n+1):
        
        theta_0 = (i * points)
        theta_1 = ((i*x_n) % mod_n) * points

        P_0 = (X_CENTER + RADIUS*cos(theta_0), Y_CENTER + RADIUS*sin(theta_0))
        P_1 = (X_CENTER + RADIUS*cos(theta_1), Y_CENTER + RADIUS*sin(theta_1))
        
        pygame.draw.line(screen, color, P_0, P_1, 1)

        if x_n < 361:
            pygame.display.update()
        else:
            pass


def Show_numbers(screen, mod_n, x_n):
    
    FONT_SERIF = pygame.font.SysFont("serif",16)
    
    show_x_n = FONT_SERIF.render("Times Table: "+str(round(x_n, 4)), 1, LIGHT_GRAY)
    show_mod_n = FONT_SERIF.render("mod: "+str(mod_n), 1, LIGHT_GRAY)

    screen.set_clip((0,0), (160, 106))
    screen.fill(BLACK)

    screen.blit(show_x_n, (20, 20))
    screen.blit(show_mod_n, (20, 40))

    
    screen.set_clip(None)

def Powers(screen, mod_n, x_n, color):
    
    pass


def Negative_TimesTable(screen, mod_n, x_n, color):

    points = (2*pi) / mod_n

    pygame.draw.line(screen, color, (WIDTH, 0), (WIDTH, HEIGHT), 4)
    pygame.draw.line(screen, color, (0, 0), (0, HEIGHT), 4)
    pygame.draw.line(screen, color, (0, HEIGHT), (WIDTH, HEIGHT), 4)
    pygame.draw.line(screen, color, (0, 0), (WIDTH, 0), 4)

    for i in range(mod_n):

        theta_0 = (i * points)
        theta_1 = -(((i*(x_n)) % mod_n) * points)

        P_0 = (X_CENTER + RADIUS*cos(theta_0), Y_CENTER + RADIUS*sin(theta_0))
        P_1 = (X_CENTER + RADIUS*cos(theta_1), Y_CENTER + RADIUS*sin(theta_1))
        
        pygame.draw.line(screen, color, P_0, P_1, 1) 



def Nice_multipliers(mod_n):

    multipliers = [] 

    for i in range(mod_n//2, 1, -1):

       if mod_n % i == 0:

           multipliers.append((mod_n//i)-1)
           #multipliers.append(mod_n//i)
           multipliers.append((mod_n//i)+1)

    dict.fromkeys(multipliers)
    multipliers = list(dict.fromkeys(multipliers))
    
    return multipliers        








