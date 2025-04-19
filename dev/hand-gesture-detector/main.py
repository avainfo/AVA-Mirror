import logging

from config.hand_detector_config import DetectorConfig
from detection.hand_detector import HandDetector


def run():
    config = DetectorConfig(
        min_detection_confidence=0.6,
        min_tracking_confidence=0.3,
        circle_radius=8,
        circle_color=(255, 0, 0),
        text_color=(255, 255, 255)
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    detector = HandDetector(config)
    detector.run(cam_index=0)


if __name__ == "__main__":
    run()
