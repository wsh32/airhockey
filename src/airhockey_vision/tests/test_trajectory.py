from unittest import TestCase
import pytest
import numpy as np
from airhockey_vision.puck_trajectory import TrajectoryCalculator

class TestTrajectory(TestCase):
    def test_first_run(self):
        t = TrajectoryCalculator()
        x,y = 30, 30
        vector = t.calc_trajectory(x,y,1.0001)
        assert vector[2] == vector[3] == 0
        assert t.first_run == False
        print(t.prev_time)

    def test_future_pos(self):
        x1,y1,x2,y2 = 30,30,31,35
        time1, time2 = 1.005, 2.005
        t = TrajectoryCalculator()
        t.calc_trajectory(x1,y1,1.005)
        x, y, xd, yd = t.calc_trajectory(x2,y2,2.005)
        assert x == 31
        assert y == 35
        assert xd - 1 < 1e3
        assert yd - 5 < 1e3


    def test_buffer(self):
        x,y = 30, 30
        t = TrajectoryCalculator()
        t.calc_trajectory(x,y,1.0001)
        t.calc_trajectory(x,y,2.0001)
        t.calc_trajectory(x,y,3.0001)
        t.calc_trajectory(x,y,4.0001)
        t.calc_trajectory(x,y,5.0001)
        t.calc_trajectory(x,y,6.0001)
        assert len(t.buffer) == 5


if __name__ == '__main__':
    test = TestTrajectory()
    test.test_first_run()
    test.test_future_pos()
