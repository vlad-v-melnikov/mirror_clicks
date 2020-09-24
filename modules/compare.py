import pyautogui

def compare_images():
    print("Comparing images...")
    pyautogui.screenshot('left.png', region=(30, 215, 920, 715))
    result = pyautogui.locateOnScreen('left.png', \
        region=(970, 110, 950, 980),\
        confidence=0.9)

    if result:
        print('Images match')
    else:
        print('IMAGES DO NOT MATCH')
