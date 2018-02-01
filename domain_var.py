def domain_var(segments_h, segments_v, dict_words):
    """
    :param segments_h: horizontal segments
    :param segments_v: vertical segments
    :return: dictionary, key : segment's name, value : segment's domain
    """
    print("Domain var...")
    var = {}
    for element_horizontal in segments_h.keys() :
        taille = segments_h[element_horizontal].__len__()
        var[element_horizontal] = set(dict_words[str(taille)])

    for element_vertical in segments_v.keys() :
        taille = segments_v[element_vertical].__len__()
        var[element_vertical] = set(dict_words[str(taille)])
    return var
