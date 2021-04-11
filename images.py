import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_mode((0, 0))

icon  = pygame.image.load("icon.png").convert_alpha()
crystal_widget = pygame.image.load("images/Crystal Widget.png").convert_alpha()

background_image = pygame.image.load("images/Backgrounds/Background.png").convert_alpha()
city_square = pygame.image.load("images/Backgrounds/City Square.png").convert_alpha()
beach = pygame.image.load("images/Backgrounds/Beach.png").convert_alpha()
train_station = pygame.image.load("images/Backgrounds/Train Station.png").convert_alpha()
park = pygame.image.load("images/Backgrounds/Park.png").convert_alpha()

blue_skin = pygame.image.load("images/Skins/Blue.png").convert_alpha()
brown_skin = pygame.image.load("images/Skins/Brown.png").convert_alpha()
green_skin = pygame.image.load("images/Skins/Green.png").convert_alpha()
pink_skin = pygame.image.load("images/Skins/Pink.png").convert_alpha()
purple_skin = pygame.image.load("images/Skins/Purple.png").convert_alpha()
red_skin = pygame.image.load("images/Skins/Red.png").convert_alpha()

blue_skin_button = pygame.image.load("images/Buttons/Characters/Blue.png").convert_alpha()
brown_skin_button = pygame.image.load("images/Buttons/Characters/Brown.png").convert_alpha()
green_skin_button = pygame.image.load("images/Buttons/Characters/Green.png").convert_alpha()
pink_skin_button = pygame.image.load("images/Buttons/Characters/Pink.png").convert_alpha()
purple_skin_button = pygame.image.load("images/Buttons/Characters/Purple.png").convert_alpha()
red_skin_button = pygame.image.load("images/Buttons/Characters/Red.png").convert_alpha()

play_button = pygame.image.load("images/Buttons/Play.png").convert_alpha()
htp_button = pygame.image.load("images/Buttons/How To Play.png").convert_alpha()

plastic_waste1 = pygame.image.load("images/Tasks/Plastic Waste 1.png").convert_alpha()
plastic_waste2 = pygame.image.load("images/Tasks/Plastic Waste 2.png").convert_alpha()
plastic_waste3 = pygame.image.load("images/Tasks/Plastic Waste 3.png").convert_alpha()
plastic_waste4 = pygame.image.load("images/Tasks/Plastic Waste 4.png").convert_alpha()

lightbulb1 = pygame.image.load("images/Tasks/Lightbulb 1.png").convert_alpha()
lightbulb2 = pygame.image.load("images/Tasks/Lightbulb 2.png").convert_alpha()
