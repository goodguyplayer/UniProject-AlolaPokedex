import urllib
from time import sleep

from models.pokedex import Pokedex
from models.pokemon import Pokemon
from models.pokemonspecies import PokemonSpecies
import io

if __name__ == '__main__':
    for j in range(17,21):
        test = Pokedex(j)
        for i in test.pokemon_entries:
            pokemonspecies = PokemonSpecies(i.pokemon_species.id)
            pokemon = Pokemon(pokemonspecies.varieties)
            print("--------------------------------------------")
            f = open(str(i.pokemon_species.id) + ".txt", 'w')
            print("Name.: " + pokemonspecies.name)
            print("Genera.: " + pokemonspecies.genera)
            print("Flavor Text.: " + pokemonspecies.flavortext)
            # print("Sprite link.: " + pokemon.sprite)
            urllib.request.urlretrieve(pokemon.sprite, str(i.pokemon_species.id) + ".png")

            f.write("Name: " + pokemonspecies.name + '\n')
            f.write("Genera: " + pokemonspecies.genera + '\n')
            f.write("Flavor: " + pokemonspecies.flavortext + '\n')

            for i in (pokemon.stats.items()):
                print("Stats " + i[0] + ".: " + str(i[1]))
                f.write(i[0] + ": " + str(i[1]) + '\n')
            f.close()
            print("--------------------------------------------")
            sleep(1)