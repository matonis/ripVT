#!/usr/bin/env python

from canari.config import config
from canari.maltego.message import MaltegoException
from canari.maltego.utils import debug, progress
from entities import vtfilereport,VTDomainReport,VTIPReport
from canari.maltego.entities import URL,Domain,IPv4Address,EmailAddress

import json
import os,sys
import requests
import re
import hashlib
import time
from copy import deepcopy

def search_vt_domain(search):

    search=search.lower()

    API_KEY=config['api_key/key']

    params = {'domain': search , 'apikey': API_KEY}
    response = requests.get('https://www.virustotal.com/vtapi/v2/domain/report', params=params)

    if response.status_code == 200:
        response_json = response.json()
        domain_entity=vt_domain_report_to_entity(search,response_json)
        return domain_entity
    else:
        debug("ripVT: received bad status code. %s" % response.status.code)
        return False

    response_json = response.json()

def search_vt_ip(search):

    API_KEY=config['api_key/key']

    params = {'ip': search , 'apikey': API_KEY}
    response = requests.get('https://www.virustotal.com/vtapi/v2/ip-address/report', params=params)
    response_json = response.json()

    if response.status_code == 200:
        ip_entity=vt_ip_report_to_entity(search,response_json)
        return ip_entity
    else:
        debug("ripVT: received bad status code. %s" % response.status.code)
        return False
        
    response_json = response.json()

def vt_domain_report_to_entity(search,t_json):

    if t_json['response_code'] == 0:
        debug("ripVT: Domain not found in VT repo.")
        return False

    e=VTDomainReport(str(search))
    if 'detected_communicating_samples' in t_json:
        e.detectedsamples=str(t_json['detected_communicating_samples']).encode('utf-8')
    if 'detected_downloaded_samples' in t_json:
        e.detecteddownloadedsamples=str(t_json['detected_downloaded_samples']).encode('utf-8')
    if 'detected_referrer_samples' in t_json:
        e.detectedreferrersamples=str(t_json['detected_referrer_samples']).encode('utf-8')
    if 'detected_urls' in t_json:
        e.detectedurls=str(t_json['detected_urls']).encode('utf-8')
    if 'resolutions' in t_json:
        e.resolutions=str(t_json['resolutions']).encode('utf-8')
    if 'subdomains' in t_json:
        e.subdomains=str(t_json['subdomains']).encode('utf-8')
    if 'pcaps' in t_json:
        e.pcaps=str(t_json['pcaps']).encode('utf-8')
    if 'undetected_communicating_samples' in t_json:
        e.undetectedcommunicatingsamples=str(t_json['undetected_communicating_samples']).encode('utf-8')
    if 'undetected_downloaded_samples' in t_json:
        e.undetecteddownloadedsamples=str(t_json['undetected_downloaded_samples']).encode('utf-8')
    if 'undetected_referrer_samples' in t_json:
        e.undetectedreferrersamples=str(t_json['undetected_referrer_samples']).encode('utf-8')

    return e

def vt_ip_report_to_entity(search,t_json):

    if t_json['response_code'] == 0:
        debug("ripVT: IP not found in VT repo.")
        return False

    e=VTIPReport(str(search))
    if 'as_owner' in t_json:
        e.asowner=str(t_json['as_owner']).encode('utf-8')
    if 'asn' in t_json:
        e.asn=str(t_json['asn']).encode('utf-8')
    if 'country' in t_json:
        e.country=str(t_json['country']).encode('utf-8')
    if 'detected_communicating_samples' in t_json:
        e.detectedcommunicatingsamples=str(t_json['detected_communicating_samples']).encode('utf-8')
    if 'detected_downloaded_samples' in t_json:
        e.detecteddownloadedsamples=str(t_json['detected_downloaded_samples']).encode('utf-8')
    if 'detected_referrer_samples' in t_json:
        e.detectedreferrersamples=str(t_json['detected_referrer_samples']).encode('utf-8')
    if 'detected_urls' in t_json:
        e.detectedurls=str(t_json['detected_urls']).encode('utf-8')
    if 'subdomains' in t_json:
        e.subdomains=str(t_json['subdomains']).encode('utf-8')
    if 'resolutions' in t_json:
        e.resolutions=str(t_json['resolutions']).encode('utf-8')
    if 'undetected_communicating_samples' in t_json:
        e.undetectedcommunicatingsamples=str(t_json['undetected_communicating_samples']).encode('utf-8')
    if 'undetected_downloaded_samples' in t_json:
        e.undetecteddownloadedsamples=str(t_json['undetected_downloaded_samples']).encode('utf-8')
    if 'undetected_referrer_samples' in t_json:
        e.undetectedreferrersamples=str(t_json['undetected_referrer_samples']).encode('utf-8')

    return e


