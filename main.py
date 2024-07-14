import pynput
import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delayRightClick = 4
rightClick = Button.right
delayLeftClick = 0.5
leftClick = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread1 = ClickMouse(delayLeftClick, leftClick)
click_thread2 = ClickMouse(delayRightClick, rightClick)
click_thread1.start()
click_thread2.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread1.running:
            click_thread1.stop_clicking()
        else:
            click_thread1.start_clicking()
        if click_thread2.running:
            click_thread2.stop_clicking()
        else:
            click_thread2.start_clicking()
    elif key == stop_key:
        click_thread1.exit()
        click_thread2.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()