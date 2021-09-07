
from Quest import *

class QuestColl:

    def main(self ,File):
        folder = "quest/"
        link = File + folder + "img_quest_01.png"
        questUrlMagician = File + folder + "img_quest_02.png"
        quest_url_gladiator = File + folder + "img_quest_03.png"
        confirmation = File + folder + "img_warp_question_confirmation.png"
        npc_check = File + folder + "img_npc_check.png"
        npc_check_two = File + folder + "img_npc_check_two.png"
        skip_tutorial = File + folder + "img_tutorial_skip.png"
        confirm_tutorial = File + folder + "img_tutorial_confirm.png"
        okay_button = File + folder + "img_ok_btn.png"
        accept_reward = File + folder + "img_accept_reward.png"
        dangeon_panel = File + folder +"img_dangeon_panel.png"
        dangeon_btn = File + folder +"img_dangeon_btn.png"
        skill_exit = File + folder +"img_skill_exit.png"
        skill_exit_two = File + folder +"img_skill_exit_two.png"
        exit_btn_two = File + folder +"img_skill_exit_2.png"
        auto_attack_check = File + folder + "img_auto_attack.png"
        auto_attack_click = File + folder +"auto_attack_click.png"
        skip_ending = File +folder + "img_skip_ending.png"
        skill_recommend = File +folder +"img_skill_recomend.png"
        skill_recommend_confirm = File + folder + "img_skill_confirm.png"
        accept_reward_two = File + folder +"img_accept_reward_two.png"
        quest_check = File + folder + "img_quest_check.png"
        quest_check_two = File + folder + "img_quest_check_two.png"
        quest_check_gray = File + folder + "img_quest_check_done.png"
        quest_check_gray_two = File + folder + "img_quest_check_done_two.png"
        quest_check_blue =  File + folder + "img_quest_check.png"
        quest_check_blue_two = File + folder + "img_quest_check_two.png"

        quest = Quest(link, questUrlMagician, quest_url_gladiator,
                      confirmation, npc_check, npc_check_two,
                      skip_tutorial, confirm_tutorial, okay_button,
                      accept_reward, dangeon_panel,
                      dangeon_btn, skill_exit, exit_btn_two,
                      auto_attack_check, auto_attack_click,
                      skip_ending, skill_recommend, skill_recommend_confirm,
                      skill_exit_two, accept_reward_two, quest_check,quest_check_two,
                      quest_check_gray, quest_check_gray_two, quest_check_blue ,
                      quest_check_blue_two)

        return quest

