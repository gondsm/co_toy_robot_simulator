# A static method returns an object of the class below, so we need "better" type annotations.
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional
import logging

from pose import Pose

logger = logging.getLogger(__name__)


@dataclass
class Command:
    """Represents a single command to be passed to the simulator.

    Contains a command type and a pose. The pose will only be valid for commands of type PLACE; all other commands will
    have their pose set to None.
    """

    class Type(Enum):
        """Enumerates all known command types.

        (Enum values are strings to aid in string-to-enum conversion.)
        """
        PLACE = "PLACE",
        MOVE = "MOVE",
        LEFT = "LEFT",
        RIGHT = "RIGHT",
        REPORT = "REPORT"

    def __init__(self, type: Type, pose: Optional[Pose] = None):
        """Ensures that the object is initialised consistently, namely that pose is only valid for a PLACE command.
        """
        self.type = type
        self.pose = pose

        if self.type == Command.Type.PLACE:
            if pose is None:
                raise RuntimeError("A PLACE command MUST always have a pose!")

        if self.type != Command.Type.PLACE:
            if pose is not None:
                raise RuntimeError("Only PLACE commands should have a pose!")

    @classmethod
    def from_string(cls, raw_cmd: str) -> Command:
        """Constructs a new Commmand from the given string.

        Raises a RuntimeError if parsing failes, and uses logging to explain why.
        """
        cmd = parse_string_into_command(raw_cmd)

        # If parsing fails for any reason, we raise an exception here.
        # (Parsing should have logged out the reason for the failure.)
        if cmd is None:
            raise RuntimeError(f"Could not parse command: {raw_cmd}")

        return cmd

    type: Type
    pose: Optional[Pose]


def parse_string_into_command(raw_cmd: str) -> Optional[Command]:
    """Parses a string into a command.

    In case of parsing failure, the reason for failure is logged out, and the output will be None.
    """
    split_raw_cmd = raw_cmd.split(" ")

    # Parse out the command type
    type = None
    try:
        type = Command.Type[split_raw_cmd[0]]
    except KeyError:
        logger.error(f"Unknown command type or wrong separator in {raw_cmd}.")
        return None

    # Parse out the pose for a PLACE command
    pose = None

    if type == Command.Type.PLACE:
        if len(split_raw_cmd) != 2:
            logger.error(f"Wrong number of parts in PLACE command: {len(split_raw_cmd)}")
            return None

        split_params = split_raw_cmd[1].split(",")

        if len(split_params) != 3:
            logger.error(f"Wrong number of arguments in PLACE command: {len(split_params)}")
            return None

        try:
            x = int(split_params[0])
            y = int(split_params[1])
        except ValueError:
            logger.error("Error parsing out numbers from command!")
            return None

        try:
            direction = Pose.Direction[split_params[2]]
        except KeyError:
            logger.error(f"Given direction is invalid: {split_params[2]}")
            return None

        pose = Pose(x, y, direction)

    return Command(type, pose)
