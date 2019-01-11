#!/usr/bin/env python

from canari.maltego.entities import Person
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import vtfilereport,peCert,Certificate
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
    label='[ripVT] - Report to Certs (Indiv)',
    description='Translate Report to Certs.',
    uuids=[ 'ripVT.v2.report2certsi'],
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


    for cert in scans['signers details']:
        name=cert['name']
        serial=cert['serial number']
        after=cert['valid from']
        before=cert['valid to']

        r=Certificate(name + "\n" + serial)
        r.serial=serial
        r.after=after
        r.before=before
        r.subject=name

        response+=r


    return response