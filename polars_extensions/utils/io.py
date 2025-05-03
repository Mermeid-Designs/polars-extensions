from typing import overload

import polars as pl


@overload
def to_csv_compatible(
    frame: pl.DataFrame,
) -> pl.DataFrame: ...


@overload
def to_csv_compatible(
    frame: pl.LazyFrame,
) -> pl.LazyFrame: ...


def to_csv_compatible(
    frame: pl.DataFrame | pl.LazyFrame,
) -> pl.DataFrame | pl.LazyFrame:
    """Convert polars DataFrame/LazyFrame into CSV-compatible data types

    Casts all non-CSV-compatible columns to strings.

    @param frame  The DataFrame/LazyFrame to convert
    @return  Successful CSV-compatible generation results
    """
    list_columns = [
        col for col, dtype in frame.schema.items() if isinstance(dtype, pl.List)
    ]
    array_columns = [
        col for col, dtype in frame.schema.items() if isinstance(dtype, pl.Array)
    ]
    struct_columns = [
        col for col, dtype in frame.schema.items() if isinstance(dtype, pl.Struct)
    ]

    return frame.with_columns(
        [
            # Convert objects to strings
            cs.object().cast(pl.Utf8),
            # Convert `Struct` types to dictionaries represented as strings
            #   e.g. {[9, 1, 3],null} -> '{"a":[9,1,3],"b":null} '
            pl.col(struct_columns).struct.json_encode(),
            # Convert `List` types to lists represented as strings
            #   e.g. [1, 2] -> "[1, 2]"
            '[' + pl.col(list_columns).cast(pl.List(pl.Utf8)).list.join(', ') + ']',
            # Convert `Array` types to lists represented as strings
            #   e.g. [1, 2] -> "[1, 2]"
            '[' + pl.col(array_columns).cast(pl.List(pl.Utf8)).list.join(', ') + ']',
        ]
    )


@overload
def to_json_compatible(
    frame: pl.DataFrame,
) -> pl.DataFrame: ...


@overload
def to_json_compatible(
    frame: pl.LazyFrame,
) -> pl.LazyFrame: ...


def to_json_compatible(
    frame: pl.DataFrame | pl.LazyFrame,
) -> pl.DataFrame | pl.LazyFrame:
    """Convert polars DataFrame/LazyFrame into JSON-compatible data types

    Drops all columns that are entirely null or entirely nested nulls.

    @param frame  The DataFrame/LazyFrame to convert
    @return  Successful JSON-compatible generation results
    """
    from .null import drop_null_columns

    return drop_null_columns(frame, nested_nulls=True)
