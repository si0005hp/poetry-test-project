import pandas as pd
import pyarrow as pa


def read_parquet_as_list(path: str) -> list[dict]:
    df: pd.DataFrame = pd.read_parquet(path)
    return pa.Table.from_pandas(df).to_pylist()