def search_vt(search,offset=False):

    API_KEY=config['api_key/key']

    paginate=config['ripVT/paginate']

    if not offset:
        offset=''

    params = {'apikey': API_KEY, 'query': search, 'offset':offset}

    response = requests.get('https://www.virustotal.com/vtapi/v2/file/search', params=params)

    if response.status_code == 200:
        json_response=response.json()
        if json_response.has_key("hashes"):
            if len(json_response['hashes']) > 0:
                hashes=deepcopy(json_response['hashes'])
                if paginate == "True":
                    if 'offset' in json_response:
                        hashes+=search_vt(search,offset=json_response['offset'])
                    return hashes
                else:
                    return hashes
            else:
                debug("ripVT: No hits received.")
                return []
        else:
            debug("ripVT: no hash key received in response. External error.")
            return False
    else:
        debug("ripVT: received bad status code. %s" % response.status_code)
        return False

def get_full_report(hash_val):

    API_KEY=config['api_key/key']
    HASH=str(hash_val)

    params = {'apikey': API_KEY, 'resource': HASH, 'allinfo': 1}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        debug("ripVT: received bad status code. %s" % response.status_code)
        return False

def report_to_rentity(tmp_json):

    try:
        t_json=json.loads(tmp_json)
    except Exception as e:
        debug("ripVT: Couldn't decode json. Huh? %s" % e)
        return False

    if t_json['response_code'] == 0:
        debug("ripVT: File not found in VT repo.")
        return False

    e=vtfilereport(str(t_json['md5'].encode('utf-8')))
    #e.json=str(tmp_json).encode('utf-8')
    e.md5=str(t_json['md5']).encode('utf-8')
    e.sha1=str(t_json['sha1']).encode('utf-8')
    e.sha256=str(t_json['sha256']).encode('utf-8')
    e.ssdeep=str(t_json['ssdeep']).encode('utf-8')
    e.firstseen=str(t_json['first_seen']).encode('utf-8')
    e.lastseen=str(t_json['last_seen']).encode('utf-8')
    e.filetype=str(t_json['type']).encode('utf-8')
    e.size=str(t_json['size']).encode('utf-8')
    e.submissionnames=t_json['submission_names']
    e.permalink=str(t_json['permalink']).encode('utf-8')
    e.uniquesources=str(t_json['unique_sources']).encode('utf-8')
    e.total=str(t_json['total']).encode('utf-8')
    e.timessubmitted=str(t_json['times_submitted']).encode('utf-8')
    e.tags=str(t_json['tags']).encode('utf-8')
    e.scans=str(t_json['scans']).encode('utf-8')
    e.scandate=str(t_json['scan_date']).encode('utf-8')
    e.positives=str(t_json['positives']).encode('utf-8')
    e.maliciousvotes=str(t_json['malicious_votes']).encode('utf-8')
    e.harmlessvotes=str(t_json['harmless_votes']).encode('utf-8')
    e.communityreputation=str(t_json['community_reputation']).encode('utf-8')
    e.additionalinfo=t_json['additional_info']
    e.itwurls=str(t_json['ITW_urls']).encode('utf-8')

    if t_json.has_key('additional_info'):
        if t_json['additional_info'].has_key('compressed_parents'):
            e.parents=str(t_json['additional_info']['compressed_parents']).encode('utf-8')
        if t_json['additional_info'].has_key('sigcheck'):
            e.sigcheck=t_json['additional_info']['sigcheck']
        else:
            e.sigcheck=""

        if t_json['additional_info'].has_key('pe-imphash'):
            e.imphash=t_json['additional_info']['pe-imphash']
        else:
            e.imphash=""

        if t_json['additional_info'].has_key('pe-resource-list'):
            e.resources=t_json['additional_info']['pe-resource-list']
        else:
            e.resources=""

        if t_json['additional_info'].has_key('pe-entry-point'):
            e.entrypoint=t_json['additional_info']['pe-entry-point']
        else:
            e.entrypoint=""

        if t_json['additional_info'].has_key('sections'):
            e.sections=t_json['additional_info']['sections']
        else:
            e.sections=""

        if t_json['additional_info'].has_key('behaviour-v1'):
            e.behavioral=True
            e.behaviordata=str(t_json['additional_info']['behaviour-v1']).encode('utf-8')
        else:
            e.behavioral=False
            e.behavior_data=""

        if t_json['additional_info'].has_key('imports'):
            e.imports=t_json['additional_info']['imports']
        else:
            e.imports=""

        if t_json['additional_info'].has_key('exports'):
            e.exports=t_json['additional_info']['exports']
        else:
            e.imports=""

        if t_json['additional_info'].has_key('pe-timestamp'):
            e.compiled=time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(t_json['additional_info']['pe-timestamp']))
        else:
            e.imports=""

        if t_json['additional_info'].has_key('pe-machine-type'):
            e.machine=t_json['additional_info']['pe-machine-type']
        else:
            e.machine=""

    else:
        e.parents=""
        e.sigcheck=""
        e.imphash=""
        e.resources=""
        e.entrypoint=""
        e.sections=""
        e.behavioral=False
        e.behavior_data=""
        e.imports=""
        e.machine=""

    e.linklabel="F: %s - L: %s" % (e.firstseen,e.lastseen)

    return e

