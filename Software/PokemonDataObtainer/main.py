from time import sleep

from models.pokedex import Pokedex
from models.pokemon import Pokemon
from models.pokemonspecies import PokemonSpecies
import PIL.Image as Image
import io

if __name__ == '__main__':
    test = Pokedex(17)
    for i in test.pokemon_entries:
        pokemonspecies = PokemonSpecies(i.pokemon_species.id)
        pokemon = Pokemon(pokemonspecies.varieties)
        print("--------------------------------------------")
        print("Name.: " + pokemonspecies.name)
        print("Genera.: " + pokemonspecies.genera)
        print("Flavor Text.: " + pokemonspecies.flavortext)
        print("Sprite link.: " + pokemon.sprite)
        for i in (pokemon.stats.items()):
            print("Stats " + i[0] + ".: " + str(i[1]))

        print("--------------------------------------------")
        sleep(1)