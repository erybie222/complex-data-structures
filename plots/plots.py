import matplotlib.pyplot as plt
import csv

def plot_height_difference(filename):
    sizes = []
    height_diffs = []

    with open(filename, 'r', newline='') as csvfile:    
        reader = csv.DictReader(csvfile)
        for row in reader:
            sizes.append(int(row['n']))
            height_diffs.append(int(row['height_diff']))

    plt.plot(sizes, height_diffs, label='BST height - AVL height', color='blue', linewidth=2)
    plt.xlabel('Rozmiar drzewa (n)')
    plt.ylabel('Różnica wysokości')
    plt.title('Porównanie wysokości drzew BST i AVL')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()