import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        time1 = data.Time(4, 17, 1)
        time2 = data.Time(3, 18, 1)
        result = lab5.time_add(time1,time2)
        expected = data.Time (7,35,2)
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        time1 = data.Time(5, 18, 2)
        time2 = data.Time(2, 17, 1)
        result = lab5.time_add(time1, time2)
        expected = data.Time(7, 35, 3)
        self.assertEqual(expected, result)
    # Part 4
    def test_is_descending_1(self):
        list = [1,2,3,4]
        result = lab5.is_descending(list)
        self.assertEqual(False, result)

    def test_is_descending_2(self):
        list = [4,3,2,1]
        result = lab5.is_descending(list)
        self.assertEqual(True, result)
    # Part 5


    # Part 6
    def test_furthest_from_the_origin_1(self):
        points = [data.Point(1, 2), data.Point(3, 4),
                  data.Point(0, 5), data.Point(6, 8)]
        self.assertEqual((points), 3)

    def test_furthest_from_the_origin_1(self):
        points = [data.Point(1, 2), data.Point(3, 4),
                  data.Point(0, 5), data.Point(6, 8)]
        self.assertEqual((points), 3)


if __name__ == '__main__':
    unittest.main()
