import os, sys, random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *

import images as g
player = None
next_location = None

pygame.init()
pygame.display.set_caption("Eko Ninja")
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()

pygame.font.init()
title_font = pygame.font.Font("HanaleiFill-Regular.ttf", 32)
font = pygame.font.Font("BigShouldersText-Regular.ttf", 32)
location = "Home Menu"

mouse_clicked = False

class Player(pygame.sprite.Sprite):
    def __init__(self, character):
        self.x = 100
        self.y = 315
        self.rect = Rect(self.x, self.y, 85, 160)
        self.direction = "right"
        self.isInAir = False
        self.hasJumped = False
        self.isJumping = False
        self.image = character
    def move(self, x, y):
        if not self.x <= 0 and not self.x >= 800:
            self.x = self.x + x
            self.y = self.y + y
            self.rect = Rect(self.x, self.y, 85, 160)
        if not self.y <= 0 and not self.y >= 600:
            self.x = self.x + x
            self.y = self.y + y
            self.rect = Rect(self.x, self.y, 85, 160)
        self.rect.clamp_ip(screen_rect)
    def jump(self):
        if self.hasJumped == False:
            self.isJumping = True
    def draw(self):
        if self.isJumping == True:
            self.y = self.y - 4
        if self.y < 315:
            self.isInAir = True
            if self.y < 275: self.hasJumped = True
            if self.hasJumped == True:
                self.y = self.y + 4
        else:
            self.isInAir = False
            self.hasJumped = False
            self.isJumping = False
        screen.blit(self.image, self.rect)

def clicked(rect):
    if mouse_clicked and rect.collidepoint(pygame.mouse.get_pos()):
        return True
    return False

while 1:
    pygame.time.Clock().tick(60)
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            os._quit(0)
        if event.type == MOUSEBUTTONDOWN and mouse_clicked == False:
            mouse_clicked = True
        if event.type == MOUSEBUTTONUP:
            mouse_clicked = False
            if next_location: location = next_location
    screen.blit(g.background_image, (0, 0))
    if location == "Home Menu":
        title = title_font.render("Eko Ninja", False, (20, 54, 2))
        screen.blit(title, (340, 100))
        
        screen.blit(g.blue_skin, (10, 10))
        screen.blit(pygame.transform.flip(g.green_skin, True, False), (705, 10))
        screen.blit(g.red_skin, (10, 430))
        screen.blit(pygame.transform.flip(g.purple_skin, True, False), (705, 430))

        screen.blit(g.play_button, (300, 245))
        screen.blit(g.htp_button, (300, 325))

        if clicked(Rect(300, 245, 200, 73)): next_location = "Character Menu"
        if clicked(Rect(300, 325, 200, 73)): next_location = "Instructions"

    if location == "Character Menu":
        screen.blit(g.blue_skin_button, (100, 120))
        screen.blit(g.brown_skin_button, (400, 120))
        screen.blit(g.green_skin_button, (100, 210))
        screen.blit(g.pink_skin_button, (400, 210))
        screen.blit(g.purple_skin_button, (100, 300))
        screen.blit(g.red_skin_button, (400, 300))
        temptext = font.render("Choose your Character", False, (0, 0, 0))
        screen.blit(temptext, (275, 450))

        if clicked(Rect(100, 120, 300, 80)): player = Player(g.blue_skin)
        if clicked(Rect(400, 120, 300, 80)): player = Player(g.brown_skin)
        if clicked(Rect(100, 210, 300, 80)): player = Player(g.green_skin)
        if clicked(Rect(400, 210, 300, 80)): player = Player(g.pink_skin)
        if clicked(Rect(100, 300, 300, 80)): player = Player(g.purple_skin)
        if clicked(Rect(400, 300, 300, 80)): player = Player(g.red_skin)
        if Player: next_location = "City Square"
    if location == "City Square":
        screen.blit(g.city_square, (0, 0))

    if player and not location == "Character Menu":
        player.draw()
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            if player.direction == "left": player.image = pygame.transform.flip(player.image, True, False)
            player.move(2, 0)
            player.direction = "right"
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            if player.direction == "right": player.image = pygame.transform.flip(player.image, True, False)
            player.move(-2, 0)
            player.direction = "left"
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            player.move(0, -2)
            player.isInAir = True
    pygame.display.update()
