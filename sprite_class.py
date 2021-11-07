import os

import pygame
from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, top_left):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 150))
        self.image_o = pygame.image.load("o.png").convert_alpha()
        self.image_x = pygame.image.load("x.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.topleft = top_left
        self.is_x = False
        self.was_clicked = False

    def click(self, event, flag, board):
        if self.rect.collidepoint(event.pos) and not self.was_clicked:
            if flag:
                board[self.rect.top // 166][self.rect.left // 166] = -1
                self.image = self.image_o
            else:
                board[self.rect.top // 166][self.rect.left // 166] = 1
                self.image = self.image_x
                self.is_x = True
            self.image = pygame.transform.smoothscale(self.image, (150, 150))
            self.was_clicked = True
            return True
        return False



