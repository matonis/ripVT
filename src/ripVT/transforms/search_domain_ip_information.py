#!/usr/bin/env python

from canari.maltego.entities import IPv4Address
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import VTIPReport
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
    label='[ripVT] - Get IP Report',
    description='Searches Virus Total information related to IP.',
    uuids=[ 'ripVT.v2.get_ip_report' ],
    inputs=[ ( 'ripVT', IPv4Address ),],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search=str(request.value)
    hits=search_vt_ip(search)

    if hits:
        response+=hits


    return response