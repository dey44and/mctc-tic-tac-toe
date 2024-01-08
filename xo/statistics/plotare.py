import matplotlib.pyplot as plt

# Datele din simulări
simulations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
elapsed_times = [
    [137.23, 271.24, 406.70, 540.50, 673.07, 807.22, 942.22, 1073.53, 1208.62, 1343.93],
    [33.30, 67.60, 101.32, 135.59, 170.97, 205.46, 239.91, 274.11, 309.02, 342.95],
    [29.16, 57.45, 85.41, 113.88, 141.55, 169.20, 196.59, 225.01, 253.07, 281.49],
    [27.74, 55.62, 83.86, 112.21, 140.93, 168.96, 197.54, 225.64, 253.85, 281.29],
    [43.32, 87.09, 130.69, 174.98, 218.38, 262.92, 307.43, 350.82, 394.52, 438.12],
    [30.42, 61.30, 91.90, 122.08, 152.13, 182.29, 213.15, 244.18, 275.55, 306.20]
]

# Graficul pentru timpul mediu per simulare
plt.figure(figsize=(10, 6))
for i, times in enumerate(elapsed_times, 1):
    plt.plot(times, label=f"Simulation {i}")

plt.xlabel('Number of simulations')
plt.ylabel('Elapsed time (seconds)')
plt.title('Elapsed time per simulation')
plt.legend()
plt.tight_layout()

# Afișare grafic
plt.show()