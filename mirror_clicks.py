from pynput import keyboard, mouse
import pyautogui, logging, json
from modules.compare import compare_images

###################################################
try:
    with open('settings.json') as f:
        settings = json.load(f)
    keymap_exit = settings['keymap_exit']
    keymap_action = settings['keymap_action']
    keymap_compare = settings['keymap_compare']
    screenshot_region = tuple(settings['screenshot_region'])
    compare_region = tuple(settings['compare_region'])
    confidence_level = settings['confidence_level']

except FileNotFoundError:
    print("settings.json file not found. Quitting the script...")
    exit()

screen_width, screen_height = pyautogui.size()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

###################################################

def jump_mouse():
    logging.debug("Clicking at at {}".format(pyautogui.position()))
    pyautogui.click(button='left')
    print("Click", end='... ')
    
    pos_x, pos_y = pyautogui.position()
    pyautogui.click(x=pos_x + screen_width/2, y=pos_y, button='left')
    logging.debug("Clicking at {}".format(pyautogui.position()))
    print("Move... Click", end='...')
    
    pyautogui.moveRel(-screen_width/2, 0)
    logging.debug("Moved back to {}".format(pyautogui.position()))

    print("Move back.")

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    logging.debug('key pressed = ', vk)

    if(vk in keymap_exit.values()):
        return False
    
    if(vk in keymap_action.values()):
        jump_mouse()
    elif(vk in keymap_compare.values()):
        compare_images(screenshot_region, compare_region, confidence_level)
    else:
        print(f'Key {vk} is not bound.')

with keyboard.Listener(on_press=on_press) as listener:
    print("Starting...")
    print("Press {} to click/mirror click.".format(keymap_action.keys()))
    print("Press {} to compare images.".format(keymap_compare.keys()))
    print("Press {} to quit.".format(keymap_exit.keys()))
    listener.join()
    