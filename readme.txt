How to use Mirror Clicks.

You need to have windows for TEST and PROD arranged side by side on one screen. They need to be perfectly aligned, so use Win-LEFT and Win-RIGHT keys to arrange them.
For now, this script is purely command line, but it will be developed into a GUI-based app in the future.

This Python script simplifies regression testing by solving two issues:
- Clicking in both windows on the same links (no need to remember links you clicked on or two move the mouse yourself from left to right and back).
- Comparing images in two windows and resolving if they match or not (remember to enter settings into settings.json)

1. Setting up:

The script can compare images on the left and right sides of the screen and conclude if they are different or the same. Useful for comparing complex images like charts and maps.
For this function to work, you need to set up the dimensions of areas to be compared.
You will need two things: mouse_pos.py script and settings.json (the latter is in "modules/" folder).

In settings.json find screenshot_region and compare_region settings. They have 4 values:
- x of top left corner
- y of top left corner
- area width
- area height

screenshot_region is the "source" area for comparison.
compare_region is the "target" area.

Arrange the windows where you will use the function side by side on one screen, find the values using "python mouse_pos.py" script (it only shows coordinates, so for now,  
calculate width and height yourself) and enter these values into settings.json. 
Make sure that the target area is bigger than the source area.

2. Regressive testing:

- Arrange the windows side by side on your screen. Preferably, the command window needs to be on the other screen so that you can see what's going on during the script execution.

- Start the script with this command: "python mirror_clicks.py"

- Aim the mouse pointer at a link in the LEFT window (for me, it is usually TEST, but it can be PROD). Do not click, unless you want to do something out of sync between the windows.

- Press the button associated with "keymap_action". Automatically, a click will happen in this position, then the mouse cursor moves to the right half of the screen, a click happens
in the same position and the cursor returns to the left window.

- Compare what you see and continue pressing the "action" button.

- When you open an image that needs to be compared between TEST and PROD (remember, they need to be alinged, and correct settings need to be in settings.json), 
press the button associated with "keymap_compare". The result of matching is printed in the console where the script is running.

- If you disagree with the comparison result, adjust "confidence level" with UP and DOWN arrows, with a step of 0.01. The maxmimum value is 1, the minimum is 0.01. Usually 1 does not make a match happen
no matter what you do, so the actual setting you should be using is 0.95. Do not go under 0.8, or it will match images that you can say` are different with a naked eye.
"Confidence level" establishes how much of the pixels have to be the same between two images.

- When you are going to finish, press ESC and the script will complete.