from dataclasses import dataclass
from typing import Tuple


@dataclass
class DetectorConfig:
    min_detection_confidence: float = 0.7
    min_tracking_confidence: float = 0.5
    circle_radius: int = 5
    circle_color: Tuple[int, int, int] = (255, 0, 0)
    text_color: Tuple[int, int, int] = (0, 255, 0)
