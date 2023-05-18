import pyautogui
from pynput.keyboard import Listener, Key
import time
import json

poke_name = 'cleffa'

class Rec:
    def __init__(self):
        self.count = 0
        self.coordinates = []

    def photo(self):
        x, y = pyautogui.position()
        screen_shot = pyautogui.screenshot(region=(x - 9, y - 9, 18, 18))
        patch = f'{poke_name}/flag_{self.count}.png'
        screen_shot.save(patch)
        self.count += 1
        infos = {
            "patch": patch,
            "move": [],
            "wait": 0,
            "start": None
        }
        self.coordinates.append(infos)

    def tick(self):
        if self.coordinates:
            last_coordinates = self.coordinates[-1]
            if last_coordinates["start"] is None:
                last_coordinates["start"] = time.time()
            else:
                last_coordinates["wait"] = time.time() - last_coordinates["start"]
                del last_coordinates["start"]

    def move(self):
        x, y = pyautogui.position()
        last_coordinate = self.coordinates[-1]
        last_coordinate["move"] = [x, y]
        print(last_coordinate)

    def key_code(self, key):
        print(key)
        if key == Key.esc:
            with open(f'{poke_name}/{poke_name}.json', 'w') as file:
                json.dump(self.coordinates, file)

            return False
        if key == Key.insert:
            self.photo()
        if key == Key.home:
            self.move()
        if key == Key.page_up:
            self.tick()

    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()

record = Rec()
record.start()