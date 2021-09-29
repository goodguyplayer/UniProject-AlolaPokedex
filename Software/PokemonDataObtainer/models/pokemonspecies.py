import pokebase as pb

class PokemonSpecies:
    def __init__(self, id:str):
        self.pokemonspecies = pb.pokemon_species(id)
        self.name = self.pokemonspecies.name
        self.flavortext = self.setFlavorText(self.pokemonspecies.flavor_text_entries)
        self.genera = self.setGenus(self.pokemonspecies.genera)
        self.varieties = self.setVariety(self.pokemonspecies.varieties)

    def setGenus(self, genera: list):
        for i in genera:
            if i.language.name == "en":
                return i.genus

    def setFlavorText(self, flavor:list):
        for i in flavor:
            if i.language.name == "en":
                return i.flavor_text

    def setVariety(self, variety:list):
        for i in variety:
            if "alola" in i.pokemon.name:
                return i.pokemon.url
        return variety[0].pokemon.url
