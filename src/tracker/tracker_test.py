import tracker
import unittest

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




def main():
  unittest.main()

if __name__ == '__main__':
  main()
