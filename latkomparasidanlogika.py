# Latihan komparasi & logika

# membuat gabungan area rentang dari angka

# ++++++3-------10++++++
#print("===KURANG DARI 3 ATAU LEBIH DARI 10===")
#inputUser = float(input("masukkan angka yg bernilai\nkurang dari 3\natau\nlebih dari 10\n:"))

# ++++++3---------------------
# Memeriksa angka kurang dari 3
#isKurangDari = (inputUser < 3)
#print("Kurang dari 3 =", isKurangDari)

# -------------------10++++++
# Memeriksa angka lebih dari 10
#isLebihDari = (inputUser > 10)
#print("Lebih dari 10 =", isLebihDari)

# ++++++3-------10++++++
#isCorrect = isKurangDari or isLebihDari
#print("angka yg anda masukan: ", isCorrect)

# ------3+++++++++10------
#print("===LEBIH DARI 3 DAN KURANG DARI 10====")
#inputUser = float(input("masukkan angka yg bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

# ------3+++++++++
#isLebihDari = (inputUser > 3)
#print("Lebih dari 3 =", isLebihDari)

# +++++++10------
#isKurangDari = (inputUser < 10)
#print("Kurang dari 10 =", isKurangDari)

# --------3+++++++++10-------
#isCorrect = isKurangDari and isLebihDari
#print("angka yg anda masukan: ", isCorrect)


# Latihan
# -----0+++++5----8+++++11----
#print("Latihan nomor 1")
#inputUser = float(input("Masukkan angka yg bernilai\nlebih dari 0\ndan kurang dari 5\natau lebih dari 8\ndan kurang dari 11\n"))

#isLebihDari = (inputUser > 0)
#print("Lebih dari 0 =", isLebihDari)

#isKurangDari = (inputUser < 5)
#print("Kurang dari 5 =", isKurangDari)

#isCorrect = isLebihDari and isKurangDari
#print("angka yg anda masukan: ", isCorrect)

#isLebih = (inputUser > 8)
#print("Lebih dari 8 =", isLebih)

#isKurang = (inputUser < 11)
#print("Kurang dari 11 =", isLebih)

#isCorrect = isLebih and isKurang
#print("angka yg anda masukan: ", isCorrect)


# +++++0-----5++++8+++++11----
print("Latihan nomor 2")
inputUser = float(input("Masukkan angka yg bernilai\nkurang dari 0\ndan lebih dari 5\natau krang dari 8\ndan lebih dari 11\n"))

isKurangDari = (inputUser < 0)
print("Kurang dari 0 =", isKurangDari)

isLebihDari = (inputUser > 5)
print("Lebih dari 5 =", isLebihDari)

isCorrect = isLebihDari and isKurangDari
print("angka yg anda masukan: ", isCorrect)

isKurang = (inputUser < 8)
print("Kurang dari 8 =", isKurang)

isLebih = (inputUser > 11)
print("Lebih dari 11 =", isLebih)

isCorrect = isLebihDari or isKurang
print("angka yg anda masukan: ", isCorrect)

isCorrect = isKurang and isLebih
print("angka yg anda masukan: ", isCorrect)
