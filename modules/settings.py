import json
from pyautogui import size


class Settings:
    is_changed = False
    is_paused = False
    SETTINGS_PATH = 'modules\\settings.json'
    CONF_STEP = 0.01

    def __init__(self) -> None:
        try:
            with open(self.SETTINGS_PATH) as f:
                settings = json.load(f)

            self.keymap_exit = settings['keymap_exit']
            self.keymap_action = settings['keymap_action']
            self.keymap_compare = settings['keymap_compare']
            self.keymap_conf_up = settings['keymap_conf_up']
            self.keymap_conf_down = settings['keymap_conf_down']
            self.keymap_pause = settings['keymap_pause']

            self.screenshot_region = tuple(settings['screenshot_region'])
            self.compare_region = tuple(settings['compare_region'])
            self.confidence_level = settings['confidence_level']

        except FileNotFoundError:
            print("settings.json file not found. Quitting the script...")
            exit()

        self.screen_width, self.screen_height = size()

    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("Script PAUSED.")
        else:
            print("Script continues.")

    def key_prompt(self):
        print("Press {} to click/mirror click.".format(list(self.keymap_action.keys())))
        print("Press {} to compare images.".format(list(self.keymap_compare.keys())))
        print("Press {} to increase confidence level.".format(list(self.keymap_conf_up.keys())))
        print("Press {} to reduce confidence level.".format(list(self.keymap_conf_down.keys())))
        print("Press {} to quit.".format(list(self.keymap_exit.keys())))
        print("Press {} to pause.".format(list(self.keymap_pause.keys())))

    def conf_up(self):
        if self.confidence_level == 1:
            print("Confidence level is MAXIMUM.")
            return
        self.confidence_level = (int(self.confidence_level * 100) + int(self.CONF_STEP * 100)) / 100
        print("Confidence level up, now it is " + str(self.confidence_level))
        self.is_changed = True

    def conf_down(self):
        if self.confidence_level == self.CONF_STEP:
            print("Confidence level is MINIMUM.")
            return
        self.confidence_level = (int(self.confidence_level * 100) - int(self.CONF_STEP * 100)) / 100
        print("Confidence level up, now it is " + str(self.confidence_level))
        self.is_changed = True

    def save_settings(self):
        data = {
            "keymap_exit": self.keymap_exit,
            "keymap_pause": self.keymap_pause,
            "keymap_action": self.keymap_action,
            "keymap_compare": self.keymap_compare,
            "keymap_conf_up": self.keymap_conf_up,
            "keymap_conf_down": self.keymap_conf_down,
            "screenshot_region": self.screenshot_region,
            "compare_region": self.compare_region,
            "confidence_level": self.confidence_level,
        }

        with open(self.SETTINGS_PATH, 'w') as f:
            json.dump(data, f, indent=4)
