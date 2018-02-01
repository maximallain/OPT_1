def segments_relations(dict_intersection, P) :
    print("Segments' relations...")
    relations_all={}
    i = 1
    for value in dict_intersection.values():
        list_keys = list(value.keys())
        list_values = list(value.values())
        varh = list_keys[0]
        posh = list_values[0]
        varv = list_keys[1]
        posv = list_values[1]
        dom_varh = P.var[varh]
        dom_varv = P.var[varv]
        relations = {(wordh,wordv) for wordv in dom_varv for wordh in dom_varh if wordh[posh]==wordv[posv]}
        relations_all[i]=(varh, varv, relations)
        i+=1
        P.addConstraint(varh, varv, relations)
