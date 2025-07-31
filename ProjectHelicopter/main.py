from clouds import SkySystem
import map as game_map
import time
import os
from helicopter import Chopper
from pynput import keyboard
import json

#Параметры игры
frame_count = 1
tick_interval = 1
tree_interval = 40
clouds_interval = 30
fire_interval = 15
map_width, map_height = 20, 10

#Инициализация объектов
drone = Chopper(map_width, map_height)
cloud_system = SkySystem(map_width, map_height)
world = game_map.GameMap(map_width, map_height)

#Начальный вывод карты
world.render(drone, cloud_system)

#Направления движения
DIRECTIONS = {
    'w': (-1, 0),
    'd': (0, 1),
    's': (1, 0),
    'a': (0, -1)
}

#Обработка нажатий клавиш
def handle_key_release(key):
    global drone, frame_count, cloud_system, world

    try:
        char = key.char.lower()
    except AttributeError:
        return

    if char in DIRECTIONS:
        dx, dy = DIRECTIONS[char]
        drone.move(dx, dy)

    elif char == 'f':  #Сохранение игры
        save_data = {
            'helicopter': drone.export_data(),
            'clouds': cloud_system.export_data(),
            'field': world.export_data(),
            'tick': frame_count
        }
        with open('savegame.json', 'w') as file:
            json.dump(save_data, file)

    elif char == 'g':  #Загрузка игры
        if os.path.exists('savegame.json'):
            with open('savegame.json', 'r') as file:
                saved = json.load(file)
                drone.import_data(saved.get('helicopter', {}))
                cloud_system.import_data(saved.get('clouds', {}))
                world.import_data(saved.get('field', {}))
                frame_count = saved.get('tick', 0)

keyboard.Listener(on_release=handle_key_release).start()

#Основной цикл игры
def game_loop():
    global frame_count
    while True:
        os.system('cls')
        world.handle_chopper_interaction(drone, cloud_system)
        drone.display_status()
        world.render(drone, cloud_system)
        print(f'Frame: {frame_count}')

        frame_count += 1
        time.sleep(tick_interval)

        if frame_count % tree_interval == 0:
            world.grow_tree()
        if frame_count % fire_interval == 0:
            world.update_fire_cells()
        if frame_count % clouds_interval == 0:
            cloud_system.refresh()

#Запуск игры
if __name__ == "__main__":
    game_loop()
