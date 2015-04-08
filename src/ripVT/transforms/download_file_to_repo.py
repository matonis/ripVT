#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,PEFile,vtfilereport
from common.ripVT import *
import json

__author__ = '@matonis'
__copyright__ = 'Copyright 2015, Ripvt Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = '@matonis'
__email__ = 'dfir.matonis@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]

@configure(
    label='Download File to Repo',
    description='Download selected file to repo.',
    uuids=[ 'ripVT.v2.download_hash','ripVT.v2.download_ripfile','ripVT.v2.download_from_report' ],
    inputs=[ ( 'ripVT', Hash ),( 'ripVT', PEFile ),('ripVT', vtfilereport) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    download_me=str(request.value)

    if download_to_repo(download_me):
        debug("ripVT: Successfully downloaded file to repo.")
    else:
        debug("ripVT: Couldn't download file to repo.")

    return response