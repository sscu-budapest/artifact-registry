from datetime import datetime  # noqa: F401

import datazimmer as dz
import metazimmer.gpsping.ubermedia


class FilteredPing(dz.BaseEntity):
    pass


class FilteredPingFeatures(dz.TableFeaturesBase):
    device_id = str
    datetime = datetime
    year_month = str
    dayofmonth = str
    loc = metazimmer.gpsping.ubermedia.Coordinates


filtered_ping_table = dz.ScruTable(
    features=FilteredPingFeatures, subject_of_records=FilteredPing, partitioning_cols=["year_month", "dayofmonth"]
)
