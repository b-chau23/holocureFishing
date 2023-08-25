import time
import pyautogui as auto
from threading import Timer
from mss import mss


def fish(search):
    print("Start")
    spot = {'left': search[0], 'top': search[1], 'width': search[2], 'height': search[3]}
    with mss() as sct:
        while True:
            pixel = sct.grab(spot)
            pixels = [pixel.pixel(i, 0) for i in range(10)]

            for px in pixels:
                if px in ARROW_COLORS:
                    press_button(ARROW_COLORS[px])
                    break


def set_up():
    search = None
    while not search:
        try:
            x, y = auto.locateCenterOnScreen("frame.png", confidence=0.7)
            search = (x - 20, y, 10, 1)
        except TypeError:
            continue
    fish(search)


def press_button(action):
    global reset
    if reset.is_alive():
        reset.cancel()
    reset = Timer(2.0, recast_rod)
    reset.start()

    # I know press() exists but it only works with the sleep
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
    ARROW_COLORS = {
        (45, 235, 43): 'd',
        (245, 197, 67): 'a',
        (52, 144, 246): 's',
        (225, 50, 50): 'w',
        (174, 49, 208): 'space'
    }
    start, stop = time.time(), time.time()
    # initialize a global variable for press_button
    # also just so happens to start the program
    reset = Timer(0.0, set_up)
    reset.start()
