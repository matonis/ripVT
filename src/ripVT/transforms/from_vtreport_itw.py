#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import vtfilereport
from canari.maltego.entities import URL,Domain,IPv4Address,EmailAddress
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
    label='[ripVT] - Report to ITW locations',
    description='Translate Report to ITW locations.',
    uuids=[ 'ripVT.v2.report2itwloc'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    urls=ast.literal_eval(request.fields['itw_urls'])


    for tmp_url in urls:
        e=URL(str(tmp_url))
        e.url = str(tmp_url)
        response+=e
        
    return response