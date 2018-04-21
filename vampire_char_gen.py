#!/home/mcdade1/anaconda3/bin/python3

"""
This is my Vampire the Masquerade Character Generator. This will take in relevant information for the character,
then generate a pdf file containing the information.
"""

# Define a list of clans with disciplines and weaknesses. This will only include Camarilla and independant clans.
clan_list = ['Gangrel', 'Toreador', 'Brujah', 'Nosferatu', 'Ventrue', 'Malkavian', 'Assamite', 'Tremere', 'Ravnos', 'Giovanni', 'Setite']

clan_discs = {'Gangrel':['Protean', 'Fortitude', 'Animalism'], 'Toreador':['Auspex', 'Celerity', 'Presence'], 'Brujah':['Celerity', 'Potence', 'Presence'], 'Nosferatu':['Obfuscate', 'Animalism', 'Potence'], 'Ventrue':['Dominate', 'Fortitude', 'Presence'], 'Malkavian':['Auspex', 'Dementation', 'Obfuscate'], 'Assamite':['Celerity', 'Obfuscate', 'Quietus'], 'Tremere':['Thaumaturgy', 'Auspex', 'Dominate'], 'Ravnos':['Animalism', 'Fortitude', 'Chimerstry'], 'Giovanni':['Dominate', 'Potence', 'Necromancy'], 'Setite':['Obfuscate', 'Presence', 'Serpentis']}

# Define list of natures and demeanors

# Get Character Name
char_name = input("Name: ")

# Get Player Name
pc_name = input("Player: ")

# Get Chronicle
chronicle = input("Chronicle: ")
# Define concept
concept = input("Concept: ")

# Get Sire Name
sire_name = input("Sire: ")

# Prompt the user to pick a clan from a list of possible clans.
try:
    chosen_clan = input("Enter the number next to your chosen clan: \n1. Gangrel\n2. Toreador\n3. Brujah\n4. Nosferatu\n5. Ventrue\n6. Malkavian\n7. Assamite\n8. Tremere\n9. Ravnos\n10. Giovanni\n11. Setite\nChoice? : ")
    int(chosen_clan)
    
except ValueError:
    print("You didn't enter a valid number.")
    exit()

final_clan = clan_list[(int(chosen_clan) - 1)]
# Derive generation. This will be 13 - any rating in the generation background.

# Set Attribute Ranks 7/5/3
attributes = ['physical', 'social', 'mental']
attr_final = []
while len(attr_final) < 3:
    print(f"\nAttributes are currently ranked: {attr_final}  ")
    pick = input(f"\nRank the attributes: {attributes}  ")
    if pick in attributes:
        if pick not in attr_final:
            attr_final.append(pick)
        else:
            print("Please try again.")
    else:
        print("Not a valid entry. Please try again.")

# Set Ability Ranks 13/9/5
abilities = ['talents', 'knowledges', 'skills']
ability_final = []
while len(ability_final) < 3:
    print(f"\nAbilities are currently ranked: {ability_final}  ")
    pick2 = input(f"\nRank your abilities: {abilities}  ")
    if pick2 in abilities:
        if pick2 not in ability_final:
            ability_final.append(pick2)
        else:
            print("Please try again.")
    else:
        print("Not a valid entry. Please try again.")


print('\n\n')
print(f"Name: {char_name}\tPlayer: {pc_name}\tChronicle: {chronicle}")
print(f"Clan: {final_clan}")
print(f"Your Attributes are ranked {attr_final[0]}, {attr_final[1]}, {attr_final[2]}.")
print(f"Your abilities are ranked {ability_final[0]}, {ability_final[1]}, {ability_final[2]}.")
print(f"Clan Disciplines: {clan_discs[final_clan][0]}, {clan_discs[final_clan][1]}, {clan_discs[final_clan][2]}.")