# Latihan konversi satuan temperature

# program konversi celcius ke satuan lain

#celcius = float(input("Masukkan suhu dalam celcius: "))
#print("suhu adalah: ",celcius, "Celcius")

# reamur
# (4/5) * c
#reamur = (4/5) * celcius
#print("suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
# (9/5)*c+32
#fahrenheit = ((9/5) * celcius) + 32
#print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
# c+273
#kelvin = celcius + 273
#print("suhu dalam kelvin adalah", kelvin, "Kelvin")

# fahrenheit ke kelvin
# 5/9*(f - 32)+273
fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print("suhu adalah: ",fahrenheit, "Fahrenheit")

kelvin = 5/9*(fahrenheit - 32)+273
print("suhu dalam kelvin adalah", kelvin,"Kelvin")

# kelvin ke fahrenheit
# 9/5*(k-273)+32
kelvin = float(input("Masukkan suhu dalam kelvin: "))
print("suhu adalah: ",kelvin,"Kelvin")

kelvin = 9/5*(kelvin-273)+32
print("suhu dalam fahrenheit adalah", kelvin,"Fahrenheit")