#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import vtfilereport
from canari.maltego.entities import Phrase
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
    label='[ripVT] - Behavioral to Mutex (created)',
    description='Extracts mutexes from sandbox.',
    uuids=[ 'ripVT.v2.b2mut'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    if request.fields['behavioral']!= "false":
        behavior=ast.literal_eval(request.fields['behavior_data'])
        if behavior.has_key("mutex"):
            if behavior['mutex'].has_key('created'):
                for mutex in behavior['mutex']['created']:
                    r=Phrase(mutex['mutex'])
                    r.linklabel="behav->mutex_created"
                    response+=r

    else:
        debug("ripVT: No behavioral for %s" % request.value)
    return response