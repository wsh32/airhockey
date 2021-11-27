from airhockey_vision.homography_node import Tag, TableLocalizer

from unittest import TestCase
import pytest

import os
import yaml
import numpy as np


config_path = os.path.join(os.path.dirname(__file__), "..", "config")
default_tag_location_config = os.path.join(config_path,
                                           "default_table.yaml")
default_config_data = yaml.load(open(default_tag_location_config, 'r'),
                                Loader=yaml.Loader)

all_tag_location_config = os.path.join(config_path,
                                       "table_setup_all_tags.yaml")
all_config_data = yaml.load(open(all_tag_location_config, 'r'),
                            Loader=yaml.Loader)

black_tag_location_config = os.path.join(config_path,
                                         "table_setup_black_tags.yaml")
black_config_data = yaml.load(open(black_tag_location_config, 'r'),
                              Loader=yaml.Loader)

white_tag_location_config = os.path.join(config_path,
                                         "table_setup_white_tags.yaml")
white_config_data = yaml.load(open(white_tag_location_config, 'r'),
                              Loader=yaml.Loader)


class TestHomography(TestCase):
    def config_file_has_values(self, config_file):
        assert 'tag_locations' in config_file
        assert len(config_file['tag_locations']) >= 4

    def assert_close_2d(self, point1, point2, dist=0.01):
        assert np.linalg.norm(np.array([point1[0], point1[1]]) -
                              np.array([point2[0], point2[1]])) < dist

    def test_default_config_has_values(self):
        self.config_file_has_values(default_config_data)

    def test_all_config_has_values(self):
        self.config_file_has_values(all_config_data)

    def test_black_config_has_values(self):
        self.config_file_has_values(black_config_data)

    def test_white_config_has_values(self):
        self.config_file_has_values(white_config_data)

    def test_homography_scale(self):
        tag_locations_start = {
            "tag16h5_0": [0, 0],
            "tag16h5_1": [0, 100],
            "tag16h5_2": [50, 100],
            "tag16h5_3": [50, 0],
        }

        tag_locations_final = {
            "tag16h5_0": [0, 0],
            "tag16h5_1": [0, 10],
            "tag16h5_2": [10, 10],
            "tag16h5_3": [10, 0],
        }

        tags = {}
        for i in tag_locations_final.keys():
            tags[i] = Tag(i, np.array(tag_locations_final[i]))

        localizer = TableLocalizer(tags)
        localizer.update_tag_camera_positions(tag_locations_start)

        test_pos = (25, 50)
        test_pos_expected = (5, 5)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

        test_pos = (0, 0)
        test_pos_expected = (0, 0)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

        test_pos = (50, 100)
        test_pos_expected = (10, 10)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

        test_pos = (100, 200)
        test_pos_expected = (20, 20)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

    def test_homography_translate(self):
        tag_locations_start = {
            "tag16h5_0": [0, 0],
            "tag16h5_1": [0, 10],
            "tag16h5_2": [10, 10],
            "tag16h5_3": [10, 0],
        }

        tag_locations_final = {
            "tag16h5_0": [1, 1],
            "tag16h5_1": [1, 11],
            "tag16h5_2": [11, 11],
            "tag16h5_3": [11, 1],
        }

        tags = {}
        for i in tag_locations_final.keys():
            tags[i] = Tag(i, np.array(tag_locations_final[i]))

        localizer = TableLocalizer(tags)
        localizer.update_tag_camera_positions(tag_locations_start)

        test_pos = (5, 5)
        test_pos_expected = (6, 6)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

    def test_homography_rotate(self):
        tag_locations_start = {
            "tag16h5_0": [0, 0],
            "tag16h5_1": [0, 10],
            "tag16h5_2": [10, 10],
            "tag16h5_3": [10, 0],
        }

        tag_locations_final = {
            "tag16h5_0": [0, 10],
            "tag16h5_1": [10, 10],
            "tag16h5_2": [10, 0],
            "tag16h5_3": [0, 0],
        }

        tags = {}
        for i in tag_locations_final.keys():
            tags[i] = Tag(i, np.array(tag_locations_final[i]))

        localizer = TableLocalizer(tags)
        localizer.update_tag_camera_positions(tag_locations_start)

        test_pos = (5, 5)
        test_pos_expected = (5, 5)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

        test_pos = (2, 2)
        test_pos_expected = (2, 8)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected)
        test_pos_inv = localizer.get_camera_position_from_table(
            *test_pos_expected)
        self.assert_close_2d(test_pos_inv, test_pos)

    def test_homography_real(self):
        tag_locations_camera = {
            "tag16h5_0": [1138, 618],
            "tag16h5_2": [164, 198],
            "tag16h5_3": [165, 616],
            "tag16h5_9": [663, 194],
        }

        tag_locations_table = {
            "tag16h5_0": [2, 2],
            "tag16h5_2": [33.75, 75.25],
            "tag16h5_3": [2, 75.25],
            "tag16h5_9": [33.75, 35],
        }

        tags = {}
        for i in tag_locations_table.keys():
            tags[i] = Tag(i, np.array(tag_locations_table[i]))

        localizer = TableLocalizer(tags)
        localizer.update_tag_camera_positions(tag_locations_camera)

        test_pos = (355, 408)
        test_pos_expected = (18, 65)
        test_pos_out = localizer.get_table_position_from_camera(*test_pos)
        self.assert_close_2d(test_pos_out, test_pos_expected, dist=1)


if __name__ == '__main__':
    t = TestHomography()
    t.test_homography_real()

