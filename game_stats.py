#! /usr/bin/env python
# _*_ coding:utf-8 _*_

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        self.ai_sttings=ai_settings
        self.reset_stats()

        #游戏活动开始状态
        self.game_active=False

        #不可重置的最高得分
        self.high_score=0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.ai_sttings.ship_limit
        self.score=0
        self.level=1