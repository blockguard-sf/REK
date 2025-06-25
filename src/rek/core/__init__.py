# Copyright (c) 2025 BlockGuard SF
# Licensed under the Apache-2.0 License.

import sys
from InquirerPy import inquirer

from utils.updater import check_versions
from __init__ import forge_api_latest_release
from core.manager import Categories


class REK:
    def __init__(self, current_version):
        self.current_version = current_version
        self.latest_version = check_versions(forge_api_latest_release, self.current_version)
        if self.latest_version:
            exit("Install the latest REK for new features and improvements! https://github.com/blockguard-sf/REK/releases/latest")

        self.environment_version = '.'.join(map(str, sys.version_info[:3]))

        print(f"REK : RoLib Extension Kit - {self.current_version} [{self.environment_version}]\n")

        while True:
            category = self.load_command_class(
                message=Categories.message,
                choices=Categories.get(Categories)
                )
            self.call_command(category)


    def load_command_class(self, message, choices):
        try:
            return inquirer.select(message=message, choices=choices).execute()
        except KeyboardInterrupt:
            exit()

    def call_command(self, command):
        categories_cmd = Categories.commands
        if command in categories_cmd:
            instance = categories_cmd[command]()
