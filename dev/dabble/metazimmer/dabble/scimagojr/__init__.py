from datetime import datetime  # noqa: F401

import datazimmer as dz


class Journal(dz.BaseEntity):
    pass


class JournalFeatures(dz.TableFeaturesBase):
    rank = int
    journal_rating = float
    title = str
    type = str
    issn = str
    h_index = int
    total_docs_2020 = int
    ref_per_doc = float
    sjr_best_quartile = str
    total_docs_3years = int
    total_refs = int
    total_cites_3years = int
    citable_docs_3years = int
    country = str
    region = str
    publisher = str
    coverage = str
    categories = str


class JournalIndex(dz.IndexBase):
    sourceid = int


journal_table = dz.ScruTable(features=JournalFeatures, subject_of_records=Journal, index=JournalIndex)
