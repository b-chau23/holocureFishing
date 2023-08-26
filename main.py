import time
import pyautogui as auto
from threading import Timer
from mss import mss


def fish(search):
    print("Start!")
    spot = {'left': search[0], 'top': search[1], 'width': search[2], 'height': search[3]}
    with mss() as sct:
        while True:
            # Constantly screenshot 10 pixels in the frame/fishing zone
            pixel = sct.grab(spot)
            pixels = [pixel.pixel(i, 0) for i in range(10)]
            # Perform the associated action depending on what colour was detected
            for px in pixels:
                if px in ARROW_COLORS:
                    press_button(ARROW_COLORS[px])
                    break


def set_up():
    print("Ready!")
    search = None
    while not search:
        try:
            # Identify center of frame and offset the x by 20 to act as a buffer zone
            # give an additinal 10 pixels in width as extra buffer
            x, y = auto.locateCenterOnScreen("frame.png", confidence=0.7)
            search = (x - 20, y, 10, 1)
        except TypeError:
            continue
    fish(search)


def press_button(action):
    # Hey it's that global variable from if __name__ == "__main__"
    global reset
    # Cancel the existing thread if it is alive
    if reset.is_alive():
        reset.cancel()
    # If 2 seconds pass without a button press, assume fishing has been completed
    # and recast the rod
    reset = Timer(2.0, recast_rod)
    reset.start()

    # I know press() exists but the sleep is necessary for functionality
    auto.keyDown(action)
    time.sleep(0.1)
    auto.keyUp(action)


def recast_rod():
    for i in range(2):
        auto.keyDown('space')
        time.sleep(0.3)
        auto.keyUp('space')
        time.sleep(0.3)


if __name__ == "__main__":
    # Dictionary for colors and their associated actions
    ARROW_COLORS = {
        (45, 235, 43): 'd',
        (245, 197, 67): 'a',
        (52, 144, 246): 's',
        (225, 50, 50): 'w',
        (174, 49, 208): 'space'
    }
    # initialize a global variable for press_button
    # also just so happens to start the program
    reset = Timer(0.0, set_up)
    reset.start()
