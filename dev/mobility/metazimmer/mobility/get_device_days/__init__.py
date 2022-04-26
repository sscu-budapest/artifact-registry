from datetime import datetime  # noqa: F401

import datazimmer as dz


class DeviceDay(dz.BaseEntity):
    pass


class DeviceDayFeatures(dz.TableFeaturesBase):
    am_count = int
    pm_count = int
    other_count = int


device_day_table = dz.ScruTable(
    features=DeviceDayFeatures, subject_of_records=DeviceDay, partitioning_cols=["year_month"]
)
