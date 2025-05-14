from algorithme_de_recherche_dichotomique import BFS, DFS, GBFS, A_etoile
import time, matplotlib.pyplot as plt, tracemalloc

# Function to measure execution time and memory usage of an algorithm
def mesure(algo, *args, **kwargs):
    start = time.time()               # Start timing
    tracemalloc.start()              # Start tracking memory
    algo(*args, **kwargs)            # Run the algorithm
    end = time.time()                # End timing
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()              # Stop tracking memory
    memoire_utilisee = peak / 1024  # Convert memory to KB
    return end - start, memoire_utilisee

# Lists to store time and memory usage results
Temp = []
Memoire = []

# Algorithm names for labeling the plot
Algo = ['BFS', 'DFS', 'GBFS', 'A*']

# Graph structure (HERBRE) representing connections between nodes
HERBRE = {
    'A': ['H'], 'B': ['C'], 'C': ['B', 'J'], 'D': ['E'], 'E': ['D', 'F'],
    'F': ['E', 'G', 'M'], 'G': ['F', 'N'], 'H': ['A', 'I'], 'I': ['H', 'J', 'P'],
    'J': ['C', 'I', 'K', 'Q'], 'K': ['J', 'L', 'R'], 'L': ['K', 'M'], 'M': ['L', 'F'],
    'N': ['G', 'U'], 'O': ['P', 'V'], 'P': ['I', 'O', 'W'], 'Q': ['J', 'R', 'X'],
    'R': ['K', 'Q', 'S'], 'S': ['R', 'T'], 'T': ['S', 'U', 'AA'], 'U': ['N', 'T', 'AB'],
    'V': ['O', 'W', 'AC'], 'W': ['P', 'V', 'AD'], 'X': ['Q', 'Y', 'AE'],
    'Y': ['X', 'Z', 'AF'], 'Z': ['Y', 'AG'], 'AA': ['T', 'AH'], 'AB': ['U', 'AI'],
    'AC': ['V', 'AD', 'AJ'], 'AD': ['W', 'AC', 'AK'], 'AE': ['X', 'AF', 'AL'],
    'AF': ['Y', 'AE', 'AG', 'AM'], 'AG': ['Z', 'AF', 'AN'], 'AH': ['AA', 'AI', 'AO'],
    'AI': ['AB', 'AP'], 'AJ': ['AC', 'AK', 'AQ'], 'AK': ['AD', 'AJ', 'AL', 'AR'],
    'AL': ['AE', 'AK', 'AM', 'AS'], 'AM': ['AF', 'AL', 'AN', 'AT'],
    'AN': ['AG', 'AM', 'AU'], 'AO': ['AH'], 'AP': ['AI', 'AW'], 'AQ': ['AJ', 'AR'],
    'AR': ['AK', 'AQ', 'AS'], 'AS': ['AL', 'AR', 'AT'], 'AT': ['AM', 'AS', 'AU'],
    'AU': ['AN', 'AT', 'AV'], 'AV': ['AU', 'AW'], 'AW': ['AP', 'AV']
}

# Heuristic distance dictionary for GBFS and A*
Distante = {
    'A': 12, 'B': 11, 'C': 10, 'D': 9, 'E': 8, 'F': 7, 'G': 6,
    'H': 11, 'I': 10, 'J': 9, 'K': 8, 'L': 7, 'M': 6, 'N': 5,
    'O': 10, 'P': 9, 'Q': 8, 'R': 7, 'S': 6, 'T': 5, 'U': 4,
    'V': 9, 'W': 8, 'X': 7, 'Y': 6, 'Z': 5, 'AA': 4, 'AB': 3,
    'AC': 8, 'AD': 7, 'AE': 6, 'AF': 5, 'AG': 4, 'AH': 3, 'AI': 2,
    'AJ': 7, 'AK': 6, 'AL': 5, 'AM': 4, 'AN': 3, 'AO': 2, 'AP': 1,
    'AQ': 6, 'AR': 5, 'AS': 4, 'AT': 3, 'AU': 2, 'AV': 1, 'AW': 0
}

# Measure each algorithm and record results
T, m = mesure(BFS, 'A', 'AW', HERBRE)
Temp.append(T)
Memoire.append(m)

T, m = mesure(DFS, 'A', 'AW', HERBRE)
Temp.append(T)
Memoire.append(m)

T, m = mesure(GBFS, 'A', 'AW', HERBRE, Distante)
Temp.append(T)
Memoire.append(m)

T, m = mesure(A_etoile, 'A', 'AW', HERBRE, Distante)
Temp.append(T)
Memoire.append(m)

# Display measured times and memory usage
print("Execution time (BFS, DFS, GBFS, A*):", Temp)
print("Memory usage (BFS, DFS, GBFS, A*):", Memoire)

# Plotting the results using Matplotlib
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot execution time
axs[0].bar(Algo, Temp, color='lightblue')
axs[0].set_title("Execution Time")
axs[0].set_xlabel("Algorithm")
axs[0].set_ylabel("Time (seconds)")

# Plot memory usage
axs[1].bar(Algo, Memoire, color='lightgreen')
axs[1].set_title("Memory Usage")
axs[1].set_xlabel("Algorithm")
axs[1].set_ylabel("Memory (KB)")

plt.tight_layout()
plt.show()
