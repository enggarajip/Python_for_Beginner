# Input dari user

# data yg dimasukkan pasti string
data = input("Masukkan data: ")
print("data =", data, ",type =", type(data))

# jika ingin mengambil data int dan float, maka
angka = int(input("Masukkan data: "))
angka = float(input("Masukkan data: "))
print("data =", angka, ",type =", type(angka))

# jika mengambil data boolean, maka
biner = bool(int(input("Masukkan data boolean: ")))
print("data =", biner, ",type: ",type(biner))
