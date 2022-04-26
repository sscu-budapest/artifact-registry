from datetime import datetime  # noqa: F401

import datazimmer as dz
import metazimmer.gpsping.ubermedia


class Stop(dz.BaseEntity):
    pass


class Arrival(dz.CompositeTypeBase):
    speed = float
    distance = float
    time = float


class Duration(dz.CompositeTypeBase):
    start = datetime
    end = datetime


class StopFeatures(dz.TableFeaturesBase):
    device_id = str
    year_month = str
    dayofmonth = str
    place_label = int
    stop_number = int
    n_events = int
    interval = Duration
    center = metazimmer.gpsping.ubermedia.Coordinates
    is_home = bool
    is_work = bool
    from_last_stop = Arrival
    from_last_ping = Arrival


stop_table = dz.ScruTable(
    features=StopFeatures, subject_of_records=Stop, partitioning_cols=["year_month", "dayofmonth"]
)
