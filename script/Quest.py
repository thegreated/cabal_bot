import pyautogui as pt
from time import sleep
import Bot


class Quest:
    pt.FAILSAFE = True
    def __init__(self, questUrl, quest_url_magician, quest_url_gladiator,
                 confirmation, npc_check,
                 npc_check_two, skip_tutorial, confirm_tutorial,
                 okay_button, accept_reward,
                 dangeon_panel, dangeon_btn, skill_exit,
                 exit_btn_two, auto_attack_check,auto_attack_click,
                 skip_ending, skill_recommend, skill_recommend_confirm,
                 skill_exit_two,accept_reward_two, quest_check,quest_check_two,
                 quest_check_gray, quest_check_gray_two, quest_check_blue ,
                 quest_check_blue_two):

        self.questUrl = questUrl
        self.quest_url_magician = quest_url_magician
        self.quest_url_gladiator = quest_url_gladiator
        self.confirmation = confirmation
        self.npc_check = npc_check
        self.npc_check_two = npc_check_two
        self.skip_tutorial = skip_tutorial
        self.confirm_tutorial = confirm_tutorial
        self.okay_button = okay_button
        self.accept_reward = accept_reward

        self.dangeon_panel = dangeon_panel
        self.dangeon_btn = dangeon_btn
        self.skill_exit = skill_exit
        self.exit_btn_two = exit_btn_two
        self.auto_attack_check = auto_attack_check
        self.auto_attack_click = auto_attack_click
        self.skip_ending = skip_ending
        self.skill_recommend = skill_recommend
        self.skill_recommend_confirm = skill_recommend_confirm
        self.skill_exit_two = skill_exit_two
        self.accept_reward_two = accept_reward_two
        self.quest_check = quest_check
        self.quest_check_two = quest_check_two
        self.quest_check_gray = quest_check_gray
        self.quest_check_gray_two = quest_check_gray_two
        self.quest_check_blue = quest_check_blue
        self.quest_check_blue_two = quest_check_blue_two


    def main(self):

        selector = self.questselectcolor()
        self.warpflow()
        colorblue = (29, 104, 154)
        color = self.colorSelector(colorblue)
        print("COLOR-BOOLEAN")
        print(color)
        self.panelcheck()
        self.skillflow()

        # if self.exittwo():
        #     sleep(1)
        # bug exit dungeon panel
        if self.skipending():
            sleep(1)

        print(selector)
        return selector


    def skillflow(self):
        if self.skillrecommend():
            self.skillExit()
            self.skillexittwo()
            if self.skillrecommendconfirm():
                self.skillExit()
                self.skillexittwo()
            sleep(.5)
        if self.skillExit():
            sleep(.5)

    def panelcheck(self):
        if self.npccheck() or self.npcchecktwo():
            pt.doubleClick()
        if self.tutorialskip():
            sleep(.5)
        if self.confirmtutorial():
            self.okbuttonclick()
        if self.acceptreward() or self.acceptrewardtwo():
            sleep(.5)

    def warpflow(self):
        if self.warpcheck():
            sleep(7)
            pt.press('space')
            self.questclick()

    def questclick(self):
        data = self.pointer(self.questUrl, 40, 320)
        if data:
            pt.doubleClick()
            print("-->Quest click")
        return data

    def questcheck(self):
        data = self.pointer(self.quest_check, 40, 320)
        print("-->Quest check")
        print(data)
        return data

    def questselectcolor(self):
        if self.questclick() or self.questUrlMagician() or self.questUrlGladiator():
            sleep(.5)


    def questcheckGray(self):
        data = self.pointer(self.quest_check_gray, 40, 20)
        print("-->Quest check Gray")
        pt.doubleClick()
        return data

    def questcheckGraytwo(self):
        data = self.pointer(self.quest_check_gray_two, -100, 20)
        print("-->Quest check Gray Two")
        pt.doubleClick()

        return data

    def questcheckBlue(self):
        data = self.pointer(self.quest_check_blue, -100, 20)
        print("-->Quest Blue")
        print(data)
        pt.doubleClick()
        return data

    def questcheckBlueTwo(self):
        data = self.pointer(self.quest_check_blue_two, -100, 20)
        print("-->Quest Blue two")
        print(data)
        pt.doubleClick()
        return data

    def questUrlMagician(self):
        data = self.pointer(self.quest_url_magician, 40, 320)
        if data:
            pt.doubleClick()
            print("-->Quest click")
        return data

    def questUrlGladiator(self):
        data = self.pointer(self.quest_url_gladiator, 40, 320)
        if data:
            pt.doubleClick()
            print("-->Quest click")
        return data

    def warpcheck(self):
        data =  self.pointer(self.confirmation,40, 20)
        if data:
            pt.click()
            print("-->warp check")
        return data

    def npccheck(self):
            data = self.pointer(self.npc_check, 40, 520)
            if data:
                pt.doubleClick()
                print("-->npc check")
            return data

    def npcchecktwo(self):
            data = self.pointer(self.npc_check_two, 120, 260)
            if data:
                pt.doubleClick()
                print("-->npc check_2")
            return data

    def tutorialskip(self):
            data = self.pointer(self.skip_tutorial, 70, 20)
            if data:
                pt.click()
                print("-->tutorial skip")
            return data

    def confirmtutorial(self):
            data = self.pointer(self.confirm_tutorial, 40, 20)
            if data:
                pt.click()
                print("-->confirm tutorial panel show")
            return data

    def okbuttonclick(self):
        data = self.pointer(self.okay_button, 40, 20)
        if data:
            pt.click()
            print("-->button ok click")
        return data

    def okbuttonclick(self):

        data = self.pointer(self.okay_button, 40, 20)
        if data:
            pt.click()
            print("-->Accept Reward ")
        return data

    def acceptreward(self):
        data = self.pointer(self.accept_reward, 40, 20)
        if data:
            pt.click()
            print("-->Accept Reward")
        return data

    def acceptrewardtwo(self):
        data = self.pointer(self.accept_reward_two, 40, 20)
        if data:
            pt.click()
            print("-->Accept Reward two")
        return data


    def skillexittwo(self):
        data = self.pointer(self.skill_exit_two, 20, 20)
        if data:
            pt.click()
            print("-->Skill Exit_two")
        return data

    def skillExit(self):

        data = self.pointer(self.skill_exit, 20, 20)
        if data:
            pt.click()
            print("-->Skill Exit")
        return data

    def exittwo(self):

        data = self.pointer(self.exit_btn_two, 20, 20)
        if data:
            pt.click()
            print("-->Exit Two")
        return data

    def autoattackcheck(self):
        data = self.pointer(self.auto_attack_check, 30, 20)
        if data:
            pt.click()
            print("-->Auto Attact check")
        return data

    def autoattackclick(self):

        data = self.pointer(self.auto_attack_click, -80, 140)
        if data:
            print("-->Auto Attact click")
        return data

    def skipending(self):
        data = self.pointer(self.skip_ending, 50, 20)
        if data:
            pt.doubleClick()
            print("-->Skip Ending")
        return data

    def skillrecommend(self):
        data = self.pointer(self.skill_recommend, 40, 20)
        if data:
            pt.click()
            print("-->Click skill recommend")
        return data

    def skillrecommendconfirm(self):
        data = self.pointer(self.skill_recommend_confirm, 40, 20)
        if data:
            pt.click()
            print("-->Click skill recommend confirm")
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

    def colorSelector(self, color):
        s = pt.screenshot()
        for x in range(s.width):
            for y in range(s.height):
                if s.getpixel((x, y)) == color:
                    pt.doubleClick(x, y)  # do something here
                    return True




