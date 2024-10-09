from dataclasses import dataclass

from pose import Pose


@dataclass
class State:
    """Encapsulates the current state of simulation.
    """
    pose: Pose
