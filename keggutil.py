__author__ = "Kozo Nishida"
__email__ = "knishida@riken.jp"
__version__ = "0.1.0"
__license__ = "MIT"

API_BASE = "http://rest.kegg.jp/"

import requests
import pandas as pd
from StringIO import StringIO
#from progressbar import ProgressBar

def search_pathway_object(cpd_ids):
    map_list = requests.get('http://rest.kegg.jp/list/pathway/map')
    map_ids = pd.read_table(StringIO(map_list.content.strip()), header=None)[0]
    found_in = {}
    all_found_ids = set([])
    for map_id in map_ids:
        map_cpds = requests.get('http://rest.kegg.jp/link/cpd/' + map_id)
        if len(map_cpds.content) > 3:
            map_cpd_ids = pd.read_table(StringIO(map_cpds.content.strip()), header=None)[1]

            print map_id
            found_ids = set(map_cpd_ids.values) & set(cpd_ids)
            if len(found_ids) > 0:
                found_in[map_id] = found_ids
                all_found_ids = all_found_ids | found_ids
    found_in["notFound"] = set(cpd_ids) - all_found_ids
    return found_in

def get_brite():
    brite = requests.get('http://rest.kegg.jp/list/brite')
    brite_tbl = pd.read_table(brite.content.strip(), header=None)
    return brite_tbl

def save_cpd_entries():
    cpds = requests.get('http://rest.kegg.jp/list/compound')
    lines = cpds.content.strip().split('\n')
#    pbar = ProgressBar(maxval=len(lines))
    for i in range(len(lines)):
        cpdid = lines[i].split('\t')[0]
        res = requests.get('http://rest.kegg.jp/get/' + cpdid)
        f = open(cpdid[4:], 'w')
        f.write(res.content)
        f.close()
#        pbar.update(i)
#    pbar.finish()
    print "all KEGG COMPOUND entries are saved"
