import pyautogui as pag
import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        x, y = pag.position()
        posStr = 'x: ' + str(x).rjust(4) + ', y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        posStr += ', RGB: (' \
            + str(pixelColor[0]).rjust(3) + ', ' \
            + str(pixelColor[1]).rjust(3) + ', '\
            + str(pixelColor[2]).rjust(3) + ')'
        print(posStr, end='')
        print('\b' * len(posStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')
