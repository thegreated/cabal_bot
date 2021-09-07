import pyautogui as pt
from time import sleep
import Bot


class MiniQuest:

    def __init__(self,cabal_logo):
        sleep(1)



    def caballogoClick(self):
        data = self.pointer(self.dangeon_clear_click, 40, 20)
        if data:
            print("-->Cabal logo click")
            pt.click()
        return data


    def pointer(self, images, x2, y2):
        try:
            position = pt.locateOnScreen(images, confidence=.9)
            x = position[0]
            y = position[1]
            pt.moveTo(x, y, duration=.1)
            pt.moveTo(x + x2, y + y2, duration=.1)
            return True
        except:
            return False

