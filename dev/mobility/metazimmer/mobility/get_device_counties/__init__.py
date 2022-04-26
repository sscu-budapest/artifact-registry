from datetime import datetime  # noqa: F401

import datazimmer as dz


class DeviceCounty(dz.BaseEntity):
    pass


class DeviceCountyFeatures(dz.TableFeaturesBase):
    count = int
    rate = float


class DeviceCountyIndex(dz.IndexBase):
    device_id = str
    county = str


device_county_table = dz.ScruTable(
    features=DeviceCountyFeatures, subject_of_records=DeviceCounty, index=DeviceCountyIndex
)
