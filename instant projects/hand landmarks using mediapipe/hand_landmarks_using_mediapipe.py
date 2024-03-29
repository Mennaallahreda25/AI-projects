# -*- coding: utf-8 -*-
"""Hand landmarks using mediapipe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18COTMZ9WRlexyCOFuaW5fTHG4Feh7zyS
"""

import cv2
import time
import mediapipe as mp

result = cv2.VideoWriter('handlandmarks.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (640, 480))
cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(static_image_mode=False)
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    ret, img = cap.read()
    if not ret:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for idd, lm in enumerate(handlms.landmark):
                print(idd, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(idd, cx, cy)
                if idd == 0:
                    cv2.circle(img, (cx, cy), 9, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (15, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    result.write(img)
    cv2.imshow("frame", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

