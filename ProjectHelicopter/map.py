from utils import chance_roll, random_cell, adjacent_cell
from clouds import SkySystem

#Типы ячеек: пусто, дерево, вода, госпиталь, магазин, огонь
TILE_SYMBOLS = ['🟩', '🌳', '🌊', '🏥', '🏭', '🔥']

BONUS_FOR_TREE = 100
TANK_UPGRADE_COST = 200
LIFE_RESTORE_COST = 500

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self._populate_forest(5, 10)
        self._create_river(10)
        self._create_river(30)
        self._place_shop()
        self._place_hospital()
        self.clouds = SkySystem(width, height)

    def in_bounds(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width

    def render(self, chopper, clouds):
        print('⬛️' * (self.width + 2))
        for row in range(self.height):
            print('⬛️', end='')
            for col in range(self.width):
                symbol = TILE_SYMBOLS[self.grid[row][col]]
                if clouds.sky_map[row][col] == 1:
                    symbol = '☁️'
                elif clouds.sky_map[row][col] == 2:
                    symbol = '⛈️'
                elif chopper.row == row and chopper.col == col:
                    symbol = '🚁'
                print(symbol, end='')
            print('⬛️')
        print('⬛️' * (self.width + 2))

    # ------------ Генерация ------------

    def _create_river(self, length):
        x, y = random_cell(self.width, self.height)
        self.grid[x][y] = 2
        while length > 0:
            nx, ny = adjacent_cell(x, y)
            if self.in_bounds(nx, ny):
                self.grid[nx][ny] = 2
                x, y = nx, ny
                length -= 1

    def _populate_forest(self, r, mxr):
        for i in range(self.height):
            for j in range(self.width):
                if chance_roll(r, mxr):
                    self.grid[i][j] = 1

    def grow_tree(self):
        x, y = random_cell(self.width, self.height)
        if self.grid[x][y] == 0:
            self.grid[x][y] = 1

    def _place_shop(self):
        x, y = random_cell(self.width, self.height)
        self.grid[x][y] = 4

    def _place_hospital(self):
        x, y = random_cell(self.width, self.height)
        if self.grid[x][y] != 4:
            self.grid[x][y] = 3
        else:
            self._place_hospital()

    # ------------ Пожары ------------

    def _ignite_tree(self):
        x, y = random_cell(self.width, self.height)
        if self.grid[x][y] == 1:
            self.grid[x][y] = 5

    def update_fire_cells(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 5:
                    self.grid[i][j] = 0
        for _ in range(5):
            self._ignite_tree()

    # ------------ Взаимодействие с вертолётом ------------

    def handle_chopper_interaction(self, chopper, clouds):
        tile = self.grid[chopper.row][chopper.col]
        weather = clouds.sky_map[chopper.row][chopper.col]

        if tile == 2:  # Вода
            chopper.water = chopper.max_tank
        elif tile == 5 and chopper.water > 0:
            chopper.points += BONUS_FOR_TREE
            chopper.water -= 1
            self.grid[chopper.row][chopper.col] = 1
        elif tile == 4 and chopper.points >= TANK_UPGRADE_COST:
            chopper.max_tank += 1
            chopper.points -= TANK_UPGRADE_COST
        elif tile == 3 and chopper.points >= LIFE_RESTORE_COST:
            chopper.health += 10
            chopper.points -= LIFE_RESTORE_COST

        if weather == 2:
            chopper.health -= 1
            if chopper.health <= 0:
                chopper.game_over()

    # ------------ Сохранение / загрузка ------------

    def export_data(self):
        return {'grid': self.grid}

    def import_data(self, data):
        self.grid = data.get('grid') or [[0 for _ in range(self.width)] for _ in range(self.height)]
