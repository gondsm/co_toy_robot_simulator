from typing import Optional
import logging

from command import Command
from state import State
from pose import Pose
import simulator_primitives as primitives

logger = logging.getLogger(__name__)


class Simulator:
    """The Simulator class manages the state of the world and of the robot.

    This class is responsible for processing commands that change (or don't) the state of the world and the robot, and
    also to report on that state as needed.
    """

    robot_state: Optional[Pose] = None

    # Limits of the table
    # (Taken from task, but could easily be configured.)
    x_range: list[int] = [0, 4]
    y_range: list[int] = [0, 4]

    def process_command(self, command: Command):
        # Determine how the command will affect state
        candidate_state = self.__compute_next_state(command)

        # Determine whether that effect is acceptable
        if self.__validate_state(candidate_state):
            # If so, replace the current state
            self.robot_state = candidate_state
        else:
            logger.warning("Latest command would lead to inadmissible state, so it has been ignored.")

    def get_current_state(self) -> State:
        if self.robot_state is None:
            raise RuntimeError("The simulator was asked to output a state before initialisation!")

        return State(self.robot_state)

    def __compute_next_state(self, command: Command) -> Pose:
        """Computes the next state of the system given a command.
        """
        match command.type:
            case Command.Type.PLACE:
                return command.pose
            case Command.Type.MOVE:
                return primitives.move_forward(self.robot_state)
            case Command.Type.LEFT:
                return Pose(self.robot_state.x, self.robot_state.y, primitives.turn_left(self.robot_state.direction))
            case Command.Type.RIGHT:
                return Pose(self.robot_state.x, self.robot_state.y, primitives.turn_right(self.robot_state.direction))
            case _:
                raise RuntimeError(f"Simulator received an unexpected command type: {command.type}")

    def __validate_state(self, candidate_state: Pose):
        """Determines whether the candidate state is valid.
        """
        if self.x_range[0] <= candidate_state.x <= self.x_range[1]\
           and self.y_range[0] <= candidate_state.y <= self.y_range[1]:
            return True
        else:
            return False
