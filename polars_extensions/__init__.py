"""
@mainpage Polars Extensions

@section description_main Description
Extensions for Polars.

@section notes_main Notes
- TODO: Add special project notes here that you want to communicate to the user.

@section author_sensors Author(s)
- Created by Mermeid Designs
- Maintained by Mermeid Designs
"""

from importlib import metadata

package_name = 'polars-extensions'
__version__ = metadata.version(package_name)
VERSION = __version__

__all__ = ['__version__', 'VERSION']
