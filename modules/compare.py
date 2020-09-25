import pyautogui, os

def compare_images(screenshot_region, compare_region, confidence_level=0.95):
    print("Comparing images...")

    if not os.path.isdir('./screenshot'):
        os.mkdir('./screenshot')

    pyautogui.screenshot('screenshot\\left.png', region=screenshot_region)
    result = pyautogui.locateOnScreen('screenshot\\left.png', \
        region=compare_region,\
        confidence=confidence_level)

    if result:
        print('Images match')
    else:
        print('IMAGES DO NOT MATCH')
