import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6
)

def detect_hand(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        return result.multi_hand_landmarks[0]
    return None


def classify_sign(hand_landmarks):
    thumb = hand_landmarks.landmark[4].y
    index = hand_landmarks.landmark[8].y
    middle = hand_landmarks.landmark[12].y

    if index < middle:
        return "HELLO"
    if thumb < index:
        return "YES"
    return "UNKNOWN"
