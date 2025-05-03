from typing import overload

import polars as pl
import polars.selectors as cs

__all__ = [
    'drop_null_rows',
    'drop_null_columns',
]


@overload
def drop_null_rows(
    frame: pl.DataFrame, *, subset: str | list[str] | type[pl.DataType] | None = None
) -> pl.DataFrame: ...


@overload
def drop_null_rows(
    frame: pl.LazyFrame, *, subset: str | list[str] | type[pl.DataType] | None = None
) -> pl.LazyFrame: ...


def drop_null_rows(
    frame: pl.DataFrame | pl.LazyFrame,
    *,
    subset: str | list[str] | type[pl.DataType] | None = None,
) -> pl.DataFrame | pl.LazyFrame:

    if (subset or None) is None:
        return frame.filter(~pl.all_horizontal(pl.all().is_null()))
    return frame.filter(~pl.all_horizontal(pl.col(subset).is_null()))


@overload
def drop_null_columns(frame: pl.DataFrame, *, nested_nulls: bool) -> pl.DataFrame: ...


@overload
def drop_null_columns(frame: pl.LazyFrame, *, nested_nulls: bool) -> pl.LazyFrame: ...


def drop_null_columns(
    frame: pl.DataFrame | pl.LazyFrame, *, nested_nulls: bool
) -> pl.DataFrame | pl.LazyFrame:
    if not nested_nulls:
        return frame.select(~cs.by_dtype(pl.Null))
    return frame.select(
        ~cs.by_name(
            [
                name
                for name, dtype in frame.schema.items()
                if pl.Null in pl.datatypes.unpack_dtypes(dtype)
            ]
        )
    )
