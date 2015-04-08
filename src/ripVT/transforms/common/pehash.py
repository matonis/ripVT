#!/usr/bin/env python

from __future__ import division

import os,sys
import bz2
import hashlib
import bitstring
import binascii
import pefile

def get_pehash(pe_file):

	print "here"

	#::Interpreted from publication by Georg Wicherski::#
	#::https://www.usenix.org/legacy/event/leet09/tech/full_papers/wicherski/wicherski.pdf
	#::Playing with kolmogorov precision seems to increase strength of results in certain
	#::circumstances.

	hashes={'characteristics': int(),
			'subsystem' : int(),
			'stackcommit': int(),
			'heapcommit': int()
			}

	pehash_container=[]

	#::PE Header Properties::# 
	pe_characteristics=pe_file.FILE_HEADER.Characteristics #::Header: (WORD)
	pe_subsystem=pe_file.OPTIONAL_HEADER.Subsystem #::Header: (WORD)
	pe_stackcommit=pe_file.OPTIONAL_HEADER.SizeOfStackCommit #::Header (DWORD)
	pe_heapcommit=pe_file.OPTIONAL_HEADER.SizeOfHeapCommit #::Header (DWORD)

	#::FILE_HEADER.CHARACTERISTICS - Xor low word -> high word
	hashes['characteristics'] = (pe_characteristics & 0xFF) ^ ((pe_characteristics >> 8) & 0xFF)

	#::OPTIONAL_HEADER.Subsystem - Xor low word -> high word
	hashes['subsystem'] = (pe_subsystem & 0xFF) ^ ((pe_subsystem >> 8) & 0xFF)

	#::OPTIONAL_HEADER.SizeOfStackCommit - XOR each byte where 0xFFF0
	hashes['stackcommit'] = (((pe_stackcommit >> 8) & 0xFF) ^ ((pe_stackcommit >> 16) & 0xFF)) ^ ((pe_stackcommit >> 24) & 0xFF)

	#::OPTIONAL_HEADEr.SizeofHeapCommit - XOR each byte where 0xFFF0
	hashes['heapcommit'] = (((pe_heapcommit >> 8) & 0xFF) ^ ((pe_heapcommit >> 16) & 0xFF)) ^ ((pe_heapcommit >> 24) & 0xFF)

	pehash_container=bitstring.BitArray(uint=hashes['characteristics'],length=8)
	pehash_container.append(bitstring.BitArray(uint=hashes['subsystem'],length=8))
	pehash_container.append(bitstring.BitArray(uint=hashes['stackcommit'],length=8))
	pehash_container.append(bitstring.BitArray(uint=hashes['heapcommit'],length=8))

	for section in pe_file.sections:

		def bit_append(subhash):
			section_container=[]

			section_container=bitstring.BitArray(uint=subhash['virtualaddress'],length=23) #::Adjust section if addy typo'd
			section_container.append(bitstring.BitArray(uint=subhash['rawsize'],length=24))
			section_container.append(bitstring.BitArray(uint=subhash['characteristics'],length=8))
			section_container.append(bitstring.BitArray(uint=subhash['kolmogorov'],length=8))

			return section_container

		subhashes={ 'name' : '',
					'virtualaddress': int(),
					'rawsize' : int(),
					'characteristics' : int(),
					'kolmogorov' : int()
					}

		sub_virtualaddress = (section.VirtualAddress >> 9) & 0xFFFFFFF #::DWORD - Did the author typo? Should we be working with a 24 bit value vs 23?
		sub_rawsize = (section.SizeOfRawData >> 8) & 0xFFFFFF #::DWORD
		sub_characteristics = section.Characteristics #::DWORD
		section_raw=pe_file.get_data(section.VirtualAddress,section.SizeOfRawData)
		section_bzip_len=len(bz2.compress(section_raw))
		section_rawsize=int(section.SizeOfRawData)


		subhashes['name'] = section.Name.rstrip('\0')
		subhashes['virtualaddress'] = sub_virtualaddress
		subhashes['rawsize'] = sub_rawsize
		subhashes['characteristics'] = ((sub_characteristics >> 16) & 0xFF) ^ ((sub_characteristics >> 24) & 0xFF)

		subhashes['kolmogorov'] = 0

		if section_rawsize != 0:
			subhashes['kolmogorov'] = int( (7 * (section_bzip_len)) / section_rawsize )

		pehash_container.append(bit_append(subhashes))
		
	return (str(hashlib.sha1(pehash_container.tobytes()).hexdigest()))

print get_pehash(pefile.PE(os.path.expanduser(sys.argv[1])))
