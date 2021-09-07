import pyautogui as pt
from time import sleep
import Bot
import random


class Attack:

    def __init__(self, attack_done, auto_attack_click,
                 auto_attack_check, auto_attack_check_two,
                 bangkai_one, player_attack, quest_logo):
        self.attack_done = attack_done
        self.auto_attack_click = auto_attack_click
        self.auto_attack_check = auto_attack_check
        self.auto_attack_check_two = auto_attack_check_two
        self.bangkai_one = bangkai_one
        self.player_attack = player_attack
        self.quest_logo = quest_logo



    def main(self):
        attacking = self.playerAttack()
        print("ATTACT CHECK")
        if self.autoattackcheck() or self.autoattackchecktwo():
            print("-->auto attact trigger")
            if self.playerAttack():
                print("Player is attacking now sleep 20")
                while self.questLogoexist():
                    sleep(10  )
                return True
        else:
            self.autoattackclick()

    def autoattackclick(self):
        data = self.pointer(self.auto_attack_click, -200, -20)
        if data:
            print("-->auto attact click")
            pt.click()
            return True
        return data

    def autoattackcheck(self):
        i = 0
        data = self.pointer(self.auto_attack_check, 30, 20)
        return data

    def autoattackchecktwo(self):
        i = 0
        data = self.pointer(self.auto_attack_check_two, 30, 20)
        return data

    def bangkaione(self):
        randomres = random.randint(0, 2)
        data = self.pointer(self.bangkai_one, 40, 20)
        if data and randomres == 1:
            print("-->bangkai")
            pt.click()
            sleep(1)
            pt.click()

    def playerAttack(self):
        data = self.pointer(self.player_attack, 40, 20)
        if data:
            print("-->Player attacking")
        return data

    def questLogoexist(self):
        data = self.pointer(self.quest_logo, 40, 20)
        if data:
            print("-->Quest Exist")
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


