import logging

import cv2
import mediapipe as mp
import numpy as np

from config.hand_detector_config import DetectorConfig
from gesture.gestures import Gestures


class HandDetector:
    def __init__(self, config: DetectorConfig):
        """
        Initialize the HandDetector with the specified configuration.

        :param config: DetectorConfig instance containing detection and drawing settings.
        """
        self.config = config
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=config.min_detection_confidence,
            min_tracking_confidence=config.min_tracking_confidence
        )
        self.drawing = mp.solutions.drawing_utils

    def draw(self, frame, landmarks):
        """
        Draws keypoints and indices on the given frame based on detected hand landmarks.

        :param frame: The image frame to draw on (BGR format).
        :param landmarks: A list of hand landmark points to draw.
        """
        h, w, _ = frame.shape
        for idx, lm in enumerate(landmarks):
            x, y = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (x, y), self.config.circle_radius,
                       self.config.circle_color, cv2.FILLED)
            cv2.putText(frame, str(idx), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        self.config.text_color, 1)

    def process_frame(self, frame):
        """
        Processes a single frame to detect hands, draw landmarks, and check for gestures.

        :param frame: A single video frame (BGR format) to process.
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(np.ascontiguousarray(frame_rgb))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.drawing.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                self.draw(frame, hand_landmarks.landmark)

                Gestures.check(hand_landmarks)

    def run(self, cam_index=0):
        """
        Starts the hand detection loop using the given camera index.

        :param cam_index: Index of the camera to use (default is 0).
        """
        logging.info("Starting hand detection")
        cap = cv2.VideoCapture(cam_index)
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    logging.warning("Frame invalide")
                    continue
                frame = cv2.flip(frame, 1)
                self.process_frame(frame)
                cv2.imshow("Hand Detector", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
