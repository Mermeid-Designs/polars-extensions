import polars as pl

import polars_extensions.utils.null as null


@pl.api.register_lazyframe_namespace('nulls')
class Null:
    def __init__(self, ldf: pl.LazyFrame):
        self._ldf = ldf

    def drop_null_rows(
        self, *, subset: str | list[str] | type[pl.DataType] | None = None
    ) -> pl.LazyFrame:
        return null.drop_null_rows(self._ldf, subset=subset)

    def drop_null_columns(self, *, nested_nulls: bool) -> pl.LazyFrame:
        return null.drop_null_columns(self._ldf, nested_nulls=nested_nulls)
