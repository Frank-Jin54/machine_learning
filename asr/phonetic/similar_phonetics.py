import jellyfish
import phonetics
from Levenshtein import distance
from fuzzywuzzy import fuzz

code1 = jellyfish.soundex("ate")
code2 = jellyfish.soundex("eight")

print(code1, code2)
print(fuzz.ratio(code1, code2))

code1 = phonetics.metaphone("ate")
code2 = phonetics.metaphone("eight")
print(code1, code2)
print(fuzz.ratio(code1, code2))


code1 = phonetics.metaphone("Rupert")
code2 = phonetics.metaphone("Robert")
print(code1, code2)
print(fuzz.ratio(code1, code2))