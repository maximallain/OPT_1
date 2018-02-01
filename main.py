from dict_intersection import dict_intersection
from sequence_finder import sequence_finder
from constraint_programming import constraint_programming
from dict_vocabulary import dict_vocabulary
from domain_var import domain_var
from segments_relations import segments_relations

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
dict_words = dict_vocabulary(path=fileword)
print(dict_words)
var = domain_var(segments_h,segments_v,dict_words)

P = constraint_programming(var)
dict_intersection = dict_intersection(segments_h,segments_v)
segments_relations = segments_relations(dict_intersection,P)


print("Solving...")

#print(P.conflict)
P.maintain_arc_consistency()
result = P.solve()
print(result)