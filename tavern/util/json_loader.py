#  -*- coding: utf-8 -*-
import os
import json

def resolve_include(current_path, path):
    abspath = os.path.join(os.path.dirname(current_path), path)
    return load_json(abspath)

def load_all_json(path):
    yield load_json(path)

def byteify(input, encoding='utf-8'):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode(encoding)
    else:
        return input

def load_json(path):
    with open(path) as f:
        data = json.load(f, encoding='utf-8')
        data = byteify(data)

    if "includes" not in data:
        return data

    includes = data["includes"]
    if includes and type(includes) == list:
        data.update({
            "includes": [resolve_include(path, include) for include in includes]
        })

    return data