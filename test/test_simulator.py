import unittest
import sys
from pathlib import Path

# Make modules in parent directory accessible
sys.path.append(str(Path(__file__).parents[1]))

from simulator import Simulator
from command import Command
from pose import Pose


class TestSimulator(unittest.TestCase):
    """Test the Simulator class.

    These are not meant as exhaustive tests of the underlying functionaly; they test only if the Simulator is plumbing
    through commands appropriately.

    (see test_simulator_primitives for exhaustive testing of underlying functionality)
    """

    def test_construction(self):
        """It should be possible to construct a Simulator with nothing going wrong.
        """
        sim = Simulator()

        self.assertEqual(sim.robot_state, None)

    def test_placement(self):
        """It should be possible to place a robot.
        """
        target_pose = Pose(0, 0, Pose.Direction.NORTH)
        cmd = Command(Command.Type.PLACE, target_pose)

        sim = Simulator()

        sim.process_command(cmd)

        self.assertEqual(sim.robot_state, target_pose)

    def test_moving(self):
        """It should be possible to move a placed robot
        """
        target_pose = Pose(0, 0, Pose.Direction.NORTH)
        cmd = Command(Command.Type.PLACE, target_pose)

        sim = Simulator()

        sim.process_command(cmd)

        cmd_move = Command(Command.Type.MOVE)

        sim.process_command(cmd_move)

        expected_pose = Pose(0, 1, Pose.Direction.NORTH)
        self.assertEqual(sim.robot_state, expected_pose)

    def test_turning_left(self):
        """It should be possible to turn left.
        """
        target_pose = Pose(0, 0, Pose.Direction.NORTH)
        cmd = Command(Command.Type.PLACE, target_pose)

        sim = Simulator()

        sim.process_command(cmd)

        cmd_turn = Command(Command.Type.LEFT)

        sim.process_command(cmd_turn)

        expected_pose = Pose(0, 0, Pose.Direction.WEST)
        self.assertEqual(sim.robot_state, expected_pose)

    def test_turning_right(self):
        """It should be possible to turn right.
        """
        target_pose = Pose(0, 0, Pose.Direction.NORTH)
        cmd = Command(Command.Type.PLACE, target_pose)

        sim = Simulator()

        sim.process_command(cmd)

        cmd_turn = Command(Command.Type.RIGHT)

        sim.process_command(cmd_turn)

        expected_pose = Pose(0, 0, Pose.Direction.EAST)
        self.assertEqual(sim.robot_state, expected_pose)