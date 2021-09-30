import pokebase as pb

class Pokemon:
    def __init__(self, id:str):
        self.pokemon = pb.pokemon(int(id))
        self.sprite = self.pokemon.sprites.front_default
        self.stats = self.setStats(self.pokemon.stats)

    def setStats(self, stats: list):
        return {
            "hp": stats[0].base_stat,
            "attack": stats[1].base_stat,
            "defense": stats[2].base_stat,
            "special-attack": stats[3].base_stat,
            "special-defense": stats[4].base_stat,
            "speed": stats[5].base_stat,
        }