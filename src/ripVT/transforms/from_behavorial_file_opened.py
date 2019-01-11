#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Filename,vtfilereport
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
    label='[ripVT] - Behavioral to Opened Files (VT)',
    description='Extracts opened files from sandbox.',
    uuids=[ 'ripVT.v2.b2of'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    if request.fields['behavioral']!= "false":
        behavior=ast.literal_eval(request.fields['behavior_data'])
        if behavior.has_key("filesystem"):
            if behavior['filesystem'].has_key("opened"):
                for t_file in behavior['filesystem']['opened']:
                    r=Filename(t_file['path'])
                    r.linklabel="vt_behave->opened"
                    response+=r
    else:
        debug("ripVT: No behavioral for %s" % request.value)
    return response