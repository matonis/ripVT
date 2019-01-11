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
    label='[ripVT] - Report to File Names',
    description='Translate Report to Filenames.',
    uuids=[ 'ripVT.v2.report2filenames'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    submission_names=ast.literal_eval(request.fields['submission_names'])

    for name in submission_names:
        if not name == "vti-rescan":
            try:
                tmp_name=name.encode('utf-8')
                r=Filename(tmp_name)
            except:
                r=Filename("HEXENC-%s" % (str(name).encode("hex")))
            r.linklabel="vtrep->names"
            response+=r

    return response