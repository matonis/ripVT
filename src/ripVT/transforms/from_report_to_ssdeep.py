#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import PEFile,vtfilereport,pessdeep
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
    label='[ripVT] - Report to SSDEEP',
    description='Get ssdeep from entity object.',
    uuids=[ 'ripVT.v2.to_ssdeep_pefile','ripVT.v2.to_ssdeep_filereport' ],
    inputs=[ ( 'ripVT', PEFile ),('ripVT', vtfilereport) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    r=pessdeep(request.fields['ssdeep'] + " 40")
    r.linklabel="ssdeep"
    response+=r

    return response