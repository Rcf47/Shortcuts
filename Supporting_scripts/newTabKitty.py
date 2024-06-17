# Enter script code
import time

keyboard.press_key("<ctrl>")
keyboard.press_key("<shift>")
keyboard.press_key("t")
time.sleep(0.1)
keyboard.release_key("<ctrl>")
keyboard.release_key("<shift>")
keyboard.release_key("t")