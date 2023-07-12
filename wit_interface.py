from wit import Wit


class WitInterface:
    available_commands = ['init', 'add']

    @staticmethod
    def command_handling(command, arg):
        match command:
            case "init":
                Wit.init()
            case "add":
                Wit.add(arg)
