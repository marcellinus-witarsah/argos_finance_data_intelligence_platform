from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame
from argos_finance_data_intelligence_platform import taxis


def test_find_all_taxis():
    results = taxis.find_all_taxis()
    assert results.count() > 5
