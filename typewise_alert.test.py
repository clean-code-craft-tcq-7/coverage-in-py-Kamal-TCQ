import unittest

import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertEqual(typewise_alert.infer_breach(20, 50, 100), 'TOO_LOW')
        self.assertEqual(typewise_alert.infer_breach(150, 50, 100), 'TOO_HIGH')
        self.assertEqual(typewise_alert.infer_breach(50, 50, 100), 'NORMAL')
        self.assertEqual(typewise_alert.infer_breach(75, 50, 100), 'NORMAL')
        self.assertEqual(typewise_alert.infer_breach(49, 50, 100), 'TOO_LOW')
        self.assertEqual(typewise_alert.infer_breach(101, 50, 100), 'TOO_HIGH')

    def test_check_and_alert_with_different_alert_targets(self):
        alert_target = 'TO_CONTROLLER'
        battery_char = {'coolingType': 'PASSIVE_COOLING'}
        temperature_in_c = 30
        breach_type, message = typewise_alert.check_and_alert(alert_target, battery_char, temperature_in_c)
        self.assertEqual(breach_type, 'NORMAL')
        self.assertEqual(message, '0xfeed, NORMAL')

        alert_target = 'TO_EMAIL'
        temperature_in_c = 50
        breach_type, message = typewise_alert.check_and_alert(alert_target, battery_char, temperature_in_c)
        self.assertEqual(breach_type, 'TOO_HIGH')
        self.assertEqual(message, 'a.b@c.com, Hi, the temperature is too high')

 
if __name__ == '__main__':
    unittest.main()
