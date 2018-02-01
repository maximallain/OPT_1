
def print_res(segments_h, segments_v, result, filecross):
    """

    :param segments_h:
    :param segments_v:
    :param result:
    :return:
    """
    case_final = {}
    for segments_h, list_pos_letter_h in segments_h.items() :
        i = 0
        word_h = result[segments_h]
        for elt in list_pos_letter_h :
            case_final[elt] = word_h[i]
            i += 1
    for segments_v, list_pos_letter_v in segments_v.items() :
        i = 0
        word_v = result[segments_v]
        for elt in list_pos_letter_v :
            case_final[elt] = word_v[i]
            i += 1


    with open(filecross, 'r') as fc :
        len_cross = len(fc.readlines())

    str_final = ""
    for i in range(0,len_cross) :
        str_temp = ""

        for j in range(0, len_cross) :
            var_temp = "x"+str(i)+"."+str(j)
            if var_temp in case_final :
                str_temp += case_final[var_temp]+" "
            else :
                str_temp += ". "

        str_final += str_temp + "\n"

    print("Final result :\n")
    print(str_final)

