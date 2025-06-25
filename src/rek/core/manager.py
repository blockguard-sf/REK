# Copyright (c) 2025 BlockGuard SF
# Licensed under the Apache-2.0 License.

from InquirerPy import inquirer

from core.basic import BaseCommands
from core.commands.info import InfoCommands
from core.commands.action import ActionCommands

def load_command_class(message, choices):
    try:
        return inquirer.select(message=message, choices=choices).execute()
    except KeyboardInterrupt:
        exit()


class Categories(BaseCommands):
    message = "What do you want to do with REK?"
    commands = {
        "RoLib - Package Actions": lambda : ActionCommands.commands[load_command_class(ActionCommands.message, ActionCommands.get(ActionCommands))](),
        "About": lambda : print(InfoCommands.commands[load_command_class(InfoCommands.message, InfoCommands.get(InfoCommands))]),
        "Exit": lambda : exit()
    }


