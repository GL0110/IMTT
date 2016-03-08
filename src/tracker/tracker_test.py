import tracker
import unittest

class CalcsBoxPos_Test(unittest.TestCase):

  def test_evenbox(self):
    box = [[66, 120],
           [68, 120],
           [66, 122],
           [68, 122]]
    expected_pos = (67, 121)
    pos = tracker.GetBBoxPos(box)
    self.assertEqual(expected_pos, pos)

  # def TestOddBox(self)



def main():
  unittest.main()

if __name__ == '__main__':
  main()
