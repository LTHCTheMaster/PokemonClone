from gamecore.utils import datatypes as dt

# Normal: 0
# Fighting: 1
# Flying: 2
# Poison: 3
# Ground: 4
# Rock: 5
# Bug: 6
# Ghost: 7
# Steel: 8
# Fire: 9
# Water: 10
# Grass: 11
# Electric: 12
# Psychic: 13
# Ice: 14
# Dragon: 15
# Dark: 16
# Fairy: 17
print("[INIT]: Predefine pokemon types")

with open('data/types.json', 'r') as tfile:
    types = eval(tfile.read())

NAMES = [i for i in types]
pokeTypes = [dt.PokeType(i) for i in NAMES]

def addWeaknesses(selftype: int, othertypes: list[int]):
    for i in range(len(othertypes)):
        pokeTypes[selftype].add_weakness(pokeTypes[othertypes[i]])
def addResistances(selftype: int, othertypes: list[int]):
    for i in range(len(othertypes)):
        pokeTypes[selftype].add_resistance(pokeTypes[othertypes[i]])
def addImmunities(selftype: int, othertypes: list[int]):
    for i in range(len(othertypes)):
        pokeTypes[selftype].add_immune(pokeTypes[othertypes[i]])

print("[INIT]: Create pokemon types relations")

def addAllWeaknesses():
    for i in types:
        if len(types[i]["weakness"]) > 0:
            addWeaknesses(NAMES.index(i),[NAMES.index(j) for j in types[i]["weakness"]])
def addAllResistances():
    for i in types:
        if len(types[i]["resistance"]) > 0:
            addResistances(NAMES.index(i),[NAMES.index(j) for j in types[i]["resistance"]])
def addAllImmunities():
    for i in types:
        if len(types[i]["immune"]) > 0:
            addImmunities(NAMES.index(i),[NAMES.index(j) for j in types[i]["immune"]])

addAllWeaknesses()
addAllResistances()
addAllImmunities()

def displayTypes() -> str:
    return '\n'.join([str(i) for i in pokeTypes])

print(displayTypes())
print("[INIT]: Pokemon Types Initialization Ended")
