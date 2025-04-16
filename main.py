from trees.bst import BinarySearchTree
from trees.tree_utils import tree_height
from data.gerenator import generate_unique_numbers
from trees.avl import build_avl_from_sorted_array
from measurements.benchmark import run_benchmark
from measurements.benchmark import save_result_csv
from plots.plots import plot_height_difference
from plots.plots import plot_time_difference
if __name__ == "__main__":

    filename = 'saved_measurements.csv'
    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14]:
        tree.insert(value)

    sorted_array = generate_unique_numbers(5, seed=123)
    sorted_array.sort()  
    avl_root = build_avl_from_sorted_array(sorted_array)

    print("Tablica wejściowa:", sorted_array)
    print("AVL inorder:", BinarySearchTree()._inorder_recursive(avl_root))
    print("Wysokość AVL:", tree_height(avl_root))
    
    for i, n in enumerate([100, 1000, 5000]):
        result = run_benchmark(n)
        save_result_csv(result, filename, append=(i != 0))
        print(result)

    plot_time_difference(filename)