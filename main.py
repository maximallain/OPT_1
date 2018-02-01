import time
from dict_intersection import dict_intersection
from sequence_finder import sequence_finder
from constraint_programming import constraint_programming
from dict_vocabulary import dict_vocabulary
from domain_var import domain_var
from print_res import print_res
from constraints import constraints
import string

"""
1. On récupère les segments h et v
2. On récupère les mots de vocabulaire du fichier
3. On définit le domainew
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
constraints(dict_intersection, P)

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


print_res = print_res(segments_h, segments_v, result, filecross)

print(print_res)
