from Attact import *


class AttackColl:

    def main(self, File):
        folder = "attack/"
        auto_attack_check = File + folder + "img_auto_attack.png"
        auto_attack_check_two = File + folder + "img_auto_attack_two.png"
        auto_attack_click = File + folder + "auto_attack_click.png"
        attack_done = File + folder + "img_attack_done.png"
        bangkai_one = File + folder + "img_bangkai.png"
        player_attack = File + folder + "img_attacking.png"
        quest_logo = File + folder + "img_quest_logo.png"


        attact = Attack(attack_done, auto_attack_click,
                        auto_attack_check,
                        auto_attack_check_two, bangkai_one, player_attack,
                        quest_logo)

        return attact

