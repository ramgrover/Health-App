import unittest
from healthApp import calculate_days_to_target, calculate_maintenance_calories

class TestHealthFunctions(unittest.TestCase):
    def test_calculate_days_to_target(self):
        # Test for different strategies
        self.assertEqual(calculate_days_to_target(70, 60, "mild"), 40)  # Assuming 0.25 kg change per day for mild strategy
        self.assertEqual(calculate_days_to_target(70, 60, "moderate"), 20)  # Assuming 0.5 kg change per day for moderate strategy
        self.assertEqual(calculate_days_to_target(70, 60, "quick"), 10)  # Assuming 1 kg change per day for quick strategy

        # Test for invalid strategy input
        self.assertEqual(calculate_days_to_target(70, 60, "invalid"), "Invalid strategy input")

    def test_calculate_maintenance_calories(self):
        # Test for valid input
        self.assertEqual(calculate_maintenance_calories(70, 170, 25, "male", 3), (1692.5, 2624.875))  # Sample input values

        # Test for invalid gender
        self.assertEqual(calculate_maintenance_calories(70, 170, 25, "invalid", 3), "Invalid gender")

        # Test for invalid activity level
        self.assertEqual(calculate_maintenance_calories(70, 170, 25, "male", 6), "Invalid activity level")

if __name__ == '__main__':
    unittest.main()
