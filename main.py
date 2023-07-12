import click as click
from wit_interface import WitInterface
from logging_handler import logger
if __name__ == '__main__':
    @click.command()
    @click.argument("command")
    @click.argument("param", default="")
    def wit_CLI(command, param):
        if command in WitInterface.available_commands:
            logger.info(f"wit command executed, command: {command}, args: {param}")
            WitInterface.command_handling(command, param)
        else:
            click.secho('no such wit command', fg="red", bold=True)

    wit_CLI()
