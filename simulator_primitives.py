import copy

from pose import Pose


def move_forward(pose: Pose) -> Pose:
    """Given a pose, determine the resulting pose if the robot moves one step forward.
    """
    output = copy.deepcopy(pose)

    match pose.direction:
        case Pose.Direction.NORTH:
            output.y += 1
        case Pose.Direction.SOUTH:
            output.y -= 1
        case Pose.Direction.EAST:
            output.x += 1
        case Pose.Direction.WEST:
            output.x -= 1

    return output


def turn_left(direction: Pose.Direction) -> Pose.Direction:
    """Given a direction, return the result of turning left.
    """
    match direction:
        case Pose.Direction.NORTH:
            return Pose.Direction.WEST
        case Pose.Direction.SOUTH:
            return Pose.Direction.EAST
        case Pose.Direction.EAST:
            return Pose.Direction.NORTH
        case Pose.Direction.WEST:
            return Pose.Direction.SOUTH


def turn_right(direction: Pose.Direction) -> Pose.Direction:
    """Given a direction, return the result of turning right.
    """
    match direction:
        case Pose.Direction.NORTH:
            return Pose.Direction.EAST
        case Pose.Direction.SOUTH:
            return Pose.Direction.WEST
        case Pose.Direction.EAST:
            return Pose.Direction.SOUTH
        case Pose.Direction.WEST:
            return Pose.Direction.NORTH
