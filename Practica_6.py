import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#Rango de colores seleccionados ------------------------  
    lower_color = np.array([30,150,50])
    upper_color = np.array([255,255,180])
#Mascara en donde se muestra----------------------------   
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame,frame, mask= mask)
#Enseñar la video en la pantalla ------------------------
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

