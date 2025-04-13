import random

def generate_unique_numbers(count: int, seed: int = None) -> list[int]:
    if seed is not None:
        random.seed(seed)
    return random.sample(range(count * 10), count)
