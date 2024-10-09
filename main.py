import logging
import argparse

from simulator import Simulator
from user_interface import UserInterface
from command import Command


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Little toy robot simulator.")
    parser.add_argument('--live',
                        action='store_true',
                        help='If set, the simulator will take input from stdin. If not, it will run a hard-coded test.')
    args = parser.parse_args()

    # Construct simulator and user interface, the two components we will orchestrate here.
    simulator = Simulator()
    interface = UserInterface()

    # Select a source of commands, depending on whether this is a live session.
    command_source = interface.get_command_from_user if args.live else interface.get_pre_coded_commands

    # Iterate over the source of commands until it has run out.
    for command in command_source():
        # The simulator does not need to process REPORT commands, as they cannot affect state.
        if command.type != Command.Type.REPORT:
            simulator.process_command(command)

        # The interface is always told about the latest state, in case it needs to update something (e.g.
        # visualisation).
        current_state = simulator.get_current_state()
        interface.update_state(current_state)

        # If the command is to report, then the interface is told to do so
        if command.type == Command.Type.REPORT:
            interface.report_state()
