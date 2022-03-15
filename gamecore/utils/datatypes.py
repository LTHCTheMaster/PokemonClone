from fractions import Fraction

print("[INIT]: Define Some DataTypes")

weakness = Fraction("2")
resistance = Fraction("1/2")
immune = Fraction("0")
normal = Fraction("1")

class PokeType:
    def __init__(self, name: str):
        self.name = name
        self.weakness_t = []
        self.resistance_t = []
        self.immune_t = []
    
    def add_weakness(self, other):
        self.weakness_t.append(other)
    def add_resistance(self, other):
        self.resistance_t.append(other)
    def add_immune(self, other):
        self.immune_t.append(other)
    
    def isWeakTo(self, other) -> bool:
        if isinstance(other, PokeType):
            temp = [i.name for i in self.weakness_t]
            return other.name in temp
        return False
    def isResistantTo(self, other) -> bool:
        if isinstance(other, PokeType):
            temp = [i.name for i in self.resistance_t]
            return other.name in temp
        return False
    def isImmuneTo(self, other) -> bool:
        if isinstance(other, PokeType):
            temp = [i.name for i in self.immune_t]
            return other.name in temp
        return False

    def __str__(self) -> str:
        return f"{self.name}:\n\tWEAKNESS: {','.join([i.name for i in self.weakness_t])}\n\tRESISTANCE: {','.join([i.name for i in self.resistance_t])}\n\tIMMUNE: {','.join([i.name for i in self.immune_t])}"

class Move:
    def __init__(self, name: str, typed: PokeType, basePower: int, accuracy: int):
        self.name = name
        self.typed = typed
        self.basePower = basePower
        self.accuracy = accuracy

class Pokemon:
    def __init__(self, name: str, bst: list[int], types: list[PokeType]):
        self.name = name
        self.bst = bst # 0: HP, 1: ATK, 2: SPATK, 3: DEF, 4: SPDEF, 5: SPEED
        self.type0 = types[0]
        if len(types) >= 2:
            self.type1 = types[1]
        else:
            self.type1 = "UNDEFINED"
    
    def getMultiplier(self, move: Move) -> Fraction:
        multiplier = normal
        if self.type0.isWeakTo(move.typed):
            multiplier *= weakness
        elif self.type0.isResistantTo(move.typed):
            multiplier *= resistance
        elif self.type0.isImmuneTo(move.typed):
            multiplier *= immune
        if not type(self.type1) is str:
            if self.type0.isWeakTo(move.typed):
                multiplier *= weakness
            elif self.type0.isResistantTo(move.typed):
                multiplier *= resistance
            elif self.type0.isImmuneTo(move.typed):
                multiplier *= immune
        return multiplier