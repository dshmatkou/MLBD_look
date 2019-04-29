import json
from pyindex import PySmallWorldIndex
from django.conf import settings


def load_index(cache_path=settings.INDEX_CACHE):
    with open(cache_path, 'r') as f:
        content = json.loads(f.read())

    index = PySmallWorldIndex(
        len(content[0]['feature_vector']),
        settings.GRAPH_CONNECTIVITY
    )
    for item in content:
        index.add_item(item['filename'], item['feature_vector'])

    return index
