import pyautogui as auto
import time as t
auto.press("win")
auto.typewrite("paint")
auto.press("enter")
t.sleep(1)
auto.moveTo(x=325, y=575)
auto.dragRel(xOffset=-100)
auto.dragRel(yOffset=100)
auto.dragRel(xOffset=100)
auto.dragRel(yOffset=-100)
auto.moveTo(x=335, y=575)
auto.dragRel(yOffset=100)
auto.dragRel(xOffset=100)
auto.dragRel(yOffset=-100)
auto.dragRel(xOffset=-100)
auto.moveRel(xOffset=50, yOffset=0)
auto.dragRel(yOffset=-250)
auto.dragRel(xOffset=-110)
auto.dragRel(yOffset=250)
auto.moveRel(yOffset=-200, xOffset=0)
auto.dragRel(xOffset=110, yOffset=0)
auto.moveRel(xOffset=-55, yOffset=-50)
auto.dragRel(yOffset=25)