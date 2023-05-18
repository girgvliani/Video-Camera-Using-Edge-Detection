import numpy as np
import cv2 as cv
import time
from canny import *


t_start = 0
t_end = 0
cap = cv.VideoCapture('1.mp4')
lastframe = 0
trigger = 0

if (cap.isOpened() == False):
    print("Error opening video stream or file")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        green = (0, 255, 0)

        canny = cv.Canny(frame, 100, 200)#I know it is built in canny but it gave me the best results
        #canny = canny(frame) #this is my version of canny detection it works
        #  but it is slow and this code has some errors with my canny


        cv.line(frame, (430, 300), (605, 225), green, 5)
        cv.line(frame, (300, 200), (470, 160), green, 5)
        cv.line(frame, (820, 230), (1000, 370), green, 5)
        cv.line(frame, (1025, 160), (1200, 230), green, 5)

        cv.imshow('Frame', frame)
        cv.imshow('canny', canny)

        image_change = np.abs(canny - lastframe)
        cv.imshow('difference', image_change)

        if image_change[260, 515] == 255 and trigger == 1:
            # print("point 2")
            dis1 = 6  # distance can be changed according to the real distance
            # my distance data is not correct but is close
            trigger = 2
            t_end = time.perf_counter()
            print(f'end time: {t_end}')
            t_delta = t_end-t_start
            print(t_delta)
            avgSpeed = (dis1/(t_delta))*18/5
            print(f'speed = {avgSpeed}')
            t_start = 0
            t_end = 0

        if image_change[180, 385] == 255 and trigger == 0:
            # print("point 1")
            trigger = 1

            t_start = time.perf_counter()
            print(f'start time: {t_start}')

        if image_change[320, 910] == 255 and trigger == 2:
            # print("point 3")
            trigger = 3
            t_start = time.perf_counter()
            print(f'start time: {t_start}')

        if image_change[195, 1087] == 255 and trigger == 3:
            # print("point 4")
            dis2 = 4.5  # distance can be changed according to the real distance
            # my distance data is not correct but is close
            trigger = 0
            t_end = time.perf_counter()
            print(f'end time: {t_end}')
            t_delta = t_end-t_start
            print(t_delta)
            avgSpeed = (dis2/(t_delta))*18/5
            print(f'speed = {avgSpeed}')
            t_start = 0

        if image_change[190, 350] == 255 and trigger == -3:
            print("point rev 3")

            t_start = time.perf_counter()
            print(f'start time: {t_start}')

        if image_change[280, 460] == 255 and trigger == -2:
            trigger = -3
            print("point rev 2")
            dis1 = 6  # distance can be changed according to the real distance
            # my distance data is not correct but is close

            t_end = time.perf_counter()
            print(f'end time: {t_end}')
            t_delta = t_end-t_start
            print(t_delta)
            avgSpeed = (dis1/(t_delta))*18/5
            print(f'speed = {avgSpeed}')
            t_start = 0
            t_end = 0

        if image_change[250, 850] == 255 and trigger == -1:
            # print("point 3")
            dis2 = 4.5  # distance can be changed according to the real distance
            # my distance data is not correct but is close
            trigger = -2
            t_end = time.perf_counter()
            print(f'end time: {t_end}')
            t_delta = t_end-t_start
            print(t_delta)
            avgSpeed = (dis2/(t_delta))*18/5
            print(f'speed = {avgSpeed}')
            t_start = 0

        if image_change[180, 1020] == 255 and trigger == 0:
            t_start = time.perf_counter()
            print(f'start time: {t_start}')
            trigger = -1

        lastframe = canny

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()
