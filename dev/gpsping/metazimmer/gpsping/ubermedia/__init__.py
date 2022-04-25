from datetime import datetime  # noqa: F401

import datazimmer as dz


class Ping(dz.BaseEntity):
    pass


class Coordinates(dz.CompositeTypeBase):
    lon = float
    lat = float


class PingFeatures(dz.TableFeaturesBase):
    device_id = str
    datetime = datetime
    year_month = str
    dayofmonth = str
    loc = Coordinates


ping_table = dz.ScruTable(
    features=PingFeatures,
    subject_of_records=Ping,
    partitioning_cols=["year_month", "dayofmonth"],
    max_partition_size=2000000,
)
