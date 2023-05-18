import pyautogui
import keyboard
import button
from time import sleep


MY_POKE_POSITION = (1744, 258)


ATTACK = [
    {"button": "F12", "delay": 0.6},
    {"button": "F9", "delay": 0.6},
    {"button": "F5", "delay": 0.6},
    {"button": "F6", "delay": 0.6},
    {"button": "F7", "delay": 0.6},
    {"button": "F8", "delay": 0.6},
    {"button": "F4", "delay": 0.6}
]


class Actions:
    def __init__(self):
        pass

    def move(self, imagem_position):
        x, y = pyautogui.center (imagem_position)
        pyautogui.moveTo(x, y, 0.1)

    def move_to_and_click(self, imagem_position):
        self.move (imagem_position)
        pyautogui.click()


    def exec_hotkey(self, hotkey, delay=0.5):
            muk = True
            if type(hotkey) == list:
                 for attack in hotkey:
                    if muk == None:
                         return
                    keyboard.press(button.key[hotkey["button"]], attack['delay'])
                    muk = pyautogui.locateAllOnScreen('muk.png', confidence=0.8)
            else:
                keyboard.press(button.key[hotkey], delay)
    
    def revive(self):
         current_position = pyautogui.position()
         pyautogui.moveTo(MY_POKE_POSITION)
         pyautogui.click(button="right")
         self.exec_hotkey('BACKSPACE')
         sleep(0.33)
         pyautogui.click()
         pyautogui.click(button="right")
         pyautogui.moveTo(current_position)

         

    def pokemon_moviment(self):
         for i in range(3):
              self.exec_hotkey('CAPS')
              sleep(0.3)


    def pokeball(self, pokemon):
         if pokemon is not None:
              x, y = pyautogui.center(pokemon)
              pyautogui.moveTo(x, y)
              self.exec_hotkey("TAB")
              sleep(0.0)
