import cv2
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

mp_hands = hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

def detect_sign(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(
                frame,
                hand_landmarks,
                hands.HAND_CONNECTIONS
            )
        return "HAND DETECTED"

    return None
