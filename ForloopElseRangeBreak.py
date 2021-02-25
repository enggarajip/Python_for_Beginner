angka = int(input("masukkan angka: "))

for i in range(0,10):
    print(i)

    if i is angka:
        print("angka ditemukan",angka)
        break
else:
    print("angka tidak ditemukan")
print("space di luar for")