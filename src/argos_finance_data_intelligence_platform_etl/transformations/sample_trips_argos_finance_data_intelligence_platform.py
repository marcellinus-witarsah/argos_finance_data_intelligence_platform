from pyspark import pipelines as dp
from pyspark.sql.functions import col


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table
def sample_trips_argos_finance_data_intelligence_platform():
    return spark.read.table("samples.nyctaxi.trips")
