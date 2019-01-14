# ripVT

Maltego Canari transforms for Virus Total private API. Provided AS-IS, no warranties, no guarantees. 

No jokes in this repo. It's as serious as you are.

# Pivots
Multiple unique entities enable forward & reverse searches. Unique graphically-distinguished icons.

**Search (Phrase Entity) ->**

* Generic Search
* Behavioral
* Engines
* ITW

**Generic**
* Hash -> Download to Repository

**Hash -> VT File Report ->**

* Behavioral (Copied Files, Deleted, Downloaded, Moved, Mutex, Network, Opened, Read, Replaced, Written)
* Imphash
* Cert / Certs
* Compile Time
* Detections
* Exports / Imports
* File Names
* In-The-Wild (ITW) Locations
* Parents (Dropped / Created By)
* PE Resources
* PE Sections
* SSDEEP
* Similar-To

**Domain -> VT Domain Report ->**

* Undetected/Detected Communicating Samples
* Undetected/Detected Domain-Embedding Samples
* Undetected/Detected Domain-Downloaded Samples
* PCAP
* Domain Resolutions
* Siblings
* Subdomains
* Detected URLs

**IP Address -> VT IP Report**

* Undetected/Detected Communicating Samples
* Undetected/Detected Domain-Embedding Samples
* Undetected/Detected Domain-Downloaded Samples
* PCAP
* Domain Resolutions
* Siblings
* Subdomains
* Detected URLs

**Detections ->**

* Search Detection Name (Engine Included)
* Search Detection Name (No Engine

**Cuckoo -> (Report ID **

* Report -> Network



# Installation

1. Requires Canari, specifically [this branch/version](https://github.com/allfro/canari/tree/c90ed9f0f0fb5075358d7a1a4c1080aac3d4e6bc)
2. Install [Malformity](https://github.com/digital4rensics/Malformity)
3.
```bash
sudo python setup.py install
canari create-profile ripVT
```
4. Import generated ripVT.mtz
5. Import entities stored at:
```bash
src/ripVT/resources/external/entities.mtz
```

6. Copy src/ripVT/resources/etc/ripVT.conf to ~/.canari/
7. Pivot


# Usage
![Visual Guide](https://github.com/matonis/ripVT/blob/master/pivot.png)
