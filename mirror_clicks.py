from pynput import keyboard
import pyautogui, logging, msvcrt
from modules.compare import compare_images
from modules.settings import Settings

###################################################

settings = Settings()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

###################################################


def jump_mouse():
    logging.debug("Clicking at at {}".format(pyautogui.position()))
    pyautogui.click(button='left')
    print("Click", end='... ')
    
    pos_x, pos_y = pyautogui.position()
    pyautogui.click(x=pos_x + settings.screen_width/2, y=pos_y, button='left')
    logging.debug("Clicking at {}".format(pyautogui.position()))
    print("Move... Click", end='...')
    
    pyautogui.moveRel(-settings.screen_width/2, 0)
    logging.debug("Moved back to {}".format(pyautogui.position()))

    print("Move back.")


def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    logging.debug('key pressed = ', vk)

    if vk in settings.keymap_exit.values():
        if settings.is_changed:
            settings.save_settings()
            print("Settings saved.")
            while msvcrt.kbhit(): #flushing the buffer to prevent issue with chars typed after ESC 
                msvcrt.getch()
        return False
    
    if vk in settings.keymap_pause.values():
        settings.pause()
        return

    if settings.is_paused:
        return

    if vk in settings.keymap_action.values():
        jump_mouse()

    elif vk in settings.keymap_compare.values():
        compare_images(
            settings.screenshot_region,
            settings.compare_region,
            settings.confidence_level
        )

    elif vk in settings.keymap_conf_up.values():
        settings.conf_up() if not settings.is_paused else print("Script paused")

    elif vk in settings.keymap_conf_down.values() and not settings.is_paused :
        settings.conf_down()

    else:
        print(f'Key {vk} is not bound.')

###################################################


print("Starting...")
settings.key_prompt()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
