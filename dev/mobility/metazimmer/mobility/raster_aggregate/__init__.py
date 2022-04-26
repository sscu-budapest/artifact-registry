from datetime import datetime  # noqa: F401

import datazimmer as dz


class RasterHour(dz.BaseEntity):
    pass


class RasterHourFeatures(dz.TableFeaturesBase):
    month = str
    count = int


class RasterHourIndex(dz.IndexBase):
    raster_id = str
    hour = datetime


raster_hour_table = dz.ScruTable(
    features=RasterHourFeatures, subject_of_records=RasterHour, index=RasterHourIndex, partitioning_cols=["month"]
)
