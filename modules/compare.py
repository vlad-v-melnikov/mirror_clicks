import pyautogui

def compare_images(screenshot_region=(30, 215, 920, 715), compare_region=(970, 110, 950, 980), confidence_level=0.9):
    print("Comparing images...")
    pyautogui.screenshot('screenshot\\left.png', region=screenshot_region)
    result = pyautogui.locateOnScreen('screenshot\\left.png', \
        region=compare_region,\
        confidence=confidence_level)

    if result:
        print('Images match')
    else:
        print('IMAGES DO NOT MATCH')
