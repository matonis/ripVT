#!/usr/bin/env python

from canari.maltego.entities import Domain
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import VTIPReport,Hash
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
    label='[ripVT] - Report to Resolutions',
    description='Parses report for resolutions.',
    uuids=[ 'ripVT.v2.ip_2_rep_resolutions'],
    inputs=[ ( 'ripVT', VTIPReport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        items=ast.literal_eval(request.fields['resolutions'])
    except:
        return response

    for item in items:
        last=item['last_resolved']
        host=item['hostname']

        r=Domain(host)
        r.linklabel=last
        response+=r

    return response
