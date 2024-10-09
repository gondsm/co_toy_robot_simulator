import unittest
import sys
from pathlib import Path

# Make modules in parent directory accessible
sys.path.append(str(Path(__file__).parents[1]))

from pose import Pose
import simulator_primitives as primitives


class TestMove(unittest.TestCase):
    """Test moving the robot around.
    """

    def test_move_north(self):
        initial_pose = Pose(1, 1, Pose.Direction.NORTH)
        expected_pose = Pose(1, 2, Pose.Direction.NORTH)

        result = primitives.move_forward(initial_pose)

        self.assertEqual(result, expected_pose)

    def test_move_south(self):
        initial_pose = Pose(1, 1, Pose.Direction.SOUTH)
        expected_pose = Pose(1, 0, Pose.Direction.SOUTH)

        result = primitives.move_forward(initial_pose)

        self.assertEqual(result, expected_pose)

    def test_move_east(self):
        initial_pose = Pose(1, 1, Pose.Direction.EAST)
        expected_pose = Pose(2, 1, Pose.Direction.EAST)

        result = primitives.move_forward(initial_pose)

        self.assertEqual(result, expected_pose)

    def test_move_west(self):
        initial_pose = Pose(1, 1, Pose.Direction.WEST)
        expected_pose = Pose(0, 1, Pose.Direction.WEST)

        result = primitives.move_forward(initial_pose)

        self.assertEqual(result, expected_pose)


class TestTurnLeft(unittest.TestCase):
    """Test turning left.

    (These may seem a tad excessive, but I wanted to cover all combinations in case I decided to change the underlying
    implementation. The key is that there is no cross-contamination between functionality and the tests, meaning we can
    go ahead and re-implement functions as needed, confident that the tests will catch regressions.)
    """

    def test_turn_left_north(self):
        initial_direction = Pose.Direction.NORTH
        expected_direction = Pose.Direction.WEST

        result = primitives.turn_left(initial_direction)

        self.assertEqual(result, expected_direction)

    def test_turn_left_south(self):
        initial_direction = Pose.Direction.SOUTH
        expected_direction = Pose.Direction.EAST

        result = primitives.turn_left(initial_direction)

        self.assertEqual(result, expected_direction)

    def test_turn_left_east(self):
        initial_direction = Pose.Direction.EAST
        expected_direction = Pose.Direction.NORTH

        result = primitives.turn_left(initial_direction)

        self.assertEqual(result, expected_direction)

    def test_turn_left_west(self):
        initial_direction = Pose.Direction.WEST
        expected_direction = Pose.Direction.SOUTH

        result = primitives.turn_left(initial_direction)

        self.assertEqual(result, expected_direction)


class TestTurnRight(unittest.TestCase):
    """Test turning right.

    (Same observations as above.)
    """

    def test_turn_right_north(self):
        initial_direction = Pose.Direction.NORTH
        expected_direction = Pose.Direction.EAST

        result = primitives.turn_right(initial_direction)

        self.assertEqual(result, expected_direction)

    def test_turn_right_south(self):
        initial_direction = Pose.Direction.SOUTH
        expected_direction = Pose.Direction.WEST

        result = primitives.turn_right(initial_direction)

        self.assertEqual(result, expected_direction)

    def test_turn_right_east(self):
        initial_direction = Pose.Direction.EAST
        expected_direction = Pose.Direction.SOUTH

        result = primitives.turn_right(initial_direction)

        self.assertEqual(result, expected_direction)

    def test_turn_right_west(self):
        initial_direction = Pose.Direction.WEST
        expected_direction = Pose.Direction.NORTH

        result = primitives.turn_right(initial_direction)

        self.assertEqual(result, expected_direction)