def detType(in_val):

    val=str(in_val)

    #::Email
    email=re.compile(".*\[@\][a-z0-9\-]{1,}\.[a-z0-9\-]{1,}")

    #::IP
    ipv4=re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    #::CIDR
    cidr=re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$")

    #::Range
    v4range=re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\-\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    #::Domain
    dom=re.compile("([a-z0-9\-]{1,}\.?)+\.[a-z0-9\-]{1,}$")

    if email.match(val):
        e=EmailAddress(val)
        return e

    if ipv4.match(val):
        e=IPv4Address(val)
        return e

    if cidr.match(val):
        e=CIDR(val)
        return e

    if v4range.match(val):
        e=Range(val)
        return e

    if dom.match(val):
        e=Domain(val)
        return e

    if re.match("^([a-z]*)://", val, re.M | re.I):
        e=URL(val)
        e.url=val
        return e

def get_file_name(hash_value):

    DOWNLOAD_DIR=os.path.expanduser(config['repo/path'])
    if not os.path.exists(DOWNLOAD_DIR):
        debug("ripVT: Repo dir does not exist.")
        return False

    for f in os.listdir(DOWNLOAD_DIR):
        tmp_f=f.split("-")
        if str(hash_value) in f:
            debug(f)
            return str(f)

def is_in_repo(hash_value):

    DOWNLOAD_DIR=os.path.expanduser(config['repo/path'])
    if not os.path.exists(DOWNLOAD_DIR):
        debug("ripVT: Repo dir does not exist.")
        return False

    for f in os.listdir(DOWNLOAD_DIR):
        tmp_f=f.split("-")
        if str(hash_value) in tmp_f:
            return True

    return False

def download_to_repo(hash_val):

    DOWNLOAD_DIR=os.path.expanduser(config['repo/path'])
    API_KEY=config['api_key/key']

    if not os.path.exists(DOWNLOAD_DIR):
        debug("ripVT: Repo dir does not exist.")
        return False

    if not str(hash_val) in os.listdir(DOWNLOAD_DIR):
        params = {'apikey': API_KEY, 'hash': str(hash_val)}
        try:
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/download', params=params)
        except Exception as e:
            debug("ripVT: Exception downloading file. %s" % e)
            return False

        if response.status_code == 200:
            try:
                content=response.content
                sha256=hashlib.sha256(content).hexdigest()
                md5=hashlib.md5(content).hexdigest()
                sha1=hashlib.sha1(content).hexdigest()
                repo_name="%s-%s-%s" % (sha256,sha1,md5)
                save_file=open(os.path.join(DOWNLOAD_DIR,str(repo_name)),'wb')
            except Exception as e:
                debug("ripVT: Couldn't open file for writing. %s" % e)
                return False
            try:
                save_file.write(content)
            except Exception as e:
                debug("ripVT: Couldn't write file. %s" % e)
                return False

            save_file.close()
            debug("ripVT: Successful saved %s to repo" % str(repo_name))
            return True
        else:
            debug("ripVT: Couldn't download file, received other status code. Try again as may be problem with VT store. %s" % response.status_code)
            return False
    else:
        debug("ripVT: File is already in repo.")
        return True

def send_to_cuckoo(repo_name,params):

    if str(config['cuckoo/url']) != "":
        CUCKOO_URL="%s/tasks/create/file" % str(config['cuckoo/url'])
    else:
        debug("ripVT: Cuckoo URL not set. Please set.")
        return False

    REPO=os.path.expanduser(config['repo/path'])
    PULL_OPTION=bool(config['ripVT/download_if_not_present'])

    def open_repo_file(name,repo):
        try:
            data=open(os.path.join(repo,str(name)),'rb')
            return data
        except Exception as e:
            debug("ripVT: Couldn't open repo file for reading. %s " % e)
            return False

    def post_to_cuckoo(raw_data,parameters):

        parameters.pop("hash",None)

        if not "." in parameters['file_name']:
            parameters['file_name']=parameters['file_name'] + ".exe"

        multipart_file = {"file": (parameters['file_name'], raw_data)}

        try:
            request = requests.post(CUCKOO_URL, files=multipart_file,data=parameters)
        except Exception as e:
            debug("ripVT: Couldn't post task to Cuckoo. Internal error: %s" % e)
            return False

        if request.status_code == 200:
            json_decoder = json.JSONDecoder()
            task_id = json_decoder.decode(request.text)["task_id"]
            return task_id
        else:
            debug("ripVT: Received bad status code from Cuckoo. Returning.")
            return False

    if is_in_repo(str(repo_name)):
        data=open_repo_file(get_file_name(repo_name),REPO)
        task_id=post_to_cuckoo(raw_data=data,parameters=params)
        return task_id
    else:
        if PULL_OPTION:
            debug("ripVT: File not found in repo, downloading to repo.")
            if download_to_repo(str(repo_name)):
                data=open_repo_file(get_file_name(repo_name),REPO)
                task_id=post_to_cuckoo(raw_data=data,parameters=params)
                debug("ripVT: Sent to cuckoo with task id: %s"  % task_id)
                return task_id
            else:
                debug("ripVT: Couldn't download to repo")
        else:
            debug("ripVT: File not found in repo. Returning.")
            return False

    
