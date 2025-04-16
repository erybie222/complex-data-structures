from trees.bst import BinarySearchTree
from trees.avl import build_avl_from_sorted_array
from data.gerenator import generate_unique_numbers
from trees.tree_utils import tree_height
import time
import csv
import os

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result

def run_benchmark(n):

    data = generate_unique_numbers(n ,seed=42)
    bst_tree = BinarySearchTree()

    insert_time , _ = measure_time(lambda: [bst_tree.insert(x) for x in data])
    bst_height = tree_height(bst_tree.root)  

    find_time, _ = measure_time(lambda: [bst_tree.find(x) for x in data])
    delete_time , _ = measure_time(lambda:[bst_tree.delete(x) for x in reversed(data)])


    inorder = sorted(data)
    avl_tree = build_avl_from_sorted_array(inorder)
    avl_height = tree_height(avl_tree)

    return {
        "n" : n,
        "insert_time" : insert_time, 
        "find_time": find_time,
        "delete_time" : delete_time,
        "bst_height": bst_height,
        "avl_height": avl_height,
        "height_diff": bst_height-avl_height
    }

def save_result_csv(data , filename, append=False):
       mode = 'a' if append else 'w'
       write_header = not append

       with open(filename, mode, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if write_header:
                 writer.writeheader()
            writer.writerow(data)
            
