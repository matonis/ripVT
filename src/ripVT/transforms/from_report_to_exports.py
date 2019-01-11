#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import PEFile,vtfilereport,Export
from common.ripVT import *
import json
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
    label='[ripVT] - Report to Exports',
    description='Get exports from entity object.',
    uuids=[ 'ripVT.v2.to_exports']  ,
    inputs=[ ( 'ripVT', vtfilereport ) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        exports=ast.literal_eval(request.fields['exports'])
        for e in exports:
            a=Export(str(e))
            response+=a
    except Exception as e:
        debug("ripVT: Couldn't read in value - either not present or other error. %s" % e)
        return response

    return response