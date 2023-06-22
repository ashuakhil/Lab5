'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    #  Test out the get_pokemon_info() function
    pokemon_name = "Rockruff"
    pokedox_number= "0744"
    #  Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info(pokemon_name)
    if poke_info is not None:
      print(pokemon_name)
      print(pokedox_number)
      print(poke_info)   
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    pokemon_name = str(pokemon_name).lower()

    # TODO: Build a clean URL and use it to send a GET request
    print(f"Poke Api URL: {POKE_API_URL}{pokemon_name}")
    clean_URL =requests.get(POKE_API_URL + pokemon_name)
    
    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if clean_URL.ok:
        pokemon_info = clean_URL.json()
        return pokemon_info
    # TODO: If the GET request failed, print the error reason and return None
    else:
        print('failure')
        print(f"Failed to fetch Pokemon information: {pokemon_name}")

        return None
    
   

if __name__ == '__main__':
    main()