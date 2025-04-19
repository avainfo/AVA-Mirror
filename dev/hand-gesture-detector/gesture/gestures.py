import logging
import math


class Gestures:
    @staticmethod
    def compute_angle(a, b) -> float:
        """
        Compute the orientation angle of the vector from point a to point b, in degrees.

        :param a: The base landmark (starting point of the vector)
        :type a: mediapipe.framework.formats.landmark_pb2.NormalizedLandmark
        :param b: The target landmark (end point of the vector)
        :type b: mediapipe.framework.formats.landmark_pb2.NormalizedLandmark
        :return: Angle in degrees between the vector AB and the vertical axis (rotated by +90° to align zero at top).
        :rtype: Float
        """
        ab = {"x": b.x - a.x, "y": b.y - a.y}
        return (math.atan2(ab["y"], ab["x"]) * 180 / math.pi) + 90

    @staticmethod
    def check(landmarks):
        """
        Check and log the hand's orientation angle and openness.

        :param landmarks: A list of landmarks for one detected hand.
        :type landmarks: mediapipe.framework.formats.landmark_pb2.NormalizedLandmarkList
        """
        base_position = Gestures.get_hand_angle(landmarks)
        is_up = Gestures.is_hand_open(landmarks)
        logging.info("Angles: {}deg | right: {}".format(base_position, is_up))

    @staticmethod
    def is_hand_open(landmarks):
        """
        Determine if the hand is in an open (upright) position based on its angle.

        :param landmarks: A list of landmarks for one detected hand.
        :type landmarks: mediapipe.framework.formats.landmark_pb2.NormalizedLandmarkList
        :return: True if the hand angle is approximately upright, False otherwise.
        :rtype: Bool
        """
        return -5 <= Gestures.get_hand_angle(landmarks) <= 15

    @staticmethod
    def get_hand_angle(landmarks):
        """
        Calculate the average orientation angle of the hand using wrist-to-index and wrist-to-pinky vectors.

        :param landmarks: A list of landmarks for one detected hand.
        :type landmarks: mediapipe.framework.formats.landmark_pb2.NormalizedLandmarkList
        :return: The average angle of the hand in degrees.
        :rtype: Float
        """
        angle_wrist_index = Gestures.compute_angle(
            landmarks.landmark[0],
            landmarks.landmark[5]
        )
        angle_wrist_pinky = Gestures.compute_angle(
            landmarks.landmark[0],
            landmarks.landmark[17]
        )

        return (angle_wrist_index + angle_wrist_pinky) / 2
