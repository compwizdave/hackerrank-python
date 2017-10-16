#!/usr/bin/env python

import yaml
import pprint

with open('/tmp/l','r') as f:
    doc = yaml.load(f)

pprint.pprint(doc)

#txt = doc["treeroot"]["branch1"]
#print txt
# print yaml.dump(f)

# print yaml.dump(mydata, canonical=True)
