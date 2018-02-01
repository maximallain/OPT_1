def constraints(dict_intersection, P) :
    """
    :param dict_intersection: take
    :param P:
    """
    print("Segment and letter's relations...")
    for key, value in dict_intersection.items():
        case = key
        seg_h = list(value.keys())[0]
        seg_v = list(value.keys())[1]
        pos_h = list(value.values())[0]
        pos_v = list(value.values())[1]
        domain_constr_h = {(word_h, word_h[pos_h]) for word_h in P.var[seg_h]}
        domain_constr_v = {(word_v, word_v[pos_v]) for word_v in P.var[seg_v]}
        P.addConstraint(seg_h, case, domain_constr_h)
        P.addConstraint(seg_v, case, domain_constr_v)