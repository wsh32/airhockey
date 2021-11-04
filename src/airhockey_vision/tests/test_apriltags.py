from airhockey_vision.apriltag_node import ApriltagDetector

from unittest import TestCase
import pytest

import cv2
import os
import yaml


config_path = os.path.join(os.path.dirname(__file__), "..", "config")
apriltag_config = os.path.join(config_path, "apriltag_16h5.yaml")
apriltag_config_data = yaml.load(open(apriltag_config, 'r'), Loader=yaml.Loader)

test_image_filename = "test_img.jpg"
test_image = os.path.join(os.path.dirname(__file__), test_image_filename)


class TestApriltags(TestCase):
    def config_file_has_values(self, config_file):
        assert 'apriltag' in config_file
        assert 'tag_family' in config_file['apriltag']

    def test_apriltag_config_has_values(self):
        self.config_file_has_values(apriltag_config_data)

    def test_apriltag_detections_test_image(self):
        apriltag_detector = ApriltagDetector(
            apriltag_config_data['apriltag']['tag_family'])

        image = cv2.imread(test_image)
        detections = apriltag_detector.detect_tags(image)

        assert len(detections) > 0

