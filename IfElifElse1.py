nilai = 50

if nilai == 75:
    print("nilai anda: ", nilai)
if nilai is not 60:
    print("nilai anda: ", nilai)

print(20*"=")

nilai = int(input("masukkan nilai anda: "))

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C")
elif 50 <= nilai <= 60:
    print("nilai anda adalah D, mohon perbaikan nilai")
else:
    print("maap nilai anda: ",nilai)
    print("mohon segera remedial")

print(20*"+")
print("operator logika untuk list dan string")
print(" ")

gorengan=["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"]
beli = "jus"

if beli in gorengan:
    print('Mamang bilang, " ya, saya jual',beli,'"')
if not beli in gorengan:
    print('" saya gak jual',beli,'"')

karakter = "u"
if karakter in beli:
    print("ada",karakter,"di",beli)
else:
    print("tidak ada",karakter,"di",beli)


uang  = input("berapa uang anda? ")
utang = 20000

if int(uang) < utang:
    print("maap coy duit lu kurang ni")
elif int(uang) == utang:
    print("thx coy pas nih!")
else:
    print("waduh uangnya lebih!")


"""
lebih dari satu syarat
and or not
&   |   !=

"""

print("PUTRI MENCARI JODOH!")

tamu = "pria"
baik = True
rajin = False

if baik & rajin & (tamu == "pria"):
    print("Kita nikah yuk!")
elif baik & rajin & (tamu == "cewe"):
    print("kita saudaraan yuk!")
else:
    print("Pergi sana!")