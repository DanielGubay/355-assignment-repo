import unittest
from io import StringIO
import sys

# Import the code you want to test
from add import add_numbers

class TestAddPositive(unittest.TestCase):
    def test_positive_addition(self):
        # Redirect stdout for capturing the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input for positive numbers
        user_input = "5\n6\n"
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            add_numbers()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the printed result
        printed_output = captured_output.getvalue()

        # Check if the output matches the expected result
        self.assertEqual(printed_output.strip(), "The sum of 5.0 and 6.0 is: 11.0")

if __name__ == '__main__':
    unittest.main()

