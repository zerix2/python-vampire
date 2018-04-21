"""
Functions for Vampire Character Generator.
"""
# Easy Stuff
def easy_stuff():
    """Get the most basic information about the player and the pc."""
    basics = {"Name":"", "Player":"", "Chronicle":"", "Nature":"", "Demeanor":"", "Concept":"", "Sire":""}
    for x in basics:
        basics[x] = input(f"{x}: ")
    return basics

def get_clan():
    """Get the user to select a clan from a list of allowed ones."""
    clan_list = ['Gangrel', 'Toreador', 'Brujah', 'Nosferatu', 'Ventrue', 'Malkavian', 'Assamite', 'Tremere', 'Ravnos', 'Giovanni', 'Setite']
    clan_discs = {'Gangrel':['Protean', 'Fortitude', 'Animalism'], 'Toreador':['Auspex', 'Celerity', 'Presence'], 'Brujah':['Celerity', 'Potence', 'Presence'], 'Nosferatu':['Obfuscate', 'Animalism', 'Potence'], 'Ventrue':['Dominate', 'Fortitude', 'Presence'], 'Malkavian':['Auspex', 'Dementation', 'Obfuscate'], 'Assamite':['Celerity', 'Obfuscate', 'Quietus'], 'Tremere':['Thaumaturgy', 'Auspex', 'Dominate'], 'Ravnos':['Animalism', 'Fortitude', 'Chimerstry'], 'Giovanni':['Dominate', 'Potence', 'Necromancy'], 'Setite':['Obfuscate', 'Presence', 'Serpentis']}
    pick = 0
    while True:
        print("Time to select a clan. Below is a list of allowed clans:")
        for x in range(len(clan_list)):
            print(f"{x + 1}. {clan_list[x]}")
        try:
            pick = int(input("Enter the number of your selection:  "))
        except ValueError:
            print("You didn't enter a number. Try again.")
            continue
        
        if (pick < 0) or (pick > 11):
            print("You didn't enter a valid number. Try again.")
            continue
        else:
            return clan_list[pick - 1],clan_discs[clan_list[pick - 1]]

# Trickier stuff.
def attrib_ranks():
    """Assign ranks to the attribute groups."""
    values = [1, 2, 3]
    attribs = {"Physical":"", "Social":"", "Mental":""}
    print("We need to assign ranks to the Physical, Social, and Mental attribute groups.\n")

    # Set the physical attribute rank.
    while True:
        try:
            physical = int(input("What will be the rank of the Physical attribute group? Enter the number of your selection.\n\t1. Primary\n\t2. Secondary\n\t3. Tertiary\n?:  "))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try again.")
            continue

        if (physical != 1) and (physical != 2) and (physical != 3):
            print("\nYou did not enter 1, 2, or 3. Try again.\n")
        else:
            attribs["Physical"] = physical
            break

    # Set the social attribute rank.
    thing = True
    while thing == True:
        print(f"\nThe current ranks are:")
        for x in attribs:
            print(f"{x}: {attribs[x]}")
        try:
            social = int(input("\nWhat will be the rank of the Social attribute group?\n"))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try again.")
            continue

        if (social != 1) and (social != 2) and (social != 3):
            print("You did not enter 1, 2, or 3. Try again\n.")
            continue
        elif social == physical:
            print("\nThat rank has already been selected. Try again.")
            continue
        else:
            attribs["Social"] = social
            thing = False

    # Set the mental attribute rank.
    picked = []
    for x in attribs:
        picked.append(attribs[x])

    while True:
        if values[0] in picked:
            values.pop(0)
        else:
            break

    attribs["Mental"] = values[0]
    print(f"\nMental will be set to {values[0]}.\n")

    return attribs

