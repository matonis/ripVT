#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,PEFile,vtfilereport
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
    label='[ripVT] - Search Similiar-To (VT)',
    description='Searches Virus Total for hits similar-to source.',
    uuids=[ 'ripVT.v2.similar2vt','ripVT.v2.similar2vt_file','ripVT.v2.similar2vt_report' ],
    inputs=[ ( 'ripVT', Hash ), ( 'ripVT', PEFile ),('ripVT',vtfilereport)],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search_param='similar-to:"%s"' % str(request.value)

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            if request.fields.has_key('sha256'):
                if not hsh == request.fields['sha256']:
                    r=Hash(str(hsh))
                    r.linklabel="similar->VT"
                    response+=r
            else:
                r=Hash(str(hsh))
                r.linklabel="similar->VT"
                response+=r

    return response
