#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash,PEFile,vtfilereport
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
    label='Get File Report (VT)',
    description='Searches Virus Total for file report with all information.',
    uuids=[ 'ripVT.v2.full_report_hash','ripVT.v2.full_report_ripfile' ],
    inputs=[ ( 'ripVT', Hash ),( 'ripVT', PEFile ) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    search=str(request.value)
    hits=get_full_report(search)

    if hits:
        vt_obj=report_to_rentity(hits.encode('utf-8'))
        if vt_obj:
            response+=vt_obj


    return response