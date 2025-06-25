# Copyright (c) 2025 BlockGuard SF
# Licensed under the Apache-2.0 License.


class BaseCommands:
    # Metadata about this command.
    message = "",
    commands = {}

    def get(self):
        values = []
        for info in self.commands:
            values.append(info)
        return values
