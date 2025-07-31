import os
from time import sleep
from utils import random_cell

class Chopper:

    def __init__(self, map_width, map_height):
        start_x, start_y = random_cell(map_width, map_height)
        self.width = map_width
        self.height = map_height
        self.row = start_x
        self.col = start_y
        self.max_tank = 1
        self.water = 0
        self.points = 0
        self.health = 20

    def move(self, d_row, d_col):
        new_x = self.row + d_row
        new_y = self.col + d_col
        if 0 <= new_x < self.height and 0 <= new_y < self.width:
            self.row = new_x
            self.col = new_y

    def display_status(self):
        print(f"💧 {self.water}/{self.max_tank} |❤️ {self.health} |🏆 {self.points}")

    def game_over(self):
        os.system('cls')
        print('+----------------------------------+')
        print('|                                  |')
        print(f'|  Ты помер,товарищ:     {self.points:<5}     |')
        print('|                                  |')
        print('+----------------------------------+')
        exit(0)

    def export_data(self):
        return {
            'row': self.row,
            'col': self.col,
            'points': self.points,
            'health': self.health,
            'water': self.water,
            'max_tank': self.max_tank
        }

    def import_data(self, data):
        self.row = data.get('row', 0)
        self.col = data.get('col', 0)
        self.points = data.get('points', 0)
        self.health = data.get('health', 20)
        self.water = data.get('water', 0)
        self.max_tank = data.get('max_tank', 1)