def ability_ranks():
    """Assign ranks to the ability groups."""
    values = [1, 2, 3]
    abilities = {"Talents":"", "Skills":"", "Knowledges":""}
    print("We need to assign ranks to the Talents, Skills, and Knowledges ability groups.\n")

    # Set the talents ability rank.
    while True:
        try:
            talents = int(input("What will be the rank of the Talents ability group? Enter the number of your selection.\n\t1. Primary\n\t2. Secondary\n\t3. Tertiary\n?:  "))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try again.")
            continue

        if (talents != 1) and (talents != 2) and (talents != 3):
            print("\nYou did not enter 1, 2, or 3. Try again.\n")
        else:
            abilities["Talents"] = talents
            break

    # Set the skills attribute rank.
    thing = True
    while thing == True:
        print(f"\nThe current ranks are:")
        for x in abilities:
            print(f"{x}: {abilities[x]}")
        try:
            skills = int(input("\nWhat will be the rank of the Social attribute group?\n"))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try again.")
            continue

        if (skills != 1) and (skills != 2) and (skills != 3):
            print("You did not enter 1, 2, or 3. Try again\n.")
            continue
        elif skills == talents:
            print("\nThat rank has already been selected. Try again.")
            continue
        else:
            abilities["Social"] = skills
            thing = False

    # Set the knowledges ability rank.
    picked = []
    for x in abilities:
        picked.append(abilities[x])

    while True:
        if values[0] in picked:
            values.pop(0)
        else:
            break

    abilities["Knowledges"] = values[0]
    print(f"\nKnowledges will be set to {values[0]}.\n")

    return abilities

# Put Dots into Physical Attributes.
def set_physical(rank):
    """Take the rank given to physical attributes and use that assign dots"""
    physical = {"Strength":1, "Dexterity":1, "Stamina":1}
    if int(rank) == 1:
        dots = 7
    elif int(rank) == 2:
        dots = 5
    else:
        dots = 3

    while dots > 0:
        pick = 0
        print(f"\nYou have {dots} dots to spend on Physical attributes.\nYour current Physical attributes are:")
        y = 1
        for x in physical:
            print(f"{y}. {x}: {physical[x]} ")
            y += 1
        try:
            pick = int(input("Where would you like to spend a dot? Enter 1, 2, or 3 to place a dot:  "))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try again.")

        if pick < 0 or pick > 3:
            print("You didn't enter 1, 2, or 3. Try again. ")
        elif pick == 1 and physical["Strength"] < 5:
            physical["Strength"] += 1
            dots -= 1
        elif pick == 2 and physical["Dexterity"] < 5:
            physical["Dexterity"] += 1
            dots -= 1
        elif pick == 3 and physical["Stamina"] < 5:
            physical["Stamina"] += 1
            dots -= 1

    return physical

# Put dots into Mental Attributes.
def set_mental(rank):
    """Take the rank given to mental attributes and use that to assign dots."""
    mental = {"Perception":1, "Intelligence":1, "Wits":1}
    if int(rank) == 1:
        dots = 7
    elif int(rank) == 2:
        dots = 5
    else:
        dots = 3

    while dots > 0:
        pick = 0
        print(f"\nYou have {dots} dots to spend on Mental attributes.\nYour current Mental attributes are:")
        y = 1
        for x in mental:
            print(f"{y}. {x}: {mental[x]}")
            y += 1
        try:
            pick = int(input("Where would you like to spend a dot? Enter 1, 2, or 3 to place a dot: "))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try again.")

        if pick < 0 or pick > 3:
            print("You didn't enter 1, 2, or 3. Try again. ")
        elif pick == 1 and mental["Perception"] < 5:
            mental["Perception"] += 1
            dots -= 1
        elif pick == 2 and mental["Intelligence"] < 5:
            mental["Intelligence"] += 1
            dots -= 1
        elif pick == 3 and mental["Wits"] < 5:
            mental["Wits"] += 1
            dots -= 1

    return mental

