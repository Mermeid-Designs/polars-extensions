"""Defines caching decorators.
#
@file cache.py

@brief The `cache` module holds decorator functions to enable caching of python objects.

@section description_cache Description
Defines the decorator functions to support saving and loading output to files.
- numpy_cache
- pickle_cache

@section libraries_cache Libraries/Modules
- [`functools`](https://docs.python.org/3/library/functools.html) standard library
  - Access to `wraps` function
- [`logging`](https://docs.python.org/3/library/logging.html) standard library
  - Access to `exception` function
- [`numpy`](https://numpy.org/doc/) library
  - Access to saving functions and loading functions
- [`pathlib`](https://docs.python.org/3/library/pathlib.html) standard library
  - Access to `Path(...).is_file` function
  - Access to `Path(...).open` function
- [`pickle`](https://docs.python.org/3/library/pickle.html) standard library
  - Access to `dump` function.
  - Access to `load` function.
- [`typing`](https://docs.python.org/3/library/typing.html) standard library
  - Access to `Callable` type hint.

@section notes_cache Notes
- None.

@section todo_cache TODO
- None.

@section author_cache Author(s)
- Created by First Last (TODO: substitute placeholders with your information)
- Maintained by First Last (TODO: substitute placeholders with person's information, or delete)
"""

import logging
from collections.abc import Callable
from functools import wraps
from inspect import signature
from pathlib import Path
from pickle import dump, load

import numpy as np

__all__ = []

# TODO: substitute placeholder package name


##
# @example numpy_cache.py
# This is an example of how to use the example_library.cache.numpy_cache method.
# More details about this example.
def numpy_cache(
    load_function: Callable | None = np.load,
    save_function: Callable | None = np.save,
    **kwargs,
):
    """Enable caching of `numpy` objects

    Extend another function's behavior by introducing caching.

    The numpy load and save functions are customizable but must be statically set.

    @param load_function  The numpy function intended for loading the data in; defaults to `np.load`.
    @param save_function  The numpy function intended for loading the data in; defaults to `np.save`.
    @param function  Function which caching is desired.
    @return  Numpy array object(s)

    Examples:
    - @ref numpy_cache.py
    """
    load_kwargs = dict()
    save_kwargs = dict()

    if len(kwargs) > 0:
        valid_load_kwargs = [
            param.name
            for param in signature(load_function).parameters.values()
            if param.default != param.empty
        ]
        valid_save_kwargs = [
            param.name
            for param in signature(save_function).parameters.values()
            if param.default != param.empty
        ]

    for key, value in kwargs.items():
        if key in valid_load_kwargs:
            load_kwargs.update({key: value})
        elif key in valid_save_kwargs:
            save_kwargs.update({key: value})

    def decodeargs(function: Callable):

        @wraps(function)
        def wrapper(*args, file_path: str | Path, force: bool = False, **kwargs):

            file_path = Path(file_path)
            # Load from cache if desired and applicable
            if file_path.is_file() and not force:
                with file_path.open('rb') as fp:
                    try:
                        return load_function(fp, **load_kwargs)
                    except Exception as e:
                        logging.exception(
                            f'Failed to load object from pickle file: {file_path}',
                            exc_info=e,
                        )

            # Compute if cached file does not exist or fails to successfully load
            output = function(*args, **kwargs)

            # Cache results to a file
            with file_path.open('wb') as fp:
                save_function(fp, output, **save_kwargs)

            return output

        return wrapper

    return decodeargs


# TODO: substitute placeholder package name


##
# @example pickle_cache.py
# This is an example of how to use the example_library.cache.pickle_cache method.
# More details about this example.
def pickle_cache(function: Callable):
    """Enable serialized caching of Python objects

    Extend another function's behavior by introducing serialized caching via `pickle` python standard library.

    @param function  Function which caching is desired.
    @return  Numpy array object(s)

    Examples:
    - @ref pickle_cache.py
    """

    @wraps(function)
    def wrapper(*args, file_path: str | Path, force: bool = False, **kwargs):
        file_path = Path(file_path)
        # Load from cache
        if file_path.is_file() and not force:
            with file_path.open('rb') as fp:
                try:
                    return load(fp)
                except Exception as e:
                    logging.exception(
                        f'Failed to load object from pickle file: {file_path}',
                        exc_info=e,
                    )
        output = function(*args, **kwargs)
        with file_path.open('wb') as fp:
            dump(output, fp)
        return output

    return wrapper
