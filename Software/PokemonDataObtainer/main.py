from time import sleep

from models.pokedex import Pokedex
from models.pokemonspecies import PokemonSpecies

if __name__ == '__main__':
    test = Pokedex(17)
    for i in test.pokemon_entries:
        pokemonspecies = PokemonSpecies(i.pokemon_species.id)
        print("--------------------------------------------")
        print("Name.: " + pokemonspecies.name)
        print("Genera.: " + pokemonspecies.genera)
        print("Flavor Text.: " + pokemonspecies.flavortext)
        print("Variety got.: " + pokemonspecies.varieties)
        print("--------------------------------------------")
        sleep(1)