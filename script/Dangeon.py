from Quest import *
import pyautogui as pt
from time import sleep



class Dangeon:

    def __init__(self, dungeon_panel, dungeon_btn,
                 dangeon_btn_two,dangeon_clear,dangeon_clear_two,
                 dangeon_clear_click, afk_attack,
                 auto_attack_click, revive_check,
                 okay_button,item_entrance,character_dead,
                 okay_button_revive,okay_button_solo):

        self.dungeon_panel = dungeon_panel
        self.dungeon_btn = dungeon_btn
        self.dangeon_btn_two = dangeon_btn_two
        self.dangeon_clear = dangeon_clear
        self.dangeon_clear_two = dangeon_clear_two
        self.dangeon_clear_click = dangeon_clear_click
        self.auto_attack_click = auto_attack_click
        self.afk_attack = afk_attack
        self.revive_check = revive_check
        self.okay_button = okay_button
        self.item_entrance = item_entrance
        self.character_dead = character_dead
        self.okay_button_revive = okay_button_revive
        self.okay_button_solo = okay_button_solo

    def main(self):
        print("DANGEON CHECK")
        if self.dungeonpanel():
            if self.dungeonbtnclick() or self.dungeonbtnclicktwo():
                sleep(1)
                return True
        if self.dangeonclear() or self.dangeoncleartwo():
            self.dangeonclearclick()
        if self.revivehero():
            self.okbuttonclicktwo()
            sleep(1)
            self.okaybuttonsolo()
        if self.okbuttonclick():
            sleep(1)
        if self.afkattack():
            print("AFK")
        if self.itementrance():
            sleep(1)
        if self.okaybuttonsolo():
            sleep(1)
        return True


    def dungeonpanel(self):

        data = self.pointer(self.dungeon_panel, 40, 20)
        if data:
            print("-->Dungeon panel show")
        return data

    def dungeonbtnclick(self):

        data = self.pointer(self.dungeon_btn, 40, 20)
        if data:
            print("-->Dungeon button click")
            pt.click()
        return data

    def dungeonbtnclicktwo(self):
        data = self.pointer(self.dangeon_btn_two, 40, 20)
        if data:
            print("-->Dungeon button click_two")
            pt.click()
        return data

    def dangeonclear(self):

        data = self.pointer(self.dangeon_clear, 40, 20)
        if data:
            print("-->Dungeon clear")
        return data

    def dangeoncleartwo(self):
        data = self.pointer(self.dangeon_clear_two, 40, 20)
        if data:
            print("-->Dungeon clear two")
        return data

    def dangeonclearclick(self):

        data = self.pointer(self.dangeon_clear_click, 40, 20)
        if data:
            print("-->Dungeon button click")
            pt.click()
        return data

    def afkattack(self):
        data = self.pointer(self.afk_attack, 40, 20)
        if data:
            print("-->hero afk")
        return data

    def autoattackclick(self):
        data = self.pointer(self.auto_attack_click, 70, 20)
        if data:
            print("-->Auto Attact click")
        return data

    def revivehero(self):
        data = self.pointer(self.character_dead, 40, 20)
        print(data)
        if data:
            pt.click()
            print("-->Revive hero")
        return data

    def okbuttonclick(self):
        data = self.pointer(self.okay_button, 40, 20)
        if data:
            pt.click()
            print("-->button ok click")
        return data

    def okbuttonclicktwo(self):
        data = self.pointer(self.okay_button_revive, 40, 20)
        print(data)
        if data:
            pt.click()
            print("-->button ok click")
        return data

    def itementrance(self):
        data = self.pointer(self.item_entrance, 40, 20)
        if data:
            pt.click()
            print("-->Item Entrace click")
        return data

    def okaybuttonsolo(self):
        data = self.pointer(self.okay_button_solo, 40, 20)
        if data:
            pt.click()
            print("-->Solo ok click")
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


