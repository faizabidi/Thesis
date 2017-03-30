# https://pypi.python.org/pypi/pynput

from pynput.mouse import Button, Controller

mouse = Controller()

mouse.position = (572,34)
mouse.press(Button.left)
mouse.move(2911,29)
mouse.release(Button.left)
mouse.position = (2911,29)
