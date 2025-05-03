from typing import Any, TypeVar

import polars as pl

__all__ = [
    'row',
    'get_column',
]

T = TypeVar('T')


def row(
    frame: pl.DataFrame | pl.LazyFrame,
    index: int | None = None,
    by_predicate: pl.Expr | None = None,
    named: bool = False,
) -> tuple[Any, ...] | dict[str, Any]:
    """Get the values of a single row, either by index or by predicate.

    @param frame  The DataFrame/LazyFrame to get the row from.
    @param index  The index of the row to get.
    @param by_predicate  A predicate to filter the row by.
    @param named  Whether to return a dictionary.
    """
    if index is not None and abs(index) >= len(frame):
        return dict() if named else tuple()
    return frame.row(index=index, by_predicate=by_predicate, named=named)


def get_column(
    frame: pl.DataFrame | pl.LazyFrame,
    name: str,
    default: T = NotImplemented,
) -> pl.Series | T:
    """Get a single column by name.

    If the column is not found, the default value is returned.
    If the default value is not provided, the method raises an exception.

    @param frame  The DataFrame/LazyFrame to get the column from.
    @param name  The name of the column to get.
    @param default  The default value to return if the column is not found.
    @return  The column as a polars Series. Or, the default value if the column is not found.
    """
    try:
        return frame.get_column(name)
    except pl.exceptions.ColumnNotFoundError as e:
        if default is NotImplemented:
            raise e
        return default
