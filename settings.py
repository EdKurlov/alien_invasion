import pygame
import sys

class Settings:
	"""Класс для хранения всех настроек игры Alien Invasion"""
	
	def __init__(self):
		"""Инициализирует настройки игры"""
		# Параметры экрана
		self.screen_width = 1000
		self.screen_height = 700
		self.bg_color = (86, 208, 245)

		# Настройки скорости корабля
		self.ship_speed = 2.5