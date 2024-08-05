# pip install pyautogui, opencv-python

from pyautogui import locateCenterOnScreen, moveTo, click
from time import sleep
from ..tools import href

def _click_button(button_name:str, x=0, y=0) -> bool:
    sleep(0.5)
    try:
        pos = locateCenterOnScreen(href(f'img\{button_name}.png'), confidence=0.8)
        moveTo((pos.x+x, pos.y+y))
        click()
    except Exception as e:
        print(f"Error '{button_name}, {e}'")
        return False
    return True

def ardublock() -> bool:
    res =         _click_button('Tools')
    res = res and _click_button('ArduBlock')
    return res

def _board(board_name:str,  x=0, y=0) -> bool:
    res =         _click_button('Tools')
    res = res and _click_button('Board')
    res = res and _click_button('Arduino AVR Boards')
    res = res and _click_button(board_name, x, y)
    return res

def board_nano() -> bool: return _board('Nano', y=20)
def board_uno()  -> bool: return _board('Uno')
def board_mega() -> bool: return _board('Mega')    


# TODO: Port, nano