
from _quest_coll import *
from _dangeon_coll import *
from _attack_coll import *

class Main:

    def __init__(self):

        file = "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/images/"
        quest = QuestColl().main(file)
        dangeon = DangeonColl().main(file)
        attact = AttackColl().main(file)

        self.quest = quest
        self.dangeon = dangeon
        self.attact = attact

    def main(self):

        while True:

            condition = self.quest.main()
            self.attact.main()
            self.dangeon.main()

            # self.attact.main()
            # self.dangeon.main()




main = Main()
main.main()






