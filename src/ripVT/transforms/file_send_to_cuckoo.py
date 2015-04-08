#!/usr/bin/env python

from canari.maltego.entities import Phrase
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import CuckooHash
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
    label='Send task to Cuckoo',
    description='Sends task to cuckoo. If file not in repo, downloads and sends if permitted per ripVT.conf.',
    uuids=[ 'ripVT.v2.send_to_cuckoo'],
    inputs=[ ( 'ripVT', CuckooHash )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    params=dict()

    params['hash']=str(request.value)

    if request.fields.has_key("as_filename"):
        params['file_name']=str(request.fields['as_filename'])
    else:
        params['file_name']=params['hash']

    if request.fields.has_key("package"):
        params['package']=str(request.fields['package'])

    if request.fields.has_key("timeout"):
        params['timeout']=int(request.fields['timeout'])

    if request.fields.has_key("priority"):
        params['priority']=int(request.fields['priority'])

    if request.fields.has_key("options"):
        params['options']=str(request.fields['options'])

    if request.fields.has_key("machine"):
        params['machine']=str(request.fields['machine'])

    if request.fields.has_key("platform"):
        params['platform']=str(request.fields['platform'])

    if request.fields.has_key("tags"):
        params['tags']=str(request.fields['tags'])

    if request.fields.has_key("custom"):
        params['custom']=str(request.fields['custom'])

    if request.fields.has_key("memory"):
        params['memory']=str(request.fields['memory'])

    if params['timeout']:
        params['enforce_timeout']=True

    if request.fields.has_key("clock"):
        params['clock']=str(request.fields['clock'])

    task_id=send_to_cuckoo(params['hash'],params)
    r=Phrase(task_id)
    r.linklabel="cuckoo_analysis_id"
    response+=r

    return response