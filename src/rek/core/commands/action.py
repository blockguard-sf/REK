# Copyright (c) 2025 BlockGuard SF
# Licensed under the Apache-2.0 License.

from core.basic import BaseCommands
from core.packages.create import Create


class ActionCommands(BaseCommands):
    message = "What do you want to do?"
    commands = {
        "Create": lambda: Create()
    }
