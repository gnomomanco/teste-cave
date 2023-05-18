import pyautogui
from pynput.keyboard import Listener, Key
from pynput import keyboard
import threading
import json
from actions import ATTACK, Actions
from time import sleep

ATTACK = [
    {"button": "F12", "delay": 0.6},
    {"button": "F9", "delay": 0.6},
    {"button": "F5", "delay": 0.6},
    {"button": "F6", "delay": 0.6},
    {"button": "F7", "delay": 0.6},
    {"button": "F8", "delay": 0.6},
    {"button": "F4", "delay": 0.6}
]

IS_POKEBALL = False                    #se tiver true vai usar ball false não vai usar


class Hunt:
    def __init__(self):
        self.isStarted = True
        with open('cleffa/cleffa.json', 'r') as file:
            infos = file.read()
        self.infos = json.loads(infos)
        self.actions = Actions()
      

    def go_to_flag(self, item):
        for i in range(10):
            flag_position = pyautogui.locateAllOnScreen(item['patch'], confidence=0.8)
            if flag_position == None:
                return
            self.actions.move_to_and_click(flag_position)
            sleep(item['wait'])


    def do_attack(self, time, item):
         for i in range(time):
             if pyautogui.locateAllOnScreen('cleffa/cleffa.png', confidence=0.8) is None:
                  break
             pyautogui.moveTo(item["move"][0], item["move"][1], 0.1)
             self.actions.pokemon_moviment(3)
             self.actions.exec_hotkey(ATTACK)
             self.actions.revive()


    def collect_items(self, item):
        pyautogui.moveTo(item["move"][0], item["move"][1], 0.1)
        pyautogui.click()
        sleep(1)    
        self.actions.exec_hotkey('F11')


    def use_pokeball(self):
        if IS_POKEBALL == True and pyautogui.locateAllOnScreen('pokeballs.png', confidence=0.8) is not None:
          for i in range(7):
            pokemon = pyautogui.locateAllOnScreen('cleffa/teste.png', confidence=0.8)
            self.actions.pokeball(pokemon)
            



    def start_route(self):
        while self.isStarted:
            for item in self.infos:
                self.go_to_flag(item)
                self.do_attack(4, item)
                sleep(1)
                self.collect_items(item)
                self.use_pokeball()
                
                


    def target_key(self, key):
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.page_down:
            threading.Thread(target=self.start_route).start()

    def start_Keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()


hunt = Hunt()
hunt.start_Keyboard()
