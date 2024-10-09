import unittest
import sys
from pathlib import Path

# Make modules in parent directory accessible
sys.path.append(str(Path(__file__).parents[1]))

from command import Command
from pose import Pose


class TestCommand(unittest.TestCase):
    """Test constructing Commands in various ways.
    """

    def test_construction(self):
        """It should be possible to construct a Command directly.
        """
        Command(Command.Type.MOVE)

    def test_construction_invalid_no_pose(self):
        """It should NOT be possible to construct a place command without a pose.
        """
        # Wrap construction into a lambda so it is callable.
        self.assertRaises(RuntimeError,
                          lambda: Command(Command.Type.PLACE, None))

    def test_construction_invalid_too_much_pose(self):
        """It should NOT be possible to construct a non-place command with a pose.
        """
        # Wrap construction into a lambda so it is callable.
        self.assertRaises(RuntimeError,
                          lambda: Command(Command.Type.MOVE, Pose(0, 0, Pose.Direction.NORTH)))


class TestCommandParsing(unittest.TestCase):
    """Test the parser that builds commands from strings.
    """

    def test_sunny_day(self):
        test_string = "MOVE"
        expected_command = Command(Command.Type.MOVE)
        output = Command.from_string(test_string)
        self.assertEqual(expected_command, output)

    def test_unrecongnised_type(self):
        test_string = "NOPE"
        self.assertRaises(RuntimeError,
                          lambda: Command.from_string(test_string))

    def test_wrong_syntax(self):
        test_string = "PLACE,1,2,NORTH"
        self.assertRaises(RuntimeError,
                          lambda: Command.from_string(test_string))

    def test_invalid_numbers(self):
        test_string = "PLACE asd,bsd,NORTH"
        self.assertRaises(RuntimeError,
                          lambda: Command.from_string(test_string))

    def test_invalid_direction(self):
        test_string = "PLACE 0,0,NOPE"
        self.assertRaises(RuntimeError,
                          lambda: Command.from_string(test_string))


if __name__ == "__main__":
    unittest.main()
