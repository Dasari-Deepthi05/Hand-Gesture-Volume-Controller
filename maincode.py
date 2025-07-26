import cv2
import pyautogui
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

last_action_time = 0
cooldown_period = 1  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for mirror view
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    hand_gesture = 'No Hand Detected'

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            if index_finger_y < thumb_y - 0.02:  # Add small margin to reduce flicker
                hand_gesture = 'Volume Up'
            elif index_finger_y > thumb_y + 0.02:
                hand_gesture = 'Volume Down'
            else:
                hand_gesture = 'Neutral'

            current_time = time.time()
            if current_time - last_action_time > cooldown_period:
                if hand_gesture == 'Volume Up':
                    pyautogui.press('volumeup')
                    last_action_time = current_time
                elif hand_gesture == 'Volume Down':
                    pyautogui.press('volumedown')
                    last_action_time = current_time

    cv2.putText(frame, hand_gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Hand Gesture Volume Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
