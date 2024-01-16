import os
from typing import List
import math
class Extraction:
    def parse_input(file_path: str) -> List[List[dict]]:
        '''Returns a list of game strings where the index is the `game number - 1`'''
        input = open(file_path).read().splitlines()
        return [Extraction.parse_game_string(game) for game in input]

    def parse_game_string(game_string: str) -> List[dict]:
        '''Returns a list dictionaries with the color name as the key and the number retrieved as the value'''
        game_string = game_string.split(": ")[-1]
        return_value = list()
        for round in game_string.split("; "):
            key_value = (s.split(" ") for s in round.split(", "))
            return_value.append({k: int(v) for v, k in key_value})
        return return_value
    
def check_game(index: int, game: List[dict], max_cubes: dict) -> int:
    '''returns the game number if the game is possible, otherwise returns 0'''
    for round in game:
        for color, count in round.items():
            if count > max_cubes[color]:
                return 0
    return index + 1

def fewest_possible(game: List[dict]) -> dict:
    '''returns a dict containing the fewest number of each cube color needed'''
    result_dict = dict()
    for round in game:
        for color, count in round.items():
            if count > result_dict.get(color, 0):
                result_dict[color] = count
    return result_dict

def power_of_set(set: dict) -> int:
    '''returns the product of cube color values'''
    return math.prod(set.values())

def part_1(games):
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    possible_game_id_sum = 0
    for index, game in enumerate(games):
        possible_game_id_sum += check_game(index, game, max_cubes)
    print(f"\npart_1:\n{possible_game_id_sum}\n")

def part_2(games):
    product_sum = 0
    for game in games:
        product_sum += power_of_set(fewest_possible(game))
    print(f"\npart_2:\n{product_sum}\n")

if __name__ == "__main__":
    games = Extraction.parse_input("input")
    part_1(games)
    part_2(games)

    