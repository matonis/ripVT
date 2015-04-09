#!/usr/bin/env python

from canari.maltego.entities import EntityField, Entity


class BinaryEntity(Entity):
    _namespace_ = u'binary'

@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'not_after', propname=u'notafter', displayname=None)
@EntityField(name=u'properties.certificate', propname=u'propertiescertificate', displayname=u'Certificate')
@EntityField(name=u'serial', propname=u'serial', displayname=None)
@EntityField(name=u'issuer', propname=u'issuer', displayname=None)
@EntityField(name=u'not_before', propname=u'notbefore', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
@EntityField(name=u'subject', propname=u'subject', displayname=None)
class Certificate(BinaryEntity):
    pass


@EntityField(name=u'properties.ssdeep', propname=u'propertiesssdeep', displayname=u'PE: SSDeep')
class pessdeep(BinaryEntity):
    pass


@EntityField(name=u'properties.export', propname=u'propertiesexport', displayname=u'PE: Export')
class Export(BinaryEntity):
    pass


@EntityField(name=u'md5_decrypted', propname=u'md5decrypted', displayname=None)
@EntityField(name=u'sha256_decrypted', propname=u'sha256decrypted', displayname=None)
@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'versions', propname=u'versions', displayname=None)
@EntityField(name=u'sha1_decrypted', propname=u'sha1decrypted', displayname=None)
@EntityField(name=u'properties.richheader', propname=u'propertiesrichheader', displayname=u'PE: Rich Header')
@EntityField(name=u'sha512_decrypted', propname=u'sha512decrypted', displayname=None)
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
@EntityField(name=u'sha512', propname=u'sha512', displayname=None)
@EntityField(name=u'ssdeep_decrypted', propname=u'ssdeepdecrypted', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
class peRich(BinaryEntity):
    pass


@EntityField(name=u'size', propname=u'size', displayname=None)
@EntityField(name=u'issuer_serial', propname=u'issuerserial', displayname=None)
@EntityField(name=u'certs', propname=u'certs', displayname=None)
@EntityField(name=u'counter_head_before', propname=u'counterheadbefore', displayname=None)
@EntityField(name=u'issuer', propname=u'issuer', displayname=None)
@EntityField(name=u'countersignature', propname=u'countersignature', displayname=None)
@EntityField(name=u'counter_head_after', propname=u'counterheadafter', displayname=None)
@EntityField(name=u'source', propname=u'source', displayname=None)
@EntityField(name=u'program', propname=u'program', displayname=None)
@EntityField(name=u'counter_head_issuer', propname=u'counterheadissuer', displayname=None)
@EntityField(name=u'before', propname=u'before', displayname=None)
@EntityField(name=u'sha512', propname=u'sha512', displayname=None)
@EntityField(name=u'chain_head', propname=u'chainhead', displayname=None)
@EntityField(name=u'counter_head_serial', propname=u'counterheadserial', displayname=None)
@EntityField(name=u'timestamp', propname=u'timestamp', displayname=None)
@EntityField(name=u'after', propname=u'after', displayname=None)
@EntityField(name=u'chain_head_serial', propname=u'chainheadserial', displayname=None)
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'properties.pecertificate', propname=u'propertiespecertificate', displayname=u'PE: Certificate')
@EntityField(name=u'url', propname=u'url', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
class peCert(BinaryEntity):
    pass


@EntityField(name=u'properties.import', propname=u'propertiesimport', displayname=u'PE: Import')
class peImport(BinaryEntity):
    pass


@EntityField(name=u'subsystem', propname=u'subsystem', displayname=None)
@EntityField(name=u'section_headers', propname=u'sectionheaders', displayname=None)
@EntityField(name=u'dos_header_attributes', propname=u'dosheaderattributes', displayname=None)
@EntityField(name=u'file_name', propname=u'filename', displayname=None)
@EntityField(name=u'exports', propname=u'exports', displayname=None)
@EntityField(name=u'rich_attributes', propname=u'richattributes', displayname=None)
@EntityField(name=u'yara_hits', propname=u'yarahits', displayname=None)
@EntityField(name=u'file_header_attributes', propname=u'fileheaderattributes', displayname=None)
@EntityField(name=u'timedatestamp', propname=u'timedatestamp', displayname=None)
@EntityField(name=u'count_directory_entries', propname=u'countdirectoryentries', displayname=None)
@EntityField(name=u'rich_header', propname=u'richheader', displayname=None)
@EntityField(name=u'dos_exe_stub', propname=u'dosexestub', displayname=None)
@EntityField(name=u'count_resources', propname=u'countresources', displayname=None)
@EntityField(name=u'section_attributes', propname=u'sectionattributes', displayname=None)
@EntityField(name=u'size', propname=u'size', displayname=None)
@EntityField(name=u'machine', propname=u'machine', displayname=None)
@EntityField(name=u'entrypoint', propname=u'entrypoint', displayname=None)
@EntityField(name=u'details', propname=u'details', displayname=None)
@EntityField(name=u'characteristics', propname=u'characteristics', displayname=None)
@EntityField(name=u'count_exports', propname=u'countexports', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
@EntityField(name=u'sha512', propname=u'sha512', displayname=None)
@EntityField(name=u'resources', propname=u'resources', displayname=None)
@EntityField(name=u'pe_type', propname=u'petype', displayname=None)
@EntityField(name=u'peid', propname=u'peid', displayname=None)
@EntityField(name=u'file_header', propname=u'fileheader', displayname=None)
@EntityField(name=u'properties.pecofffile', propname=u'propertiespecofffile', displayname=u'PECOFF: File')
@EntityField(name=u'imphash', propname=u'imphash', displayname=None)
@EntityField(name=u'count_sections', propname=u'countsections', displayname=None)
@EntityField(name=u'dos_header', propname=u'dosheader', displayname=None)
@EntityField(name=u'authenticode_attributes', propname=u'authenticodeattributes', displayname=None)
@EntityField(name=u'count_imports', propname=u'countimports', displayname=None)
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'debug_attributes', propname=u'debugattributes', displayname=None)
@EntityField(name=u'arch', propname=u'arch', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'sections', propname=u'sections', displayname=None)
@EntityField(name=u'optional_header', propname=u'optionalheader', displayname=None)
@EntityField(name=u'imports', propname=u'imports', displayname=None)
@EntityField(name=u'signed', propname=u'signed', displayname=None)
@EntityField(name=u'pehash', propname=u'pehash', displayname=None)
@EntityField(name=u'directory_entries', propname=u'directoryentries', displayname=None)
@EntityField(name=u'dos_exe_stub_properties', propname=u'dosexestubproperties', displayname=None)
@EntityField(name=u'debug', propname=u'debug', displayname=None)
class PEFile(BinaryEntity):
    pass


class RobertliaukusEntity(Entity):
    _namespace_ = u'robertliaukus'

@EntityField(name=u'properties.asdf', propname=u'propertiesasdf', displayname=u'asdf')
class asdf(RobertliaukusEntity):
    pass


@EntityField(name=u'properties.imphash', propname=u'propertiesimphash', displayname=u'PE: Imphash')
class peImphash(BinaryEntity):
    pass


@EntityField(name=u'size', propname=u'size', displayname=None)
@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'properties.pesection', propname=u'propertiespesection', displayname=u'PE: Section')
@EntityField(name=u'sect_name', propname=u'sectname', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
class PESection(BinaryEntity):
    pass


@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'language', propname=u'language', displayname=None)
@EntityField(name=u'properties.resource', propname=u'propertiesresource', displayname=u'PE: Resource')
@EntityField(name=u'sha512', propname=u'sha512', displayname=None)
@EntityField(name=u'sublanguage', propname=u'sublanguage', displayname=None)
@EntityField(name=u'res_name', propname=u'resname', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'yara_hits', propname=u'yarahits', displayname=None)
@EntityField(name=u'type', propname=u'type', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
@EntityField(name=u'size', propname=u'size', displayname=None)
class peResource(BinaryEntity):
    pass


@EntityField(name=u'properties.pehash', propname=u'propertiespehash', displayname=u'PE: peHash')
class peHash(BinaryEntity):
    pass


@EntityField(name=u'size', propname=u'size', displayname=None)
@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'struct_name', propname=u'structname', displayname=None)
@EntityField(name=u'properties.directoryentry', propname=u'propertiesdirectoryentry', displayname=u'PE: Directory Entry')
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
@EntityField(name=u'sha512', propname=u'sha512', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
class DirectoryEntry(BinaryEntity):
    pass


@EntityField(name=u'machine', propname=u'machine', displayname=None)
@EntityField(name=u'package', propname=u'package', displayname=None)
@EntityField(name=u'tags', propname=u'tags', displayname=None)
@EntityField(name=u'custom', propname=u'custom', displayname=None)
@EntityField(name=u'priority', propname=u'priority', displayname=None)
@EntityField(name=u'platform', propname=u'platform', displayname=None)
@EntityField(name=u'clock', propname=u'clock', displayname=None)
@EntityField(name=u'properties.cuckooanalysishash', propname=u'propertiescuckooanalysishash', displayname=u'Cuckoo Analysis Hash')
@EntityField(name=u'enforce_timeout', propname=u'enforcetimeout', displayname=None)
@EntityField(name=u'timeout', propname=u'timeout', displayname=None)
@EntityField(name=u'memory', propname=u'memory', displayname=None)
@EntityField(name=u'as_filename', propname=u'asfilename', displayname=None)
@EntityField(name=u'options', propname=u'options', displayname=None)
class CuckooHash(RobertliaukusEntity):
    pass


class MalformityEntity(Entity):
    _namespace_ = u'malformity'

@EntityField(name=u'properties.filename', propname=u'propertiesfilename', displayname=u'Filename')
class Filename(MalformityEntity):
    pass


@EntityField(name=u'properties.hash', propname=u'propertieshash', displayname=u'Hash')
@EntityField(name=u'Additional Hash', propname=u'AdditionalHash', displayname=None)
@EntityField(name=u'AV Name', propname=u'AVName', displayname=None)
@EntityField(name=u'Filename', propname=u'Filename', displayname=None)
class Hash(MalformityEntity):
    pass


class VirustotalEntity(Entity):
    _namespace_ = u'virustotal'

@EntityField(name=u'file_type', propname=u'filetype', displayname=None)
@EntityField(name=u'submission_names', propname=u'submissionnames', displayname=None)
@EntityField(name=u'scan_date', propname=u'scandate', displayname=None)
@EntityField(name=u'first_seen', propname=u'firstseen', displayname=None)
@EntityField(name=u'times_submitted', propname=u'timessubmitted', displayname=None)
@EntityField(name=u'additional_info', propname=u'additionalinfo', displayname=None)
@EntityField(name=u'size', propname=u'size', displayname=None)
@EntityField(name=u'total', propname=u'total', displayname=None)
@EntityField(name=u'harmless_votes', propname=u'harmlessvotes', displayname=None)
@EntityField(name=u'malicious_votes', propname=u'maliciousvotes', displayname=None)
@EntityField(name=u'machine', propname=u'machine', displayname=None)
@EntityField(name=u'json', propname=u'json', displayname=None)
@EntityField(name=u'parents', propname=u'parents', displayname=None)
@EntityField(name=u'imports', propname=u'imports', displayname=None)
@EntityField(name=u'entrypoint', propname=u'entrypoint', displayname=None)
@EntityField(name=u'sha256', propname=u'sha256', displayname=None)
@EntityField(name=u'sections', propname=u'sections', displayname=None)
@EntityField(name=u'properties.vtfile', propname=u'propertiesvtfile', displayname=u'VT File')
@EntityField(name=u'scans', propname=u'scans', displayname=None)
@EntityField(name=u'tags', propname=u'tags', displayname=None)
@EntityField(name=u'imphash', propname=u'imphash', displayname=None)
@EntityField(name=u'unique_sources', propname=u'uniquesources', displayname=None)
@EntityField(name=u'positives', propname=u'positives', displayname=None)
@EntityField(name=u'ssdeep', propname=u'ssdeep', displayname=None)
@EntityField(name=u'md5', propname=u'md5', displayname=None)
@EntityField(name=u'permalink', propname=u'permalink', displayname=None)
@EntityField(name=u'sha1', propname=u'sha1', displayname=None)
@EntityField(name=u'sigcheck', propname=u'sigcheck', displayname=None)
@EntityField(name=u'community_reputation', propname=u'communityreputation', displayname=None)
@EntityField(name=u'behavior_data', propname=u'behaviordata', displayname=None)
@EntityField(name=u'resources', propname=u'resources', displayname=None)
@EntityField(name=u'behavioral', propname=u'behavioral', displayname=None)
@EntityField(name=u'itw_urls', propname=u'itwurls', displayname=None)
@EntityField(name=u'last_seen', propname=u'lastseen', displayname=None)
class vtfilereport(VirustotalEntity):
    pass


class RipvtEntity(Entity):
    _namespace_ = u'ripVT'

@EntityField(name=u'properties.vtdetections', propname=u'propertiesvtdetections', displayname=u'VT Detections')
class VTDetections(RipvtEntity):
    pass