# Assign dots to the Social Traits.
def set_social(rank, clan):
    """Take in the rank of the social attribute group and the clan and use that to spend dots."""
    social = {"Charisma":1, "Manipulation":1, "Appearance":1}
    if int(rank) == 1:
        dots = 7
    elif int(rank) == 2:
        dots = 5
    else:
        dots = 3
        
    if clan == "Nosferatu":
        social["Appearance"] = 0
    
        
    while dots > 0:
        pick = 0
        y = 1
        print(f"\nYou have {dots} dots to spend on Social attributes.\nYour current Social attributes are: ")
        for x in social:
            print(f"{y}. {x}: {social[x]}")
            y += 1
        try:
            pick = int(input("Where would you like to spend a dot? Enter 1, 2, or 3 to place a dot: "))
        except ValueError:
            print("You didn't enter 1, 2, or 3. Try againa.")
            
        if pick < 0 or pick > 3:
            print("You didn't enter 1, 2, or 3. Try again. ")
        elif pick ==1 and social["Charisma"] < 5:
            social["Charisma"] += 1
            dots -= 1
        elif pick == 2 and social["Manipulation"] < 5:
            social["Manipulation"] += 1
            dots -= 1
        elif pick == 3 and social["Appearance"] < 5 and clan != "Nosferatu":
            social["Appearance"] += 1
            dots -= 1
        elif pick == 3 and clan == "Nosferatu":
            print("You picked Nosferatu as your clan. You can't put dots in Appearance. Try again.")
            
    return social

# Assign dots to Talent abilities.
def set_talent(rank):
    """Take in the rank of the Talents ability to get and assign the correct number of dots."""
    talents = {"Alertness":0, "Athletics":0, "Awareness":0, "Brawl":0, "Empathy":0, "Expression":0, "Intimidation":0, "Leadership":0, "Streetwise":0, "Subterfuge":0}
    spending = {1:"Alertness", 2:"Athletics", 3:"Awareness", 4:"Brawl", 5:"Empathy", 6:"Expression", 7:"Intimidation", 8:"Leadership", 9:"Streetwise", 10:"Subterfuge"}

    if int(rank) == 1:
        dots = 13
    elif int(rank) == 2:
        dots = 9
    else:
        dots = 5

    print("\033c")
    while dots > 0:
        pick = 0
        y = 1
        print(f"You have {dots} dots to spend on Talents.\nYour current Talents are: ")
        for x in talents:
            print(f"{y}. {x}: {talents[x]}")
            y += 1
        try:
            pick = int(input("Where would you like to add a dot? Enter the number of your choice:  "))
        except ValueError:
            print("\033c\nYou didn't enter a number between 1 and 10. Try again.")
            continue
        
        if pick < 0 or pick > 10:
            print("\033c\nYou didn't enter a number between 1 and 10. Try again. ")
            continue
        
        if talents[spending[pick]] >= 3:
            print("\033c\nYou can't increase a talent above 3 right now. Try again. ")
        else:
            talents[spending[pick]] += 1
            dots -= 1
            print("\033c")
    return talents

# Assign dots to Skills abilities.
def set_skills(rank):
    """Take in the rank of the Skills ability to get and assign the correct number of dots."""
    skills = {"Animal Ken":0, "Crafts":0, "Drive":0, "Etiquette":0, "Firearms":0, "Larceny":0, "Melee":0, "Performance":0, "Stealth":0, "Survival":0}
    spending = {1:"Animal Ken", 2:"Crafts", 3:"Drive", 4:"Etiquette", 5:"Firearms", 6:"Larceny", 7:"Melee", 8:"Performance", 9:"Stealth", 10:"Survival"}

    if int(rank) == 1:
        dots = 13
    elif int(rank) == 2:
        dots = 9
    else:
        dots = 5
    
    print("\033c")
    while dots > 0:
        pick = 0
        y = 1
        print(f"You have {dots} dots to spend on Skills.\nYour current Skills are: ")
        for x in skills:
            print(f"{y}. {x}: {skills[x]}")
            y += 1
        try: 
            pick = int(input("Where would you like to add a dot? Enter the number of your choice:  "))
        except ValueError:
            print("\033c\nYou didn't enter a number between 1 and 10. Try again.")
        
        if pick < 0 or pick > 10:
            print(f"\033c\nYou didn't enter a number between 1 and 10. Try again. ")
            continue
        
        if skills[spending[pick]] >= 3:
            print("\033c\nYou can't increase a skill abover 3 right now. Try again. ")
        else:
            skills[spending[pick]] += 1
            dots -= 1
            print("\033c")
        return skills
