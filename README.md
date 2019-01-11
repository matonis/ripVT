# ripVT

Maltego Canari transforms for Virus Total private API. Provided AS-IS, no warranties, no guarantees. 

No jokes in this repo... because this transform set doesn't fuck around.

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


# Usage
![Visual Guide](https://github.com/matonis/ripVT/blob/master/pivot.png)