#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import vtfilereport,peResource
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
    label='[ripVT] - Report to Resources',
    description='Translate Report to Resources.',
    uuids=[ 'ripVT.v2.report2resources'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        scans=ast.literal_eval(request.fields['resources'])
    except Exception as e:
        debug("ripVT: Couldn't read in value - either not present or other error. %s" % e)
        return response


    for resource in scans:
        r=peResource(str(resource))
        r.sha256=resource
        r.linklabel="rep->resource"
        response+=r

    return response