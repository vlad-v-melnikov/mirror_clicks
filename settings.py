import json
from pyautogui import size

class Settings:
    def __init__(self) -> None:
        try:
            with open('settings.json') as f:
                settings = json.load(f)
            self.keymap_exit = settings['keymap_exit']
            self.keymap_action = settings['keymap_action']
            self.keymap_compare = settings['keymap_compare']
            self.screenshot_region = tuple(settings['screenshot_region'])
            self.compare_region = tuple(settings['compare_region'])
            self.confidence_level = settings['confidence_level']

        except FileNotFoundError:
            print("settings.json file not found. Quitting the script...")
            exit()

        self.screen_width, self.screen_height = size()