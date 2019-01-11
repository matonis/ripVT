#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,Filename
from canari.maltego.entities import Phrase,Domain,IPv4Address,URL
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
    label='[ripVT] - Search ITW (VT)',
    description='Searches Virus Total for hits ITW',
    uuids=[ 'ripVT.v2.itw2vt_phrase','ripVT.v2.itw2vt_domain','ripVT.v2.itw2vt_ipv4','ripVT.v2.itw2vt_url','ripVT.v2.itw2vt_filename' ],
    inputs=[ ( 'ripVT', Phrase ),( 'ripVT', Domain ),( 'ripVT', IPv4Address ),( 'ripVT', URL ),('ripVT', Filename) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search_param='itw:"%s"' % str(request.value)

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="itw->VT"
            response+=r

    return response
