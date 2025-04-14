from trees.bst import BinarySearchTree
from data.gerenator import generate_unique_numbers
from trees.tree_utils import tree_height
import time

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time