#!/usr/bin/env python

from canari.maltego.entities import Domain
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import TimeDateStamp,Hash
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
    label='[ripVT] - Search Compile Time',
    description='Searches Virus Total information related to domain.',
    uuids=[ 'ripVT.v2.search_pets' ],
    inputs=[ ( 'ripVT', TimeDateStamp ),],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search=str("pets:%s" % request.value)

    hits=search_vt(search)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="pets->vt"
            response+=r

    return response