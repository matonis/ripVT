#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import PEFile,vtfilereport,peImphash
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
    label='Imphash from Entity',
    description='Get imphash from entity object.',
    uuids=[ 'ripVT.v2.to_imphash_pefile','ripVT.v2.to_imphash_filereport' ],
    inputs=[ ( 'ripVT', PEFile ),('ripVT', vtfilereport) ],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    r=peImphash(request.fields['imphash'])
    r.linklabel="to_imphash"
    response+=r

    return response