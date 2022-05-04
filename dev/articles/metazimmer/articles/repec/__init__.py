from datetime import datetime  # noqa: F401

import datazimmer as dz


class Author(dz.BaseEntity):
    pass


class Authorship(dz.BaseEntity):
    pass


class NepInclusion(dz.BaseEntity):
    pass


class NepIssue(dz.BaseEntity):
    pass


class Nep(dz.BaseEntity):
    pass


class Paper(dz.BaseEntity):
    pass


class AuthorFeatures(dz.TableFeaturesBase):
    name = str


class AuthorIndex(dz.IndexBase):
    aid = str


class AuthorshipFeatures(dz.TableFeaturesBase):
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
    year = dz.Nullable(float)
    abstract = dz.Nullable(str)
    title = str
    institution = dz.Nullable(str)


class PaperIndex(dz.IndexBase):
    pid = str


class AuthorshipIndex(dz.IndexBase):
    paper = PaperIndex
    author = AuthorIndex


class NepInclusionFeatures(dz.TableFeaturesBase):
    paper = PaperIndex


class NepInclusionIndex(dz.IndexBase):
    ind = int
    issue = NepIssueIndex


class NepIssueFeatures(dz.TableFeaturesBase):
    nep = NepIndex
    published = datetime


author_table = dz.ScruTable(features=AuthorFeatures, subject_of_records=Author, index=AuthorIndex)
authorship_table = dz.ScruTable(features=AuthorshipFeatures, subject_of_records=Authorship, index=AuthorshipIndex)
nep_inclusion_table = dz.ScruTable(
    features=NepInclusionFeatures, subject_of_records=NepInclusion, index=NepInclusionIndex
)
nep_issue_table = dz.ScruTable(features=NepIssueFeatures, subject_of_records=NepIssue, index=NepIssueIndex)
nep_table = dz.ScruTable(features=NepFeatures, subject_of_records=Nep, index=NepIndex)
paper_table = dz.ScruTable(features=PaperFeatures, subject_of_records=Paper, index=PaperIndex)
