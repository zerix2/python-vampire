#!/home/mcdade1/anaconda3/bin/python3

"""
Planning for Vampire Character Generator.
"""
# Easy Stuff
def easy_stuff():
    """Get the easy information for the character."""
    # Get Character Name
    char_name = input("Name: ")

    # Get Player Name
    pc_name = input("Player: ")

    # Get Chronicle
    chronicle = input("Chronicle: ")

    # Get Nature
    nature = input("Nature: ")

    # Get Demeanor
    demeanor = input("Demeanor: ")

    # Get concept
    concept = input("Concept: ")

    # Get Sire Name
    sire_name = input("Sire: ")
    
    return (char_name, pc_name, chronicle, nature, demeanor, concept, sire_name)
    
# Trickier Stuff

# Get Attribute Ranks

# Get Ability Ranks

#char_name, pc_name, chronicle, nature, demeanor, concept, sire_name = easy_stuff()
#print(f"Name: {char_name}")
#print(f"Player: {pc_name}")
test = easy_stuff()
print(test)
