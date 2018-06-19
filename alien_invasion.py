#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("武装飞船")

    #创建Play按钮
    play_button=Button(ai_settings,screen,"play")

    #创建一个用于存储游戏统计信息的实例
    stats=GameStats(ai_settings)

    # 创建记分牌
    sb=Scoreboard(ai_settings,screen,stats)

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets=Group()

    #创建外星人群
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        # 监听事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        # 更新屏幕绘制
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
