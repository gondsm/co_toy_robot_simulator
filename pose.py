from dataclasses import dataclass
from enum import Enum


@dataclass
class Pose:
    """Represents a pose (position + direction).

    Valid directions are limited to the members of the Direction enum.
    """

    class Direction(Enum):
        """Enumerates all possible directions.

        (Enum values are strings to aid in string-to-enum conversion.)
        """
        NORTH = "NORTH",
        SOUTH = "SOUTH",
        EAST = "EAST",
        WEST = "WEST"

    def to_short_string(self) -> str:
        return f"{self.x},{self.y},{self.direction}"

    x: int
    y: int
    direction: Direction
