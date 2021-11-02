from airhockey_vision.puck_tracking_node import PuckTracker

from unittest import TestCase
import pytest

import cv2
import os
import yaml


config_path = os.path.join(os.path.dirname(__file__), "..", "config")
green_config = os.path.join(config_path, "detect_green.yaml")
green_config_data = yaml.load(open(green_config, 'r'), Loader=yaml.Loader)
blue_config = os.path.join(config_path, "detect_blue.yaml")
blue_config_data = yaml.load(open(blue_config, 'r'), Loader=yaml.Loader)

test_image_filename = "test_img.jpg"
test_image = os.path.join(os.path.dirname(__file__), test_image_filename)


class TestPuckTracker(TestCase):
    def config_file_has_values(self, config_file):
        assert 'puck_tracking' in config_file
        assert 'h_lower' in config_file['puck_tracking']
        assert 's_lower' in config_file['puck_tracking']
        assert 'v_lower' in config_file['puck_tracking']
        assert 'h_upper' in config_file['puck_tracking']
        assert 's_upper' in config_file['puck_tracking']
        assert 'v_upper' in config_file['puck_tracking']
        assert 'visualize_color_r' in config_file['puck_tracking']
        assert 'visualize_color_g' in config_file['puck_tracking']
        assert 'visualize_color_b' in config_file['puck_tracking']

    def test_green_config_file_has_all_values(self):
        self.config_file_has_values(green_config_data)

    def test_tracks_green(self):
        green_lower = (green_config_data['puck_tracking']['h_lower'],
                       green_config_data['puck_tracking']['s_lower'],
                       green_config_data['puck_tracking']['v_lower'])
        green_upper = (green_config_data['puck_tracking']['h_upper'],
                       green_config_data['puck_tracking']['s_upper'],
                       green_config_data['puck_tracking']['v_upper'])
        visualize_color = (
            green_config_data['puck_tracking']['visualize_color_r'],
            green_config_data['puck_tracking']['visualize_color_g'],
            green_config_data['puck_tracking']['visualize_color_b'])
        puck_tracker = PuckTracker(green_lower, green_upper, visualize_color)

        image = cv2.imread(test_image)
        x, y = puck_tracker.detect_puck(image)

        assert x == pytest.approx(355, 10)
        assert y == pytest.approx(455, 10)

    def test_tracks_blue(self):
        blue_lower = (blue_config_data['puck_tracking']['h_lower'],
                      blue_config_data['puck_tracking']['s_lower'],
                      blue_config_data['puck_tracking']['v_lower'])
        blue_upper = (blue_config_data['puck_tracking']['h_upper'],
                      blue_config_data['puck_tracking']['s_upper'],
                      blue_config_data['puck_tracking']['v_upper'])
        visualize_color = (
            blue_config_data['puck_tracking']['visualize_color_r'],
            blue_config_data['puck_tracking']['visualize_color_g'],
            blue_config_data['puck_tracking']['visualize_color_b'])
        puck_tracker = PuckTracker(blue_lower, blue_upper, visualize_color)

        image = cv2.imread(test_image)
        x, y = puck_tracker.detect_puck(image)

        assert x == pytest.approx(1088, 10)
        assert y == pytest.approx(613, 10)


if __name__ == '__main__':
    pytest.main()

