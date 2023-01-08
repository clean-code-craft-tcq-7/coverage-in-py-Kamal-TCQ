import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertEqual(typewise_alert.infer_breach(150, 50, 100), 'TOO_HIGH')
    self.assertEqual(typewise_alert.infer_breach(50, 50, 100), 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(75, 50, 100), 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(49, 50, 100), 'TOO_LOW')
    self.assertEqual(typewise_alert.infer_breach(101, 50, 100), 'TOO_HIGH')

if __name__ == '__main__':
  unittest.main()
