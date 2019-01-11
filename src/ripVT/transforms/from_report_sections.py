#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import vtfilereport,PESection
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
    label='[ripVT] - Report to Sections',
    description='Translate Report to Sections.',
    uuids=[ 'ripVT.v2.report2sections'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        scans=ast.literal_eval(request.fields['sections'])
    except Exception as e:
        debug("ripVT: Couldn't read in value - either not present or other error. %s" % e)
        return response


    for section in scans:
        name=str(section[0])
        hash_val=str(section[-1])
        r=PESection(str(hash_val))
        r.md5=hash_val
        r.linklabel="%s" % name
        response+=r

    return response