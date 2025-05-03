from typing import Any, TypeVar

import polars as pl
import utils.custom

T = TypeVar('T')


@pl.api.register_dataframe_namespace('custom')
class Custom:
    def __init__(self, df: pl.DataFrame):
        self._df = df

    def row(
        self,
        index: int | None = None,
        by_predicate: pl.Expr | None = None,
        named: bool = False,
    ) -> tuple[Any, ...] | dict[str, Any]:
        return utils.custom.row(self._df, index, by_predicate, named)

    def get_column(self, name: str, default: T = NotImplemented) -> pl.Series | T:
        return utils.custom.get_column(self._df, name, default)
