from datetime import datetime  # noqa: F401

import datazimmer as dz


class CovidVictim(dz.BaseEntity):
    pass


class Condition(dz.CompositeTypeBase):
    lungs = bool
    heart = bool
    blood_pressure = bool
    diabetes = bool
    obesity = bool


class CovidVictimFeatures(dz.TableFeaturesBase):
    age = int
    estimated_date = datetime
    is_male = bool
    raw_conditions = str
    condition = Condition
    positive_rate = float
    total_vaccinations = int
    people_vaccinated = int
    people_fully_vaccinated = int
    total_boosters = int


class CovidVictimIndex(dz.IndexBase):
    serial = int


covid_victim_table = dz.ScruTable(features=CovidVictimFeatures, subject_of_records=CovidVictim, index=CovidVictimIndex)
