import os
import json
from pyindex import PySmallWorldIndex

CONNECTIVITY = 5


def load_index():
    index_cache = os.environ.get('INDEX_CACHE', 'out.json')
    with open(index_cache, 'r') as f:
        content = json.loads(f.read())

    index = PySmallWorldIndex(len(content[0]['feature_vector']), CONNECTIVITY)
    for item in content:
        index.add_item(item['filename'], item['feature_vector'])

    return index
