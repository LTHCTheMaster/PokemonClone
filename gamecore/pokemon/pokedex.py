from gamecore.utils import datatypes as dt
from gamecore.pokemon import types_define as td

print("[INIT]: Load Pokedex")

with open('data/pokedex.json', 'r') as pfile:
    pkmn = eval(pfile.read())

pokedex = [dt.Pokemon(i, pkmn[i]["bst"], [td.pokeTypes[td.NAMES.index(j)] for j in pkmn[i]["types"]], 'assets/' + i.lower() + '.png') for i in pkmn]

def displayPkmn() -> str:
    return '\n'.join([str(i) for i in pokedex])

#print(displayPkmn())
print("[INIT]: Pokedex Loaded")
