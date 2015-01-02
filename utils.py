__author__ = '@JarenGlover'

#!/usr/bin/env python

import json



def json_to_list(json_string,strip_assets='',key=None):
    '''

    :param json_string: a single json string
    :param strip_assets: chars you would like to be strip from json_string
    :param key: the key the the values you would like to be parsed and mapped
    :return: a list of floats from the json_string
    '''

    #load string as json
    json_dic = json.loads(json_string)

    #check for valid key
    if key in json_dic:
        values = str(json_dic[key])
        dic_strip = values.strip(strip_assets)
        #build a list of floats
        mapped_floats = [float(s) for s in dic_strip.split(',')]
    else:
        raise KeyError("The 'key' provided doesn't exists - please see function's docstring")

    return mapped_floats


