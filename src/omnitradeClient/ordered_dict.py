def ordered_dict(dict_params):
    params = map(lambda key,value: (key, value), dict_params.keys(), dict_params.values())
    params.sort(key=take_key)

    return params

def take_key(item):
    return item[0]
