from datetime import datetime  # noqa: F401

import datazimmer as dz


class Download(dz.BaseEntity):
    pass


class DownloadFeatures(dz.TableFeaturesBase):
    timestamp = datetime
    country_code = str
    project_name = str
    package_version = str
    distribution_type = str
    installer_name = str
    installer_version = str
    python_implementation_name = str
    python_implementation_version = str
    sys_name = str
    sys_distro_name = str
    sys_distro_version = str
    cpu = str
    openssl_version = str
    setuptools_version = str


download_table = dz.ScruTable(features=DownloadFeatures, subject_of_records=Download)
