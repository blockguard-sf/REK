# Copyright (c) 2025 BlockGuard SF
# Licensed under the Apache-2.0 License.

import logging
import os
import subprocess

class Create:
    def __init__(self):
        self.name, self.description, self.author, self.license, self.git, self.directory = self.setup_config()
        self.metadata = {
            "name": self.name,
            "description": self.description,
            "author": self.author,
            "license": self.license,
            "git": self.git,
            "directory": self.directory
        }

        logging.debug(f"Metadata: {self.metadata}")

        if self.check_config():
            logging.debug("The configuration data has been approved.")
            self.build()



    @classmethod
    def setup_config(self):
        logging.debug("Configuring the new package.")
        return input("Name: "), input("Description: "), input("Author: "), input("License: "), input("Git: [Y/N] "), input("Package Directory: ")

    def check_config(self):
        logging.debug("Checking the package configuration.")

        for data in self.metadata:
            if self.metadata[data] == "":
                logging.error(f"A value is missing from the data: '{data}'")
                return False

        self.git = str.lower(self.git)
        self.name = str.lower(self.name)
        if self.git != "y" and self.git != "n":
            logging.error("The value you entered in the 'git' data is invalid.")
            return False

        self.directory = os.path.abspath(self.directory)
        if not os.path.exists(self.directory):
            logging.error(f"The directory you provided does not exist. ({self.directory})")
            return False

        return True

    def build(self):
        os.makedirs(f"{self.directory}/{self.name}/src/{self.name}/out")
        with open(f"{self.directory}/{self.name}/src/{self.name}/Metadata.luau", "w") as file:
            file.write(f"""return {{
    ["Name"] = "{self.name}",
    ["Version"] = "1.0.0",
    ["Description"] = "{self.description}",
    ["Main"] = "out/index.luau",
    ["Author"] = "{self.author}",
    ["License"] = "{self.license}",{f"\n    [\"Repository\"] = \"https://github.com/{self.author}/{self.name}\"," if self.git else ""}
    ["Dependencies"] = {{}},
    ["Files"] = {{
        "out",
    }}
}}
""")

        with open(f"{self.directory}/{self.name}/src/{self.name}/License.luau", "w") as file:
            file.write(f"""--[[
{self.license}

-> Your license here <-
--]]

return "{self.license}" """)

        with open(f"{self.directory}/{self.name}/src/{self.name}/out/index.luau", "w") as file:
            file.write("""local Module = {}
Module.__index = Module

function Module.new()
    local self = setmetatable({}, Module)
    print("Hello, World!")
    return self
end

return Module""")

        if self.git == "y":
            os.chdir(f"{self.directory}/{self.name}")
            subprocess.run(["git", "init"])
            with open(f"{self.directory}/{self.name}/README.md", "w") as file:
                file.write(f"# {self.name}")
