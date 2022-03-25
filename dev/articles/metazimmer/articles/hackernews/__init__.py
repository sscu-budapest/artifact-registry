from datetime import datetime  # noqa: F401

import datazimmer as dz


class Post(dz.BaseEntity):
    pass


class PostFeatures(dz.TableFeaturesBase):
    post_id = str
    rank = int
    title = str
    link = str
    sitebit = str
    posted = str
    score = int
    poster = str
    comments = int
    collected = datetime


post_table = dz.ScruTable(features=PostFeatures, subject_of_records=Post, max_partition_size=10000)
