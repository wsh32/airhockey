from airhockey_vision.planner_node import Planner

from unittest import TestCase
import pytest

import os
import yaml
import numpy as np


class TestPlanner(TestCase):
    def assert_close(self, arr1, arr2, dist=0.1):
        assert np.linalg.norm(arr1 - arr2) < dist

    def test_no_vel(self):
        init_state = np.array([1, 1, 0, 0])
        final_state_expected = np.array([1, 1, 0, 0])

        transform_matrix = Planner.default_prediction_matrix_generator(1)
        final_state = np.dot(transform_matrix, init_state)

        self.assert_close(final_state, final_state_expected)

    def test_moving(self):
        init_state = np.array([1, 1, 5, 3])
        final_state_expected = np.array([6, 4, 5, 3])

        transform_matrix = Planner.default_prediction_matrix_generator(1)
        final_state = np.dot(transform_matrix, init_state)

        self.assert_close(final_state, final_state_expected)

