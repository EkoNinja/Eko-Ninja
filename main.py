import os, sys, subprocess, random
subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *

import images as g
player = None
next_location = None

pygame.init()
pygame.display.set_caption("Eko Ninja")
pygame.display.set_icon(g.icon)
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()

pygame.font.init()
title_font = pygame.font.Font("HanaleiFill.ttf", 32)
font = pygame.font.Font("BigShouldersText.ttf", 32)
location = "Home Menu"

mouse_clicked = False
crystals = 0

pygame.mixer.music.load("loop.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)

def clicked(rect):
    if mouse_clicked and rect.collidepoint(pygame.mouse.get_pos()):
        return True
    return False

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2
    fontHeight = font.size("Tg")[1]
    while text:
        i = 1
        if y + fontHeight > rect.bottom:
            break
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        text = text[i:]
    return text

class Player(pygame.sprite.Sprite):
    def __init__(self, character):
        self.x = 100
        self.y = 315
        self.rect = Rect(self.x, self.y, 85, 160)
        self.direction = "right"
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
    def checkScene(self):
        global location
        if self.x <= 0:
            if location == "City Square":
                return
            if location == "Beach":
                location = "City Square"
                self.x = 795
                return
            if location == "Train Station":
                location = "Beach"
                self.x = 795
                return
            if location == "Park":
                location = "Train Station"
                self.x = 795
                return
        if self.x >= 800:
            if location == "City Square":
                location = "Beach"
                self.x = 5
                return
            if location == "Beach":
                location = "Train Station"
                self.x = 5
                return
            if location == "Train Station":
                location = "Park"
                self.x = 5
                return
    def draw(self):
        self.checkScene()
        screen.blit(self.image, self.rect)

class Task(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.visible = True
        self.image = image
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())    

class VanishingTask(Task):
    def draw(self):
        if self.visible == True:
            screen.blit(self.image, self.rect)
            if clicked(self.rect):
                global crystals
                self.visible = False
                crystals = crystals + 1

class ChangingTask(Task):
    def __init__(self, x, y, image1, image2):
        super().__init__(x, y, image1)
        self.image1 = image1
        self.image2 = image2
    def draw(self):
        screen.blit(self.image, self.rect)
        if self.image == self.image1:
            if clicked(self.rect):
                global crystals
                self.image = self.image2
                crystals = crystals + 1

task1 = VanishingTask(50, 450, g.plastic_waste1)
task2 = VanishingTask(550, 350, g.plastic_waste2)
task3 = VanishingTask(200, 100, g.plastic_waste3)
task4 = VanishingTask(550, 75, g.plastic_waste4)

task5 = ChangingTask(30, 500, g.lightbulb1, g.lightbulb2)
task6 = ChangingTask(720, 500, g.lightbulb1, g.lightbulb2)

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
            next_location = None
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "f8":
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if pygame.key.name(event.key) == "escape":
                player = None
                location = "Home Menu"
            if pygame.key.name(event.key) == "h":
                player = None
                location = "Controls"
                    
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
        if player: next_location = "City Square"

    if location == "Instructions":
        text = "When the sun goes down and the shadows begin to lengthen, a group of Ninja protect the Japanese City of Tokyo from evil spirits. Complete tasks in order to earn crystals to reinforce the magical barrier protecting the city. However, watch out, as Ninja are misunderstood and the people of Tokyo think you’re up to no good. Actually, generations of your kind have been protecting the city for thousands of years! But they don’t know this, so beware of guards patrolling the streets - they specialise in catching Ninja and are out to imprison you! And, if the guards weren’t enough, you must finish all of your tasks before sunrise, before it’s too late and the spirits grow stronger to devour the city. Press the \"H\" key for the controls."
        drawText(screen, text, (0, 0, 0), Rect(10, 10, 790, 590), font)

    if location == "Controls":
        text = []
        text.append("Movement: Arrow keys or WASD")
        text.append("Activate Task: Spacebar")
        text.append("Return to Home Screen: ESCAPE")
        text.append("Pause Music: F8")
        text.append("View Controls: H")
        y = 10
        for x in text:
            drawText(screen, x, (0, 0, 0), Rect(10, y, 790, 590), font)
            y = y + 40
        
    if location == "City Square":
        screen.blit(g.city_square, (0, 0))

    if location == "Beach":
        screen.blit(g.beach, (0, 0))

        task1.draw()
        task2.draw()
        task3.draw()
        task4.draw()

    if location == "Train Station":
        screen.blit(g.train_station, (0, 0))
        task5.draw()
        task6.draw()

    if location == "Park":
        screen.blit(g.park, (0, 0))

    if not location == "Home Menu":
        if not location == "Character Menu":
            if not location == "Instructions":
                if not location == "Controls":
                    screen.blit(g.crystal_widget, (650, 10))
                    text = font.render(str(crystals), False, (0, 0, 0))
                    screen.blit(text, (720, 40))

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

    pygame.display.update()
