# добавим необходимый пакет с opencv
import numpy as np
import pyautogui as pg
import imutils
import cv2
import time
import pymsgbox as msg

# ! Basic image test
# Нам надо сохранить соотношение сторон
# чтобы изображение не исказилось при уменьшении
# для этого считаем коэф. уменьшения стороны
# final_wide = 200
# image_matrix = cv2.imread("matrix.jpg")
# r = float(final_wide) / image_matrix.shape[1]
# dim = (final_wide, int(image_matrix.shape[0] * r))

#? resize
# resized = cv2.resize(image_matrix, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Nigga", resized)

#? recolor to gray
# recolored = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Recolor", recolored)

#! Screenshot test
# image = pg.screenshot(region=(0,0, 300, 400))
# cv2.imshow("Title here", cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY))

#! Searching on screen
#? Find of position
# position = pg.locateOnScreen(img)
# print(position)

#! Click to debug
# (pos_x, pos_y) = pg.locateCenterOnScreen('debug_img.png')
# pg.click(pos_x, pos_y)


#! Create new file
# pg.click(pg.locateCenterOnScreen('Img\\files_viewer.png', grayscale = True, confidence=0.9))
# pg.moveTo(pg.locateCenterOnScreen('Img\\workspace.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\new_file.png', grayscale = True, confidence=0.9))
# pg.typewrite("test_file.txt")
# pg.press("enter")
# pg.typewrite("Look on this shit!")


#! Calculate
# pg.press("win")
# pg.typewrite("Calculator")
# pg.press("enter")
# # pg.click(pg.locateCenterOnScreen('Img\\calc_icon.png', grayscale = True, confidence=0.9))
# time.sleep(1)   # Time for program start-lag
# pg.click(pg.locateCenterOnScreen('Img\\calc_1_btn.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\calc_plus_btn.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\calc_2_btn.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\calc_equal_btn.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\calc_minus_btn.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\calc_1_btn.png', grayscale = True, confidence=0.9))
# pg.click(pg.locateCenterOnScreen('Img\\calc_equal_btn.png', grayscale = True, confidence=0.9))
# pg.typewrite("1+5=")
# pg.press("enter")


#! Message box function testing
# if msg.confirm(text='CONFIRM_TEXT', title='CONFIRM_TITLE', buttons=['OK', 'Cancel']) == 'OK':
#     msg.alert(text='u r pressed OK', title='ALERT_TITLE', button='OK')
# else:
#     msg.alert(text='u r pressed CANCEL', title='ALERT_TITLE', button='OK')
# msg.password(text='', title='', default='', mask='*')


#! Grayscale edge testing
# enot = cv2.imread("Img\\enot.jpg")
# # cv2.imshow("Original", enot)

# new_height = 300
# k = new_height / enot.shape[1]
# new_sizes = (new_height, int(enot.shape[0] * k))

# enot = cv2.resize(enot, new_sizes, interpolation=cv2.INTER_AREA)
# # cv2.imshow("New size", enot)

# enot_gray = cv2.cvtColor(enot, cv2.COLOR_BGR2GRAY)
# # cv2.imshow("Grayscale", enot_gray)

# enot_gauss = cv2.GaussianBlur(enot_gray, (7, 7), 1.5)
# # cv2.imshow("Gauss", enot_gauss)

# enot_edges = cv2.Canny(enot_gauss, 0, 50)
# # cv2.imshow("Edges", enot_edges)

# enot_invers = cv2.bitwise_not(enot_edges)
# # cv2.imshow("Invers", enot_invers)


# #! !!!!!!! HERE !!!!!!
# enot_cartoon_gray = cv2.bitwise_and(enot_gray, enot_edges, enot)
# cv2.imshow("Cartoon", enot_cartoon_gray)
# print(enot_cartoon_gray.shape)


# cv2.waitKey(0)
# cv2.destroyAllWindows()


#! Design test

