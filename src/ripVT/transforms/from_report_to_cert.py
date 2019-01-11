#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import vtfilereport,peCert
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
    label='[ripVT] - Report to Cert',
    description='Translate Report to Cert.',
    uuids=[ 'ripVT.v2.report2cert'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    try:
        scans=ast.literal_eval(request.fields['sigcheck'])
    except Exception as e:
        debug("ripVT: Couldn't read in value - either not present or other error. %s" % e)
        return response


    r=peCert(scans['signers'])
    r.certs=scans['signers details']
    r.linklabel="r->Cert"
    response+=r



    return response