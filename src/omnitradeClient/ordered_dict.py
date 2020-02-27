def ordered_dict(dict_params):
    return [(key, dict_params[key]) for key in sorted(dict_params.keys())]
