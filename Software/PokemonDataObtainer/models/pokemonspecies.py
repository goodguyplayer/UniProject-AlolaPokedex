import pokebase as pb

class Pokemon:
    def __init__(self, id):
        self.pokemon_entries = pb.pokedex(id).pokemon_entries