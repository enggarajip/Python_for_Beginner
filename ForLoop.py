# list sebagai iterable
#gorengan = ["bakwan","Cireng","Tahu isi", "Tempe goreng", "Ubi goreng"]

#for g in gorengan:
    #print(g)
    #print(len(g))

# string sebagai iterable
#bakwan = 'bakwan'

#for i in bakwan:
    #print(i)

# for di dalam for
gorengan = ["bakwan","Cireng","Tahu isi", "Tempe goreng", "Ubi goreng"]
buah = ["semangka", "jeruk", "apel", "anggur"]
sayur = ["kangkung", "wortel", "tomat", "kentang"]

daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)