from datetime import datetime  # noqa: F401

import datazimmer as dz


class NepInclusion(dz.BaseEntity):
    pass


class NepIssue(dz.BaseEntity):
    pass


class Nep(dz.BaseEntity):
    pass


class Paper(dz.BaseEntity):
    pass


class NepIssueIndex(dz.IndexBase):
    neid = str


class NepFeatures(dz.TableFeaturesBase):
    title = str
    info = str


class NepIndex(dz.IndexBase):
    nid = str


class PaperFeatures(dz.TableFeaturesBase):
    link = str


class PaperIndex(dz.IndexBase):
    pid = str


class NepInclusionFeatures(dz.TableFeaturesBase):
    paper = PaperIndex


class NepInclusionIndex(dz.IndexBase):
    ind = int
    issue = NepIssueIndex


class NepIssueFeatures(dz.TableFeaturesBase):
    nep = NepIndex
    published = datetime


nep_inclusion_table = dz.ScruTable(
    features=NepInclusionFeatures, subject_of_records=NepInclusion, index=NepInclusionIndex
)
nep_issue_table = dz.ScruTable(features=NepIssueFeatures, subject_of_records=NepIssue, index=NepIssueIndex)
nep_table = dz.ScruTable(features=NepFeatures, subject_of_records=Nep, index=NepIndex)
paper_table = dz.ScruTable(features=PaperFeatures, subject_of_records=Paper, index=PaperIndex)
