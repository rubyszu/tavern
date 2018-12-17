# -*- coding: utf-8 -*-
import box
from tavern.util.dict_util import resolve_value

def saveSetsOfList(check_list, save_key, **check_key):
    expected_list = []

    for i in check_list:
        if all(item in i.items() for item in check_key.items()):
            if isinstance(i[save_key], (list, box.BoxList)):
                expected_list.extend(i[save_key])
            else:
                expected_list.append(i[save_key])

    return expected_list


def saveResponseSetsOfList(response, key, check_list, save_key, **check_key):
    expected_list = []

    for i in resolve_value(check_list, response.json()):
        if all(item in i.items() for item in check_key.items()):
            if isinstance(i[save_key], (list, box.BoxList)):
                expected_list.extend(i[save_key])
            else:
                expected_list.append(i[save_key])

    return { key: expected_list }

def saveSetsOfElements(check_list, save_key, **check_key):
    expected_list = []
    for i in check_list:
        if all(item in i.items() for item in check_key.items()):
            save = {}
            for j in save_key:
                save.update({j: i[j]})
            expected_list.append(save)

    return expected_list