"""Feature selection and preparation."""

import argparse

import pandas as pd

import config
import operations


def feat_engineer_data(should_write: bool, drop_score: bool) -> pd.DataFrame:
    """Feat engineer the cleaned data provided.

    Args:
        should_write (bool): if True, saves the DataFrame as PKL file.
        drop_score (bool): if True, ignore the Energy Star variable.

    Returns:
        DataFrame: the cleaned DataFrame
    """

    return pd.DataFrame()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Feature engineering on the DataFrame, writing operation is allowed.",
    )

    args = parser.parse_args()
    feat_engineer_data()
