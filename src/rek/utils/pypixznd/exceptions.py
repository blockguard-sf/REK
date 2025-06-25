# Copyright (c) 2025 BlockGuard SF.
# Licensed under the MIT License.

class BasePyPIxzNDException(Exception):
    """Base exception for PyPIxz-ND."""

    def __init__(self, *args, details=None):
        """
        Initialize the exception with optional additional arguments.
        """
        self.details = details  # Stores the additional details
        super().__init__(*args)  # Passes the positional arguments to Exception


# Exceptions for dependency management and package installation
class DependencyError(BasePyPIxzNDException):
    """Exception raised when a dependency cannot be installed."""


class MissingRequirementsFileError(DependencyError):
    """Exception raised when a requirements file is missing."""


class ModuleInstallationError(DependencyError):
    """Exception raised when a module cannot be installed."""


class InvalidModuleVersionError(DependencyError):
    """Exception raised when a module version is invalid."""


# Additional utility exceptions
class FileError(BasePyPIxzNDException):
    """Exception raised when there is a file error."""


class ChunkedEncodingError(FileError):
    """Exception raised when chunked encoding fails."""


class SteamConsumeError(FileError):
    """Exception raised when Steam consume fails."""


# Example of Warning (if needed later)
class PyPIxzNDWarning(Warning):
    """Base warning for PyPIxz."""


class DeprecatedFeatureWarning(PyPIxzNDWarning):
    """Warning for deprecated features."""
