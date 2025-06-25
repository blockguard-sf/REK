# Copyright (c) 2025 BlockGuard SF.
# Licensed under the MIT License.

"""
PyPIxz-ND Fork of PyPIxz with no dependencies required.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2025 BlockGuard SF.
:license: MIT, see LICENSE for more details.
"""

__all__ = [
    'install_requirements',
    'install_modules',
]

from .__version__ import (
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __license__,
    __copyright__
)

from .install_packages import install_requirements, install_modules