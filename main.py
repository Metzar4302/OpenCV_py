from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys
import numpy as np
import pyautogui as pg
import imutils
import cv2 as cv2
import time
import pymsgbox as msg

def main():
    #? Recomment for testing
    tests()





def tests():
    # ! Basic image test
    # Нам надо сохранить соотношение сторон
    # чтобы изображение не исказилось при уменьшении
    # для этого считаем коэф. уменьшения стороны
    final_wide = 200
    image_cat = cv2.imread("Img/cat.jpg")
    r = float(final_wide) / image_cat.shape[1]
    dim = (final_wide, int(image_cat.shape[0] * r))
    
    lensImgPath = "Img/gitlens.png"

    #? resize
    image = resize(image_cat, dim)
    cv2.imshow("Picture", image)

    #? recolor to gray
    image = toGray(image)
    cv2.imshow("Recolor", image)
    
    # ! Screenshot test
    # shotTest()

    #! Searching on screen
    #? Find of position
    position = findOnScreen(lensImgPath)
    print(position)

    #? Click to find image
    clickToFImg(lensImgPath)

    #! Create new file
    createNewFile()

    #! Calculate
    calcUse()

    #! Message box function testing
    messageTest()

    #! Grayscale edge testing
    grayscaleTest()

def resize(image, dim):
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

def toGray(image):
    recolored = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return recolored

def shotTest():
    image = pg.screenshot(region=(0,0, 300, 400))
    cv2.imshow("Title here", cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY))

def findOnScreen(image):
    return pg.locateOnScreen(image)

def clickToFImg(image_path):
    (pos_x, pos_y) = pg.locateCenterOnScreen(image_path)
    pg.click(pos_x, pos_y)

def createNewFile():
    pg.click(pg.locateCenterOnScreen('Img\\files_viewer.png', grayscale = True, confidence=0.9))
    pg.moveTo(pg.locateCenterOnScreen('Img\\workspace.png', grayscale = True, confidence=0.9))
    pg.click(pg.locateCenterOnScreen('Img\\new_file.png', grayscale = True, confidence=0.9))
    pg.typewrite("test_file.txt")
    pg.press("enter")
    pg.typewrite("Look on this shit!")

def calcUse():
    pg.press("win")
    pg.typewrite("Calculator")
    pg.press("enter")
    # pg.click(pg.locateCenterOnScreen('Img\\calc_icon.png', grayscale = True, confidence=0.9))
    time.sleep(1)   # Time for program start-lag
    #? use fake-mouse
    # pg.click(pg.locateCenterOnScreen('Img\\calc_1_btn.png', grayscale = True, confidence=0.9))
    # pg.click(pg.locateCenterOnScreen('Img\\calc_plus_btn.png', grayscale = True, confidence=0.9))
    # pg.click(pg.locateCenterOnScreen('Img\\calc_2_btn.png', grayscale = True, confidence=0.9))
    # pg.click(pg.locateCenterOnScreen('Img\\calc_equal_btn.png', grayscale = True, confidence=0.9))
    # pg.click(pg.locateCenterOnScreen('Img\\calc_minus_btn.png', grayscale = True, confidence=0.9))
    # pg.click(pg.locateCenterOnScreen('Img\\calc_1_btn.png', grayscale = True, confidence=0.9))
    # pg.click(pg.locateCenterOnScreen('Img\\calc_equal_btn.png', grayscale = True, confidence=0.9))
    #? use fake-keyboard
    pg.typewrite("1+5=")

def messageTest():
    if msg.confirm(text='CONFIRM_TEXT', title='CONFIRM_TITLE', buttons=['OK', 'Cancel']) == 'OK':
        msg.alert(text='u r pressed OK', title='ALERT_TITLE', button='OK')
    else:
        msg.alert(text='u r pressed CANCEL', title='ALERT_TITLE', button='OK')
    msg.password(text='', title='', default='', mask='*')

def grayscaleTest():
    enot = cv2.imread("Img\\enot.jpg")
    # cv2.imshow("Original", enot)

    new_height = 300
    k = new_height / enot.shape[1]
    new_sizes = (new_height, int(enot.shape[0] * k))

    enot = cv2.resize(enot, new_sizes, interpolation=cv2.INTER_AREA)
    # cv2.imshow("New size", enot)

    enot_gray = cv2.cvtColor(enot, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Grayscale", enot_gray)

    enot_gauss = cv2.GaussianBlur(enot_gray, (7, 7), 1.5)
    # cv2.imshow("Gauss", enot_gauss)

    enot_edges = cv2.Canny(enot_gauss, 0, 50)
    # cv2.imshow("Edges", enot_edges)

    enot_invers = cv2.bitwise_not(enot_edges)
    cv2.imshow("Invers", enot_invers)
    
    enot_cartoon_gray = cv2.bitwise_and(enot_gray, enot_edges, enot)
    cv2.imshow("Cartoon", enot_cartoon_gray)
    print(enot_cartoon_gray.shape)

#! Start
if __name__ == '__main__':
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()