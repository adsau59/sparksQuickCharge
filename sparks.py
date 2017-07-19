import pynput.mouse as m
import pynput.keyboard as k
import time
from threading import Timer
import easygui


mouse = m.Controller()

value = easygui.enterbox(title="Hold Time", msg="Hold time?", default="0.375")
secs = float(value)


def click():
    mouse.press(m.Button.left)
    Timer(secs, mouse.release, [m.Button.left]).start()


def on_click(x, y, button, pressed):
    if button == m.Button.middle:
        if pressed:
            click()

print("Started...")
with m.Listener(on_click=on_click) as listener:
    listener.join()
