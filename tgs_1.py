#buatlah program untuk fungsi menghitung perkalian matrix pada matrix 4x4 untuk matrix berikut : di ketahui 
# Matriks C
C = np.array
    [44, 55, 54, 10],
    [33, 5, 32, 13],
    [21, 7, 21, 11],
    [33, 88, 32, 15]


# Matriks D
D = np.array
    [2, 1, 3, 1],
    [7, 1, 0, 7],
    [2, 0, 1, 2],
    [1, 3, 1, 2]


# Perkalian matriks C x D
result = np.dot(C, D)

# Menampilkan hasil
print("Hasil perkalian matriks C x D adalah:")
print(result)