import cv2
import numpy as np

ecke1=[]
ecke2=[]
def on_click(event, x, y, p1, p2):
    global ecke1,ecke2
    if event == cv2.EVENT_LBUTTONDOWN:
        ecke1=[x,y]
        print(ecke1)
    if event == cv2.EVENT_LBUTTONUP:  
        ecke2=[x,y]
        print(ecke2)
        cropped_image = img[ecke1[0]:ecke2[1], ecke1[0]:ecke2[1]]
        print(cropped_image)
        cv2.imshow("cropped", cropped_image)



def on_change(value):
    print(value)
img = cv2.imread("C:/Users/Mohamed Chebaane/Desktop/Dokumente Mohamed/MS/Lena.bmp")
cv2.imshow("LENA", img)
cv2.namedWindow('LENA')
cv2.setMouseCallback('LENA', on_click)
cv2.createTrackbar('slider', "LENA", 1, 4, on_change)


cv2.waitKey(0)

cv2.destroyAllWindows()
