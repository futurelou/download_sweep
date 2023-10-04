# This project is still under development
# download_sweep

A framework for downloading end of day data and sweeping to different destination directories on different servers. It has the ability to compress and decompress files as well a perform md5 checks in order to stop redundant file tranfers. This framework will leverage exsisting utilities such as wget, sftp, ftp, rsync etc...

## Getting Started

Rules for downloading and sweeping files are stored in a database table in the form of URL.

### Prerequisites

The things you need before installing the software.

import tarfile 
from tqdm import tqdm <br />
import os <br />
import zipfile <br />
import hashlib <br />
from db_handler import MsSQL <br />
import pysftp <br />
import wget <br />



