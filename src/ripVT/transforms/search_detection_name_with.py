#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import VTDetections,Hash
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
    label='[ripVT] - Search Detection Name (engine included)',
    description='Searches Virus Total for hits matching detection. Assumes engine is in existing value delinated by ":"',
    uuids=[ 'ripVT.v2.search_detection_name_with'],
    inputs=[ ( 'ripVT', VTDetections )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        search="%s" % (''.join(request.value.split(":")[1:]))
        search_param='engines:"%s"' % str(search)
    except:
        debug("ripVT: Error - value not present in property.")
        return response

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="engines->VT"
            response+=r

    return response
