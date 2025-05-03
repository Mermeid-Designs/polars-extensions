from pathlib import Path
from typing import IO

import polars as pl

import polars_extensions.utils.io as io


@pl.api.register_dataframe_namespace('io')
class IO:
    def __init__(self, df: pl.DataFrame):
        self._df = df

    def write_csv(
        self, path: str | Path | IO[str] | IO[bytes] | None = None, **kwargs
    ) -> str | None:
        return io.to_csv_compatible(self._df).write_csv(path, **kwargs)

    def write_json(
        self, path: str | Path | IO[str] | IO[bytes] | None = None, **kwargs
    ) -> str | None:
        return io.to_json_compatible(self._df).write_json(path, **kwargs)

    def write_ndjson(
        self, path: str | Path | IO[str] | IO[bytes] | None = None, **kwargs
    ) -> str | None:
        return io.to_json_compatible(self._df).write_ndjson(path, **kwargs)
