import unittest
from unittest import TestCase
import pytest
import numpy as np
from airhockey_vision.puck_trajectory import TrajectoryCalculator

class TestTrajectory(TestCase):
    def assert_close(self, arr1, arr2, dist=0.1):
        assert np.linalg.norm(arr1 - arr2) < dist

    def test_first_run(self):
        t = TrajectoryCalculator()
        x, y = 30, 30
        vector = t.update_state(x,y,1.0001)
        assert vector[2] == vector[3] == 0
        assert t.first_run == False

    def test_future_pos(self):
        x1, y1, x2, y2 = 30, 30, 31, 35
        time1, time2 = 1.005, 2.005
        t = TrajectoryCalculator()
        t.update_state(x1, y1, 1.005)
        x, y, xd, yd = t.update_state(x2, y2, time2)

        assert x == 31
        assert y == 35
        assert xd == pytest.approx(1, 0.1)
        assert yd == pytest.approx(5, 0.1)

    def test_buffer(self):
        x, y = 30, 30
        time = 1.0001
        t = TrajectoryCalculator()

        t.update_state(x, y, time)

        x += 1
        y += 2
        time += 1
        t.update_state(x, y, time)

        x += 1
        y += 2
        time += 1
        t.update_state(x, y, time)

        x += 1
        y += 2
        time += 1
        t.update_state(x, y, time)

        x += 1
        y += 2
        time += 1
        t.update_state(x, y, time)

        x += 1
        y += 2
        time += 1
        t.update_state(x, y, time)

        x += 1
        y += 2
        time += 1
        t.update_state(x, y, time)

        assert len(t.buffer) == 5

    def test_no_vel(self):
        init_state = np.array([1, 1, 0, 0])
        final_state_expected = np.array([1, 1, 0, 0])

        transform_matrix = \
                TrajectoryCalculator.default_prediction_matrix_generator(1)
        final_state = np.dot(transform_matrix, init_state)

        self.assert_close(final_state, final_state_expected)

    def test_moving(self):
        init_state = np.array([1, 1, 5, 3])
        final_state_expected = np.array([6, 4, 5, 3])

        transform_matrix = \
                TrajectoryCalculator.default_prediction_matrix_generator(1)
        final_state = np.dot(transform_matrix, init_state)

        self.assert_close(final_state, final_state_expected)


if __name__ == '__main__':
    unittest.main()

