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

    plt.plot(sizes, height_diffs, label='Różnica wysokości (BST - AVL)', color='blue', linewidth=2)
    plt.xlabel('Liczba elementów w strukturze (n)')
    plt.ylabel('Różnica wysokości')
    plt.title('Porównanie wysokości drzew BST i AVL')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_time_difference(filename):
    sizes = []
    insert_times = []
    find_times = []
    delete_times = []

    with open(filename, 'r', newline='') as csvfile:    
        reader = csv.DictReader(csvfile)
        for row in reader:
            sizes.append(int(row['n']))
            insert_times.append(float(row['insert_time']))
            find_times.append(float(row['find_time']))
            delete_times.append(float(row['delete_time']))

    plt.plot(sizes, insert_times, label='Wstawianie', color='blue', linewidth=2)
    plt.plot(sizes, find_times, label='Wyszukiwanie', color='red', linewidth=2)
    plt.plot(sizes, delete_times, label='Usuwanie', color='green', linewidth=2)

    plt.xlabel('Liczba elementów w drzewie (n)')
    plt.ylabel('Czas operacji [s]')
    plt.title('Czas operacji w drzewie BST w zależności od rozmiaru')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()