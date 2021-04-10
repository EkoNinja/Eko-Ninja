import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_mode((0, 0))

icon  = pygame.image.load("icon.png").convert_alpha()

background_image = pygame.image.load("Backgrounds/Background.png").convert_alpha()
city_square = pygame.image.load("Backgrounds/City Square.png").convert_alpha()
beach = pygame.image.load("Backgrounds/Beach.png").convert_alpha()

blue_skin = pygame.image.load("Skins/Blue.png").convert_alpha()
brown_skin = pygame.image.load("Skins/Brown.png").convert_alpha()
green_skin = pygame.image.load("Skins/Green.png").convert_alpha()
pink_skin = pygame.image.load("Skins/Pink.png").convert_alpha()
purple_skin = pygame.image.load("Skins/Purple.png").convert_alpha()
red_skin = pygame.image.load("Skins/Red.png").convert_alpha()

blue_skin_button = pygame.image.load("Buttons/Characters/Blue.png").convert_alpha()
brown_skin_button = pygame.image.load("Buttons/Characters/Brown.png").convert_alpha()
green_skin_button = pygame.image.load("Buttons/Characters/Green.png").convert_alpha()
pink_skin_button = pygame.image.load("Buttons/Characters/Pink.png").convert_alpha()
purple_skin_button = pygame.image.load("Buttons/Characters/Purple.png").convert_alpha()
red_skin_button = pygame.image.load("Buttons/Characters/Red.png").convert_alpha()

play_button = pygame.image.load("Buttons/Play.png").convert_alpha()
htp_button = pygame.image.load("Buttons/How To Play.png").convert_alpha()
