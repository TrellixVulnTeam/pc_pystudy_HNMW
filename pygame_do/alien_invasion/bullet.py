# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""创建子弹"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""对飞船发射出的子弹管理的类"""
	def __init__(self, ai_settings, screen, ship):
		"""在飞船所在处创建一个子弹对象"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		# 在（0,0）处创建一个子弹的矩形，在设置位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
		                        ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#存储用小数表示子弹位置
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	
	def update(self):
		"""向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y
	
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		