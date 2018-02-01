import time
from dict_intersection import dict_intersection
from sequence_finder import sequence_finder
from constraint_programming import constraint_programming
from dict_vocabulary import dict_vocabulary
from domain_var import domain_var
from segments_relations import segments_relations
import string

"""
1. On récupère les segments h et v
2. On récupère les mots de vocabulaire du fichier
3. On définit le domaine
4. Création du programme
"""

doc = str(2)
filecross = "Data/crossword"+doc+".txt"
fileword = "Data/words"+doc+".txt"

segments_h,segments_v = sequence_finder(path=filecross)
print(segments_h)
dict_words = dict_vocabulary(path=fileword)
var = domain_var(segments_h,segments_v,dict_words)

dict_intersection = dict_intersection(segments_h,segments_v)

alphabet = list(string.ascii_lowercase)
for key in dict_intersection.keys() :
    var[key] = set(alphabet)

P = constraint_programming(var)

for key, value in dict_intersection.items():
    case = key
    seg_h = list(value.keys())[0]
    seg_v = list(value.keys())[1]
    pos_h = list(value.values())[0]
    pos_v = list(value.values())[1]
    domain_constr_h = {(word_h, word_h[pos_h]) for word_h in P.var[seg_h]}
    domain_constr_v = {(word_v, word_v[pos_v]) for word_v in P.var[seg_v]}
    constr_h = (seg_h, case, domain_constr_h)
    constr_v = (seg_v, case, domain_constr_v)
    P.addConstraint(seg_h, case, domain_constr_h)
    P.addConstraint(seg_v, case, domain_constr_v)
time1 = time.time()
result = P.solve()
time2 = time.time()
print("Temps de résolution : {}".format(time2-time1))
print(result)

P.maintain_arc_consistency()
time1 = time.time()
result = P.solve()
time2 = time.time()
print("Temps de résolution : {}".format(time2-time1))
result = P.solve()
print(result)

case_final = {}
for segments_h, list_pos_letter_h in segments_h.items() :
    i = 0
    word_h = result[segments_h]
    for elt in list_pos_letter_h :
        case_final[elt] = word_h[i]
        i += 1
print(case_final)
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
            str_temp += "# "

    str_final += str_temp + "\n"

print(str_final)
