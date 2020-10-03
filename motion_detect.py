#Detect Motion 
import cv2
cap = cv2.VideoCapture(0)
motion = cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame = cap.read()
    mask = motion.apply(frame)
    cv2.imshow('og', frame)
    cv2.imshow('change', mask)
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()