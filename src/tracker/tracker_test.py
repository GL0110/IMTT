import tracker
from tracker import Track
import unittest


class Track_Test(unittest.TestCase):

    # Test to make sure that UpdatePosition sets next_box as position and
    # removes it from the array.
    def test_UpdatePosition(self):

        init_box = [[0, 0],
                    [1, 0],
                    [0, 1],
                    [1, 1]]
        next_box = [[1, 1],
                    [2, 1],
                    [1, 2],
                    [2, 2]]
        far_box = [[10, 10],
                   [11, 10],
                   [10, 11],
                   [11, 11]]
        input_track = Track(init_box)
        bbox_arr = [next_box, far_box]
        input_track.FindClosest(bbox_arr)
        # Ensure that it has been updated to next closest box.
        self.assertNotEqual(input_track.box, init_box)
        self.assertEqual(input_track.box, next_box)

        # Ensure that next_box has been removed from array.
        self.assertNotEqual(bbox_arr, [next_box, far_box])
        self.assertEqual(bbox_arr, [far_box])


class BBoxUtils_Test(unittest.TestCase):

  # Test with an even distance between points.
  def test_EvenBoxPos(self):
    box = [[66, 120],
           [68, 120],
           [66, 122],
           [68, 122]]
    expected_pos = (67, 121)
    pos = tracker.GetBBoxPos(box)
    self.assertEqual(expected_pos, pos)

  # Test with an odd distance between points
  def test_OddBoxPos(self):
    box = [[67, 120],
           [70, 120],
           [67, 123],
           [70, 123]]
    # The function returns int positions, so it will round down.
    expected_pos = (68, 121)
    pos = tracker.GetBBoxPos(box)
    self.assertEqual(expected_pos, pos)

  def test_DistCalc(self):
    pos1 = (0, 0)
    pos2 = (1, 0)
    expected_dist = 1
    self.assertEqual(tracker.CalcDistance(pos1, pos2), expected_dist)
    pos1 = (0, 0)
    pos2 = (0, 1)
    self.assertEqual(tracker.CalcDistance(pos1, pos2), expected_dist)

  # Test Distance calc where pos2 is greater than pos1, such that
  # pos1.x - pos2.x < 0
  def test_DistCalcWithReverseOrderedPoints(self):
    pos1 = (1, 0)
    pos2 = (2, 0)
    expected_dist = 1
    self.assertEqual(tracker.CalcDistance(pos1, pos2), expected_dist)
    pos1 = (0, 1)
    pos2 = (0, 2)
    expected_dist = 1
    self.assertEqual(tracker.CalcDistance(pos1, pos2), expected_dist)




def main():
  unittest.main()

if __name__ == '__main__':
  main()
