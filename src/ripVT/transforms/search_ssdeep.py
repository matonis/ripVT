#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,pessdeep
from common.ripVT import *
import urllib

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
    label='[ripVT] - Search SSDEEP (VT)',
    description='Searches Virus Total for hits matching ssdeep.',
    uuids=[ 'ripVT.v2.ssdeep2vt' ],
    inputs=[ ( 'ripVT', pessdeep ) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search_param='ssdeep:"%s"' % str(urllib.quote_plus(request.value))

    debug(search_param)
    
    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="ssdeep->VT"
            response+=r

    return response
