"""
This is a boilerplate pipeline 'data_formating'
generated using Kedro 0.18.14
"""
# import typing
import os
import logging
import pandas as pd


def set_columns_as_date(dataset: pd.DataFrame) -> pd.DataFrame :
    """Select all the columns of type oject of de dataframe and \n
    try to convert them in a datetime format type.

    Args:
        dataset (pd.DataFrame): _The dataframe those date columns should be converted_

    Returns:
        pd.DataFrame: _The dataframe with date columns converted_
    """
    df = dataset
    cols = df.select_dtypes(include=['object']).columns
    logger = logging.getLogger(__name__)
    for col in cols:
        try:
            logger.info("Converting %s as datetime.", col)
            df[col] = pd.to_datetime(df[col], utc=True)
        except ValueError as ve:
            logger.error("%s: One of Y, M, D is missing", ve)
    return df


def convert_to_parquet(**kwargs) -> None:
    """convert the given file to a parquet file.

    Args:
        data (str): Name of the dataset as defined in the catalog
    """
    logger = logging.getLogger(__name__)
    for name, item in kwargs.items():
        filename = str(name + ".parquet")
        try:
            logger.info("Converting %s in parquet format.", filename)
            item.to_parquet(os.path.join("data/02_intermediate", filename))
        except AttributeError as e:
            logger.error("Error occured : %s", e)
