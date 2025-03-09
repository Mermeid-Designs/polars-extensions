"""Defines version functions.

@file version.py

@brief The `version` module holds the version information for this library.

@section description_version Description
Defines the functions to report version information.
- version_short
- version_info
- parse_mypy_version

@section libraries_version Libraries/Modules
- [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html) standard library
  - Access to `distributions` function
- [`pathlib`](https://docs.python.org/3/library/pathlib.html) standard library
  - Access to `Path(...).resolve` function
- [`platform`](https://docs.python.org/3/library/platform.html) standard library
  - Access to `platform` function
- [`sys`](https://docs.python.org/3/library/sys.html) standard library
  - Access to `version_info` function.

@section notes_version Notes
- Intended for use when reporting a GitHub issue bug.

@section todo_version TODO
- None.

@section author_sensors Author(s)
- Created by First Last (TODO: substitute placeholders with your information)
- Maintained by First Last (TODO: substitute placeholders with person's information, or delete)
"""

from .__init__ import __version__ as VERSION

__all__ = ['VERSION', 'version_info']


def version_short() -> str:
    """Get the abbreviated version of this library

    @return The major and minor part of the version

    Examples:
    - @snippet version.py version_short
    """
    return '.'.join(VERSION.split('.')[:2])


def version_info() -> str:
    """Get complete version information for this library and its dependencies.

    @return Formatted output of version information.

    Example output:

    > VERSION: 2.6.3
    >
    > install path: /Users/usr/Documents/GitHub/example-libary/example_library
    >
    > python version: 3.11.6 (main, Oct  2 2023, 13:45:54) [Clang 15.0.0 (clang-1500.0.40.1)]
    >
    > platform: macOS-14.2-arm64-arm-64bit
    >
    > related packages:
    """
    import platform
    import sys
    from importlib import metadata
    from pathlib import Path

    # get data about packages that are closely related to this library, use this library or often conflict with this library
    package_names = {}  # TODO: add relevant package names
    related_packages: list[str] = []
    for dist in metadata.distributions():
        name = dist.metadata['Name']
        if name in package_names:
            related_packages.append(f'{name}-{dist.version}')
    info = {
        'VERSION': VERSION,
        'install path': Path(__file__).resolve().parent,
        'python version': sys.version,
        'platform': platform.platform(),
        'related packages': ' '.join(related_packages),
    }
    return '\n'.join(
        '{:>30} {}'.format(k + ':', str(v).replace('\n', ' ')) for k, v in info.items()
    )


def parse_mypy_version(version: str) -> tuple[int, ...]:
    """Parse mypy string version to tuple of ints.

    This function is included here rather than the mypy plugin file because the mypy plugin file cannot be imported
    outside a mypy run.

    @param version  The mypy version string.
    @return  A tuple of ints representing the version number.

    Examples:
    - @snippet version.py parse_mypy_version normal
    - @snippet version.py parse_mypy_version dev
    """
    return tuple(map(int, version.partition('+')[0].split('.')))
