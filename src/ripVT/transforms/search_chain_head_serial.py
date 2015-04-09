#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import peCert,Hash
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
    label='Search Chain Head Serial (VT)',
    description='Searches Virus Total for hits matching chain head serial string.',
    uuids=[ 'ripVT.v2.pecert_chain_serial_vt_search'],
    inputs=[ ( 'ripVT', peCert )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        search_param='sigcheck:"%s"' % str(request.fields['chain_head_serial'])
    except:
        debug("ripVT: Error - issuer serial not present in property.")
        return response

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="chain_serial->VT"
            response+=r

    return response
