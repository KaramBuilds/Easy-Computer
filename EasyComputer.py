import cv2
import mediapipe as mp
import math
import numpy as np
import time
import pyautogui
from pycaw.pycaw import AudioUtilities
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os

model_path = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")
base_options = python.BaseOptions(model_asset_path=model_path)

cap = cv2.VideoCapture(0)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
detector = vision.HandLandmarker.create_from_options(options)

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

last_action = 0

while True:
    success, frame = cap.read()
    if not success:
        continue
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    result = detector.detect(mp_image)
    if result.hand_landmarks:
        hand = result.hand_landmarks[ 0 ]
        thumb = hand[ 4 ]
        index = hand[ 8 ]

        index_up = hand[ 8 ].y < hand[ 6 ].y
        middle_up = hand[ 12 ].y < hand[ 10 ].y
        ring_up = hand[ 16 ].y < hand[ 14 ].y
        pinky_up = hand[ 20 ].y < hand[ 18 ].y

        if index_up and not middle_up and not ring_up and not pinky_up:
            dist = math.hypot(index.x - thumb.x, index.y - thumb.y)
            vol_level = np.interp(dist, [0.03, 0.22], [0.0, 1.0])
            volume.SetMasterVolumeLevelScalar(float(vol_level), None)

        if (time.time() - last_action) > 2.0:
            if not index_up and not middle_up and not ring_up and not pinky_up:
                pyautogui.press('playpause')
                last_action = time.time()
                print("Play / Pause")
            elif index_up and middle_up and not ring_up and not pinky_up:
                pyautogui.hotkey('shift', 'n')
                last_action = time.time()
                print("Next Video")
            elif index_up and middle_up and ring_up and not pinky_up:
                pyautogui.hotkey('shift', 'p')
                last_action = time.time()
                print("Previous Video")

    cv2.imshow("Gesture Controlled Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
