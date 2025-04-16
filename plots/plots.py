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

    plt.plot(sizes, insert_times, label='Dodawanie danych', color='blue', linewidth=2)
    plt.plot(sizes, find_times, label='Wyszukiwanie danych', color='red', linewidth=2)
    plt.plot(sizes, delete_times, label='Usuwanie danych', color='green', linewidth=2)

    plt.xlabel('Rozmiar drzewa (n)')
    plt.ylabel('Czas [s]')
    plt.title('Porównanie czasów dla drzewa BST')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()