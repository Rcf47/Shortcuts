# Enter script code
import time

keyboard.press_key("<super>")
#keyboard.press_key("<ctrl>")
keyboard.press_key("<enter>")
time.sleep(0.1)
keyboard.release_key("<enter>")
keyboard.release_key("<super>")
#keyboard.release_key("<ctrl>")