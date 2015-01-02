__author__ = '@JarenGlover'

#!/usr/bin/env python

import json



def string_json_obj(json_string,strip_assets='',key=None):
    #load string as json
    json_dic = json.loads(json_string)

    #check for valid key
    if key in json_dic:
        values = str(json_dic[key])
        dic_strip = values.strip(strip_assets)
        #build a list of floats
        mapped_floats = [float(s) for s in dic_strip.split(',')]
    else:
        raise KeyError("Your 'key' provided doesn't exists - please see function's docstring")

    return mapped_floats


#test_string = '''{"hustle": {}, "name": "", "userid": 0.0, "numbers": [20.0, 30.0, 40.0,15.0, 65.0, 20.0],
#  "nameid": 0.0, "user": "", "time": 87594, "query": {}, "sum": 456.0, "subname": 0.0}'''

#print string_json_obj(test_string,'[]','numbers')