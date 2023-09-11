import pyautogui as auto
import time as t
rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
for i in range(50):
    auto.press("volumeup")
auto.press("win")
t.sleep(0.2)
auto.typewrite("google chrome")
auto.press("enter")
t.sleep(1)
auto.typewrite(rickroll)
auto.press("enter")
t.sleep(3)
auto.press("f")