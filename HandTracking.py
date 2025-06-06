import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print (id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,
                            mpDraw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=1),
                            mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1))

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    cv2.imshow("Volume ~ Dawid", img)
    cv2.waitKey(1)


