import re


def dict_intersection(segments_h,segments_v):
    """
    créé une variable pour chaque séquence,
    puis balance tous les couples de séquences qui s'intersectent, avec leur coordonnées d'intersection
    :param segments_h: horizontal segments
    :param segments_v: vertical segments
    :return: dictionnary (key : intersection's id, value : dictionary (key : segment's id, value : intersection's postion in the segment)
    """
    print("Intersection...")
    res = {}
    res_temp = {}
    i=1
    for keyh, sh in segments_h.items():
        for keyv, sv in segments_v.items():
            # c'est dans cette boucle qu'il faut mettre le compteur
            intersection=[x for x in sh if x in sv]

            if len(intersection) == 1 :
                intersec_h, intersec_v = position(intersection[0])
                sh_position_h, sh_position_v = position(sh[0])
                sv_position_h, sv_position_v = position(sv[0])
                position_word_h = int(intersec_v) - int(sh_position_v)
                position_word_v = int(intersec_h) - int(sv_position_h)
                res_temp[keyh] = position_word_h
                res_temp[keyv] = position_word_v
                res["x"+str(i)]=res_temp
                i += 1
                res_temp={}
            elif len(intersection) == 0 :
                pass
            else :
                raise IndexError("Intersection's Problem")
    print(res)
    return res

def position(position_id) :
    temp = re.split('x|\.', position_id)
    temp.remove('')
    position_h = temp[0]
    position_v = temp[1]
    return position_h, position_v




