from command import Command
from state import State


class UserInterface:
    """UserInterface is (unsurprisingly) responsible for receiving commands and displaying output.
    """

    latest_state: State = None

    def get_command_from_user(self):
        while True:
            raw_cmd = input("Input your command: ")
            cmd = Command.from_string(raw_cmd)
            yield cmd

    def get_pre_coded_commands(self):
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

    def update_state(self, state: State):
        self.latest_state = state

    def report_state(self):
        """Outputs the state of the system to the terminal as a raw string.
        """
        # Using print() instead of logging as the challenge specifies that the output should be a string in a certain
        # format.
        print(self.latest_state.pose.to_short_string())
