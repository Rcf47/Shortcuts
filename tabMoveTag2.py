# Enter script code
import time

keyboard.send_keys("<ctrl>+l")
time.sleep(0.1)
keyboard.send_keys("<ctrl>+c")
time.sleep(0.1)
keyboard.send_keys("<ctrl>+w")
time.sleep(0.1)
keyboard.send_keys("<ctrl>+n")
time.sleep(0.1)
keyboard.send_keys("<ctrl>+v")
time.sleep(0.1)
keyboard.send_keys("<enter>")
time.sleep(0.1)
engine.run_script("moveToTag2")
time.sleep(0.1)
engine.run_script("switchToTag2")
time.sleep(0.1)
engine.run_script("superM")
time.sleep(0.4)
engine.run_script("superK")

# time.sleep(0.4)
# engine.run_script("masterWindow")
# time.sleep(0.1)
# keyboard.press_key("<super>")
# keyboard.press_key("<f3>")
# time.sleep(0.1)
# keyboard.release_key("<f3>")
# keyboard.release_key("<super>")
