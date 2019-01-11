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
    label='[ripVT] - Behavioral to Network (all)',
    description='Extracts outbound connections from sandbox.',
    uuids=[ 'ripVT.v2.b2netall'],
    inputs=[ ( 'ripVT', vtfilereport )],
    remote=False,
    debug=True
)
def dotransform(request, response):
    
    if request.fields['behavioral']!= "":
        try:
            behavior=ast.literal_eval(request.fields['behavior_data'])
        except Exception as e:
            debug("Entity has no behavioral data")
            return response
        if behavior.has_key("network"):
            if behavior['network'].has_key('dns'):
                for item in behavior['network']['dns']:
                    host=Domain(item['hostname'])
                    host.linklabel="vt_behav->hosts"
                    response+=host
                    if item.has_key('ip'):
                        ip=IPv4Address(item['ip'])
                        ip.linklabel="vt_behav->hosts"
                        response+=ip
            if behavior['network'].has_key('tcp'):
                for item in behavior['network']['tcp']:
                    conn=item.split(":")
                    r=IPv4Address(conn[0])
                    r.linklabel="vt_behav->hosts_tcp (%s)" % str(conn[1])
                    response+=r
            if behavior['network'].has_key('udp'):
                for item in behavior['network']['udp']:
                    conn=item.split(":")
                    r=IPv4Address(conn[0])
                    r.linklabel="vt_behav->hosts_udp (%s)" % str(conn[1])
                    response+=r

            if behavior['network'].has_key('http'):
                for item in behavior['network']['http']:
                    r=URL(item['url'])
                    r.url=item['url']
                    r.linklabel="vt_behav->hosts_http (%s)" % item['method']
                    response+=r
    else:
        debug("ripVT: No behavioral for %s" % request.value)

    return response