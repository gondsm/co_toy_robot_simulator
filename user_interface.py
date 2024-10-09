from typing import Generator

from command import Command
from state import State


class UserInterface:
    """UserInterface is (unsurprisingly) responsible for receiving commands and displaying output.
    """

    latest_state: State = None

    def get_command_from_user(self) -> Generator[Command, Command, Command]:
        """Yields a new command until the user provides an invalid command, or until the application is stopped.
        """
        while True:
            raw_cmd = input("Input your command: ")
            cmd = Command.from_string(raw_cmd)
            yield cmd

    def get_pre_coded_commands(self) -> Generator[Command, Command, Command]:
        """Yields commands from a hard-coded list.
        """
        test_commands = [
            "PLACE 0,0,NORTH",
            "MOVE",
            "REPORT",
            "PLACE 0,0,NORTH",
            "LEFT",
            "REPORT",
            "PLACE 1,2,EAST",
            "MOVE",
            "MOVE",
            "LEFT",
            "MOVE",
            "REPORT"
        ]

        for raw_command in test_commands:
            cmd = Command.from_string(raw_command)
            yield cmd

    def update_state(self, state: State) -> None:
        """Allows the interface to update its internal state.
        """
        self.latest_state = state

    def report_state(self) -> None:
        """Outputs the state of the system to the terminal as a raw string.
        """
        # Using print() instead of logging as the challenge specifies that the output should be a string in a certain
        # format.
        print(self.latest_state.pose.to_short_string())
