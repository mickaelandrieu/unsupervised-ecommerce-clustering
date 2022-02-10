"""Clean Data : NaN, invalid and outliers."""

import argparse

import pandas as pd

import config
import operations


def clean_data() -> pd.DataFrame:
    """Clean the RAW data provided.

    Args:
        should_write (bool): if True, saves the DataFrame as CSV file.
        drop_score (bool): if True, drops the Energy Star column.

    Returns:
        DataFrame: the cleaned DataFrame
    """
    

    return pd.DataFrame()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Clean the DataFrame, writing operation is allowed.",
    )

    args = parser.parse_args()
    clean_data()
