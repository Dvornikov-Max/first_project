from utils import chance_roll

class SkySystem:
    """
    Облака: 1 — обычные, 2 — грозовые.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sky_map = [[0 for _ in range(width)] for _ in range(height)]

    def refresh(self, cloud_chance=1, cloud_max=20, storm_chance=1, storm_max=10):
        for row in range(self.height):
            for col in range(self.width):
                if chance_roll(cloud_chance, cloud_max):
                    self.sky_map[row][col] = 2 if chance_roll(storm_chance, storm_max) else 1
                else:
                    self.sky_map[row][col] = 0

    def export_data(self):
        return {'sky_map': self.sky_map}

    def import_data(self, data):
        self.sky_map = data.get('sky_map') or [[0 for _ in range(self.width)] for _ in range(self.height)]
