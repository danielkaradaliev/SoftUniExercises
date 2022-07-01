from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemons=None):
        self.name = name
        self.pokemons = pokemons
        if pokemons is None:
            self.pokemons = list()

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in {x.name for x in self.pokemons}:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        from os import linesep

        result = f"Pokemon Trainer {self.name}{linesep}Pokemon count {len(self.pokemons)}{linesep}" \
                 f"{linesep.join([f'- {x.pokemon_details()}' for x in self.pokemons])}"

        return result
