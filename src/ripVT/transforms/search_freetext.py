#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Filename,Hash
from canari.maltego.entities import URL,Domain,IPv4Address,EmailAddress,Phrase
from common.ripVT import *

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
    label='Search Freetext (VT)',
    description='Searches Virus Total for hits matching an indexed string.',
    uuids=[ 'ripVT.v2.free_2_vt_Filename','ripVT.v2.free_2_vt_URL','ripVT.v2.free_2_vt_Domain','ripVT.v2.free_2_vt_IPv4Address','ripVT.v2.free_2_vt_EmailAddress','ripVT.v2.free_2_vt_Phrase'],
    inputs=[ ( 'ripVT', Filename ), ( 'ripVT', URL ),( 'ripVT', Domain ),( 'ripVT', IPv4Address ),( 'ripVT', EmailAddress ),( 'ripVT', Phrase ),],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search_param='"%s"' % str(request.value)

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="freetext->VT"
            response+=r

    return response
