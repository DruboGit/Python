from webcam import Webcam
import cv2

webcam = Webcam(src=0, w=640)
print (f"Frame size: {webcam.w} x {webcam.h}")

for frame in webcam:
    cv2.imshow('Webcam Frame', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Take screenshots
#Look for hands
#Interperate sign
#Type sign