#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,PESection
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
    label='[ripVT] - Search Section (VT)',
    description='Searches Virus Total for hits matching a section.',
    uuids=[ 'ripVT.v2.section2vt' ],
    inputs=[ ( 'ripVT', PESection ) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search_param='sectionmd5:"%s"' % str(request.fields['md5'])

    hits=search_vt(search_param)

    if hits:
        for hsh in hits:
            r=Hash(str(hsh))
            r.linklabel="section->VT"
            response+=r

    return response
