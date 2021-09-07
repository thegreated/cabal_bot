from MiniQuest import *


class DangeonColl:

    def main(self, File):

        cabal_logo = File + "mini_quest/img_mini_quest_1.png"
        quest_icon = File + "mini_quest/img_mini_quest_2.png"
        progressClicked = File + "mini_quest/img_mini_quest_3.png"
        miniquestunclick = File + "mini_quest/img_mini_quest_3_unclick.png"

        miniquest = MiniQuest(cabal_logo,quest_icon, progressClicked,
                              miniquestunclick)

        return miniquest

