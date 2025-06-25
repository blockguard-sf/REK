# Copyright (c) 2025 BlockGuard SF
# Licensed under the Apache-2.0 License.

"""
REK : RoLib Extension Kit
~~~~~~~~~~~~~~~~~~~~~~~~~

REK makes it easy to create and manage packages for RoLib

:copyright: (c) 2025 BlockGuard SF
:license: Apache-2.0, see LICENSE for more details.
"""

import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from __init__ import __version__
from utils import pypixznd


def configure_logging(set_prefix=False):
    logging.basicConfig(
        level=logging.INFO if not set_prefix else logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(filename='logs.log', mode='w')
        ]
    )


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description=f"REK: RoLib Extension Kit (Version {__version__})")
    parser.add_argument("-d", "--debug",
                        action="store_true",
                        default=False,
                        help="display extra debugging information and metrics")
    args = parser.parse_args()

    configure_logging(args.debug)
    pypixznd.install_requirements(file_path="../requirements.txt", enable_logging=True)

    import core
    core.REK(current_version=__version__)
