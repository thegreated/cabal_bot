import pyautogui as pt
from time import sleep
import pyperclip
import random


def delete_item():

    print('delete confirmation')
    sleep(1)
    positionConfirm = pt.locateOnScreen(
        "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/delete_confirmation.png",
        confidence=.8)
    x = positionConfirm[0]
    y = positionConfirm[1]
    pt.moveTo(x, y, duration=.1)
    pt.moveTo(x + 40, y + 30, duration=.1)
    pt.click()


def delete_select():
    global x, y
    print('moving delete button')
    position = pt.locateOnScreen(
        "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/delete.png", confidence=.8)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.1)
    pt.moveTo(x + 40, y + 30, duration=.1)
    pt.click()
    return True


def select_item_to_modify():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/g3_item.png", confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 60, duration=.1)
        pt.click()
        return True
    except:
       return False


def select_item_to_modify_two():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/g3_item_two.png", confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 60, duration=.1)
        pt.click()
        return True
    except:
       return False


def select_item_to_modify_four():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/g3_item_four.png", confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 60, duration=.1)
        pt.click()
        return True
    except:
       return False


def select_item_to_modify_tree():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/g3_item_tree.png", confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 60, duration=.1)
        pt.click()
        return True
    except:
       return False


def sort_item():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/sort.png",
            confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 30, duration=.1)
        pt.click()
        return True
    except:
        return False


def select_extract_after_sort():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/_g5_item.png",
            confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 20, y + 20, duration=.1)
        pt.click()
        return True
    except:
        return False


def select_extract_after_sort_1():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/_g6_item_red.png",
            confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 20, y + 20, duration=.1)
        pt.click()
        return True
    except:
        return False


def select_extract_after_sort_2():
        try:
            positionMod = pt.locateOnScreen(
                "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/_g67_item_red.png",
                confidence=.8)
            x = positionMod[0]
            y = positionMod[1]
            pt.moveTo(x, y, duration=.1)
            pt.moveTo(x + 20, y + 20, duration=.1)
            pt.click()
            return True
        except:
            return False


def extract():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/extract.png",
            confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 30, duration=.1)
        pt.click()
        return True
    except:
        return False


def agree_extract():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/agree_extract.png",
            confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 30, duration=.1)
        pt.click()
        return True
    except:
        return False


def after_extract():
    try:
        positionMod = pt.locateOnScreen(
            "C:/Users/edwar/OneDrive/Documents/Python projects/cabal_item_drop/cabalmain/after_extract.png",
            confidence=.8)
        x = positionMod[0]
        y = positionMod[1]
        pt.moveTo(x, y, duration=.1)
        pt.moveTo(x + 50, y + 30, duration=.1)
        pt.click()
        return True
    except:
        return False



while True:

    try:
      sleep(1)
      # if select_item_to_modify() or select_item_to_modify_two() or select_item_to_modify_tree() or select_item_to_modify_four():
      #       if delete_select():
      #           delete_item()
      # else:
      sort_item()
      if select_extract_after_sort() or select_extract_after_sort_1() or select_extract_after_sort_2():
            extract()
            agree_extract()
      else:
          after_extract()


    except:
        print('Reload browser')






