import cv2
import numpy as np
from util import get_limits
from util1 import get_limits1

def shape(image_mask,img):
    contours, _ = cv2.findContours(image_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    largest_contour = contours[0]
    epsilon = 0.03*cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)
    cv2.drawContours(img, largest_contour, 0, (0, 0, 0), 4)
   
    if len(approx) == 3:
        return 'triangle'
    elif len(approx) == 4:
        return 'quadrilateral'
    else:
        return 'circle'
    
def clr(color,path):
    img = cv2.imread(path)
    # img = cv2.resize(img,(720,480))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    if color == [0,0,255] or color == [255, 0, 0] :
        lowerLimit, upperLimit = get_limits1(color)
    elif color == [0,255,0]:
        lowerLimit, upperLimit = get_limits(color)
    elif color == [255,255,255]:
        lowerLimit = np.array([0, 0, 0])
        upperLimit = np.array([190, 190, 190])

    image_mask = cv2.inRange(hsv, lowerLimit, upperLimit)
    x = cv2.countNonZero(image_mask);

    return x,image_mask,img

def compare(x1,x2,x3):
    if x3 <x1 > x2:
        return "Green"

    elif x1 < x2 > x3:
        return "Blue"

    elif x2<x3>x1:
        return "Red"

def main(i):
    print("This is for image ", i )
    path = f"A:/Shape and color detection/{i}.jpg"
    a,b,c,d,e,f = 0,0,0,0,0,0
    green = [0,255,0]
    blue = [255,0,0]
    red = [0,0,255]
    white = [255,255,255]

    x1,image_mask,img = clr(green,path)
    # x1 = 0 #conveyor green problem (remove if object not on conveyor)
    
    x2,image_mask1,img = clr(blue,path)
   
    x3,image_mask2,img = clr(red,path)
    
    x4 = clr(white,path)
    
    if compare(x1,x2,x3) == 'Green':
        shp = shape(image_mask,img)
        print("Green")
        a = 1
    elif compare(x1,x2,x3) == 'Blue':
        shp = shape(image_mask1,img)
        print("Blue")
        b = 1
    elif compare(x1,x2,x3) == 'Red':
        shp = shape(image_mask2,img)
        print("Red")
        c = 1

    if shp == 'triangle':
        print('Triangle')
        d = 1
    elif shp ==  'quadrilateral':
        print('quad')
        e = 1
    elif shp ==  'circle':
        print('circle')
        f = 1
    
    print("a= ",a," b=",b," c=",c," d=",d," e=",e," f=",f)
    print()
    print()

if __name__ == "__main__":
    for i in range (1,9):
        main(i) 