import click

from wit import Wit


class WitInterface:
    available_commands = ['init', 'add', 'commit']

    @staticmethod
    def command_handling(command, arg):
        match command:
            case "init":
                Wit.init()
            case "add":
                if len(arg) > 0:
                    Wit.add(arg)
            case "commit":
                if len(arg) > 0:
                    Wit.commit(arg)
                click.secho('Try again with massage', fg="red", bold=True)

