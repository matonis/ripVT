#!/usr/bin/env python

from canari.maltego.entities import Domain
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
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
    label='[WF] - Domain to Root',
    description='Returns root domain.',
    uuids=[ 'ripVT.v2.workflows'],
    inputs=[ ( 'Workflows', Domain )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    tmp=".".join(str(request.value).split(".")[-2:])

    response+=Domain(tmp)
    return response
