#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,peImphash
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
    label='[ripVT] - Search Imphash (VT)',
    description='Searches Virus Total for hits matching an import hash',
    uuids=[ 'ripVT.v2.imphash2vt' ],
    inputs=[ ( 'ripVT', peImphash ) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search_param='imphash:"%s"' % str(request.value)

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="imphash->VT"
            response+=r

    return response
