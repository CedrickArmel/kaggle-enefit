"""
This is a boilerplate pipeline 'data_formating'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import set_columns_as_date, convert_to_parquet


def mapping(inputs: list[str]) -> dict[str, str]:
    """Helper function that creates a mapping value-value\n
    from value of the list for strings.

    Args:
        inputs (list): _Input list_

    Returns:
        dict: _The mapping_
    """
    return {k: k for k in inputs}


def create_pipeline(**kwargs) -> Pipeline:
    """_Returns a pipeline_

    Returns:
        Pipeline: _The pipeline_
    """
    return pipeline(
        [
            node(
                func=set_columns_as_date,
                inputs=['client'],
                outputs='cl',
                name="convert_date_columns_in_CL",
            ),
            node(
                func=set_columns_as_date,
                inputs=['electricity_prices'],
                outputs='ep',
                name="convert_date_columns_in_EP",
            ),
            node(
                func=set_columns_as_date,
                inputs=['forecast_weather'],
                outputs='fw',
                name="convert_date_columns_in_FW",
            ),
            node(
                func=set_columns_as_date,
                inputs='gas_prices',
                outputs='gp',
                name="convert_date_columns_in_GP",
            ),
            node(
                func=set_columns_as_date,
                inputs=['historical_weather'],
                outputs='hw',
                name="convert_date_columns_in_HW",
            ),
            node(
                func=set_columns_as_date,
                inputs=['train'],
                outputs='tr',
                name="convert_date_columns_in_TR",
            ),
            node(
                func=convert_to_parquet,
                inputs=mapping(["cl", "ep", "fw", "gp", "hw", "tr"]),
                outputs=None,
                name="convert_to_parquet",
            ),
        ]
    )
