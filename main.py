import click as click
from wit_interface import WitInterface

if __name__ == '__main__':
    @click.command()
    @click.argument("command")
    @click.argument("param", default="")
    def wit_CLI(command, param):
        if command in WitInterface.available_commands:
            WitInterface.command_handling(command, param)
        else:
            click.secho('no such wit command', fg="red", bold=True)


    wit_CLI()
