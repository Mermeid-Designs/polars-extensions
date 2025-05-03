from pathlib import Path
from typing import IO

import polars as pl

import polars_extensions.utils.io as io


@pl.api.register_lazyframe_namespace('io')
class IO:
    def __init__(self, ldf: pl.LazyFrame):
        self._ldf = ldf

    def sink_csv(
        self,
        path: str | Path | IO[str] | IO[bytes] | pl.io.PartitioningScheme,
        **kwargs,
    ) -> str | None:
        return io.to_csv_compatible(self._ldf).write_csv(path, **kwargs)

    def sink_ndjson(
        self,
        path: str | Path | IO[str] | IO[bytes] | pl.io.PartitioningScheme,
        **kwargs,
    ) -> str | None:
        return io.to_json_compatible(self._ldf).sink_ndjson(path, **kwargs)
