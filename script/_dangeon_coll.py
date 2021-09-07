from Dangeon import *


class DangeonColl:

    def main(self, File):
        folder = "dungeon/"
        okay_button = File + folder + "img_ok_btn.png"
        dangeon_panel = File + folder +"img_dangeon_panel.png"
        dangeon_btn = File + folder +"img_dangeon_btn.png"
        dangeon_btn_two = File + folder + "img_dangeon_btn_two.png"
        dangeon_clear = File + folder + "img_dangeon_clear.png"
        dangeon_clear_two = File + folder + "img_dangeon_clear_two.png"
        dangeon_clear_click = File + folder + "img_exit_button.png"
        auto_attack_click = File + folder + "auto_attack_click.png"
        afk_attack = File + folder + "img_afk.png"
        revive_check = File + folder + "img_revive_check.png"
        item_entrance = File + folder + "img_item_entrance.png"
        character_dead = File + "mini_quest/character_dead.png"
        okay_button_revive = File + "mini_quest/img_ok_button.png"
        okay_button_solo = File + "mini_quest/img_solo_ok.png"

        dangeon = Dangeon(dangeon_panel, dangeon_btn, dangeon_btn_two,
                          dangeon_clear, dangeon_clear_two,dangeon_clear_click, afk_attack,
                          auto_attack_click, revive_check, okay_button,
                          item_entrance, character_dead,okay_button_revive,
                          okay_button_solo

                          )

        return dangeon

