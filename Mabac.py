import numpy as np

# Data awal
alternatives = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
criteria_weights = np.array([0.3, 0.2, 0.1, 0.4])
decision_matrix = np.array([
    [10, 70, 50, 30],
    [10, 70, 70, 50],
    [70, 30, 70, 70],
    [70, 50, 50, 50],
    [10, 70, 70, 30],
    [50, 70, 30, 50],
    [50, 70, 30, 30],
    [10, 50, 50, 10],
    [70, 70, 10, 30],
    [50, 70, 30, 30]
])

# Normalisasi matriks
def normalize_matrix(matrix):
    norm_matrix = np.zeros(matrix.shape)
    for j in range(matrix.shape[1]):
        column = matrix[:, j]
        norm_matrix[:, j] = (column - column.min()) / (column.max() - column.min())
    return norm_matrix

# Menghitung matriks tertimbang
def weighted_matrix(matrix, weights):
    return matrix * weights

# Menghitung matriks area perkiraan batas
def boundary_matrix(matrix, weights):
    return np.prod(matrix * weights, axis=1) ** (1 / len(weights))

# Menghitung matriks jarak alternatif dari daerah perkiraan perbatasan
def distance_matrix(matrix, boundary):
    return matrix - boundary[:, np.newaxis]

# Menghitung nilai preferensi alternatif
def preference_score(matrix, distance):
    return np.sum(distance, axis=1)

# Menghitung perankingan alternatif
def ranking(alternatives, scores):
    return np.argsort(scores)[::-1]

# Menghitung nilai preferensi alternatif
norm_matrix = normalize_matrix(decision_matrix)
weighted_matrix = weighted_matrix(norm_matrix, criteria_weights)
boundary = boundary_matrix(weighted_matrix, criteria_weights)
distance = distance_matrix(weighted_matrix, boundary)
scores = preference_score(distance, criteria_weights)
ranking = ranking(alternatives, scores)

# Menampilkan hasil
print("Nilai Preferensi untuk setiap alternatif:")
for alt, score in zip(alternatives, scores):
    print(f"{alt}: {score:.4f}")

print("\nRanking alternatif:")
for rank, alt in enumerate(ranking, start=1):
    print(f"{rank}. {alt}")

print(f"\nAlternatif terbaik adalah: {ranking[0]}")