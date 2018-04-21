#!/bin/python3

"""
This is a new attempt at building a Vampire the Masquerade Character generator. I'm starting to make things more modular and hopefully simpler.
"""

from vamp_functions import easy_stuff
from vamp_functions import get_clan
from vamp_functions import attrib_ranks
from vamp_functions import ability_ranks
from vamp_functions import set_physical
from vamp_functions import set_mental
from vamp_functions import set_social

# Get easy information about the character and assign variables.
basics = easy_stuff()
clan = get_clan()
attribs = attrib_ranks()
abilities = ability_ranks()
phys = set_physical(attribs["Physical"])
print("")
social = set_social(attribs["Social"], clan[0])
ment = set_mental(attribs["Mental"])

print("***************")
for x in basics:
    print(f"{x}: {basics[x]}")
print(f"Clan: {clan[0]}")
print(f"Clan Disciplines: {clan[1]}")
print("***************")
print("Attributes\n--Physical--")

for x in phys:
    print(f"{x}: {phys[x]}")
print("\n--Social--")
for x in social:
    print(f"{x}: {social[x]}")

print("\n--Mental--")
for x in ment:
    print(f"{x}: {ment[x]}")
