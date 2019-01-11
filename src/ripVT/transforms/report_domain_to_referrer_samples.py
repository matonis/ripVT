#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import VTDomainReport,Hash
from common.ripVT import *
import ast

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
    label='[ripVT] - Report to Detected Domain-Embedded Samples',
    description='Parses report for downloaded samples.',
    uuids=[ 'ripVT.v2.domain_2_rep_det_referrer_samples'],
    inputs=[ ( 'ripVT', VTDomainReport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        items=ast.literal_eval(request.fields['detected_referrer_samples'])
    except:
        return response

    for item in items:
        sha256=item['sha256']

        r=Hash(sha256)
        response+=r

    return response
