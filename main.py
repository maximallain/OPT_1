import time
from dict_intersection import dict_intersection
from sequence_finder import sequence_finder
from constraint_programming import constraint_programming
from dict_vocabulary import dict_vocabulary
from domain_var import domain_var_segment, domain_var_letter
from print_res import print_res
from constraints import constraints
from joke import joke

print("///////// DM1 - OPTIMISATION /////////\n")

num = 0
while(num != 1 and num != 2):
    num = int(input("Number of crossword ? (1 or 2)\n"))

doc = str(num)
filecross = "Data/crossword"+doc+".txt"
fileword = "Data/words"+doc+".txt"

# Lecture of the crossword and a return horizontal and vertical segments' list
segments_h,segments_v = sequence_finder(path=filecross)

# Read and return the word's list of the file
dict_words = dict_vocabulary(path=fileword)

# Associate variables (segments) and their domains
var = domain_var_segment(segments_h,segments_v,dict_words)

# Determine the words' intersections
dict_intersection = dict_intersection(segments_h,segments_v)

# Associate variables (letters) and their domains
var = domain_var_letter(dict_intersection, var)

# Initialize the program
P = constraint_programming(var)

# Add the constraint to the program
constraints(dict_intersection, P)

# Solve

print("\n///// SOLVING //////\n")
time1 = time.time()
result = P.solve()
time2 = time.time()
print("Resolution's time without Arc Consistency : {}\n".format(time2-time1))

P.maintain_arc_consistency()
time1 = time.time()
result = P.solve()
time2 = time.time()
print("Resolution's time with Arc Consistency : {}\n".format(time2-time1))
result = P.solve()

print_res(segments_h, segments_v, result, filecross)

answer = input("Do you want a joke to end this demo ? (y/n)\n").lower()
if answer == "y" :
    joke()