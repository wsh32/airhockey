from unittest import TestCase
import pytest
import numpy as np
from airhockey_vision.puck_trajectory import TrajectoryCalculator

class TestTrajectory(TestCase):
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
        x, y, xd, yd = t.calc_trajectory(x2, y2, time2)

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



if __name__ == '__main__':
    test = TestTrajectory()
    test.test_first_run()
    test.test_future_pos()
    test.test_buffer()
