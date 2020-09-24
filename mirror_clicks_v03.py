from pynput import keyboard, mouse
import pyautogui, logging

keymap_exit = {
    'ESC' : 27,
}

keymap_action = {
    'z' : 90,
    'x' : 88,
    'c' : 67,
    'ENTER' : 13,
}

width, height = pyautogui.size()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def jump_mouse():
    logging.debug("Clicking at at {}".format(pyautogui.position()))
    pyautogui.click(button='left')
    print("Click", end='... ')
    
    #pyautogui.moveRel(width/2, 0)
    pos_x, pos_y = pyautogui.position()
    pyautogui.click(x=pos_x + width/2, y=pos_y, button='left')
    logging.debug("Clicking at {}".format(pyautogui.position()))
    print("Move... Click", end='...')
    
    pyautogui.moveRel(-width/2, 0)
    logging.debug("Moved back to {}".format(pyautogui.position()))

    print("Move back.")

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    if(vk in keymap_exit.values()):
        return False
    logging.debug('key pressed = ', vk)
    if(vk in keymap_action.values()):
        jump_mouse()
    else:
        print(f'Key {vk} is not bound.')
    

with keyboard.Listener(on_press=on_press) as listener:
    print("Starting...")
    print("Press {} to click/mirror click.".format(keymap_action.keys()))
    print("Press {} to quit.".format(keymap_exit.keys()))
    listener.join()
    