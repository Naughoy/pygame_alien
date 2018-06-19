#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_setings=ai_settings

        #加载图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True


    def update(self):
        self.x+=self.ai_setings.alien_speed_factor*self.ai_setings.fleet_direction
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)