import pygame
import sys

class Settings:
	"""Класс для хранения всех настроек игры Alien Invasion"""
	
	def __init__(self):
		"""Инициализирует настройки игры"""
		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (86, 208, 245)

		# Настройки скорости корабля
		self.ship_speed = 2.5

		# Параметры снаряда
		self.bullet_speed = 1.5
		self.bullet_width = 9
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Настройки пришельцев
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# self.fleet_direction = 1 обозначает движение вправо; а -1 - влево
		self.fleet_direction = 1