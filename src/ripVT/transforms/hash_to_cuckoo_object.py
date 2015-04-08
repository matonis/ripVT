#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,PEFile,vtfilereport,CuckooHash
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
    label='Convert to Cuckoo Object',
    description='Convert hash to Cuckoo object for control of cuckoo sessions.',
    uuids=[ 'ripVT.v2.2cuckoo_hash','ripVT.v2.2cuckoo_ripfile','ripVT.v2.2cuckoo_from_report' ],
    inputs=[ ( 'ripVT', Hash ),( 'ripVT', PEFile ),('ripVT', vtfilereport) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    r=CuckooHash(str(request.value))
    r.linklabel="hash->cuckooEnt"
    response+=r

    return response