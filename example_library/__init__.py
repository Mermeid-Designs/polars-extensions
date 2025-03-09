"""
@mainpage Example Library (TODO: add project name)

@section description_main Description
TODO: write short description of project

@section notes_main Notes
- TODO: Add special project notes here that you want to communicate to the user.

@section author_sensors Author(s)
- Created by First Last (TODO: substitute placeholders with your information)
- Maintained by First Last (TODO: substitute placeholders with person's information, or delete)
"""

from importlib import metadata

package_name = 'example-library'  # TODO: substitute placeholder with package name
__version__ = metadata.version(package_name)
VERSION = __version__

__all__ = ['__version__', 'VERSION']
