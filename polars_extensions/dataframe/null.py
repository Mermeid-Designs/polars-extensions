import polars as pl

import polars_extensions.utils.null as null


@pl.api.register_dataframe_namespace('nulls')
class Null:
    def __init__(self, df: pl.DataFrame):
        self._df = df

    def drop_null_rows(
        self, *, subset: str | list[str] | type[pl.DataType] | None = None
    ) -> pl.DataFrame:
        return null.drop_null_rows(self._df, subset=subset)

    def drop_null_columns(self, *, nested_nulls: bool) -> pl.DataFrame:
        return null.drop_null_columns(self._df, nested_nulls=nested_nulls)
