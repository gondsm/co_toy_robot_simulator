from dataclasses import dataclass
from enum import Enum


@dataclass
class Pose:
    class Direction(Enum):
        NORTH = "NORTH",
        SOUTH = "SOUTH",
        EAST = "EAST",
        WEST = "WEST"

    def to_short_string(self) -> str:
        return f"{self.x},{self.y},{self.direction}"

    x: int
    y: int
    direction: Direction
