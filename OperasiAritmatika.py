# Operasi Aritmatika

a = 10
b = 3

# Operasi Tambah +
hasil = a + b
print(a,'+',b, '=', hasil)

# Operasi Kurang -
hasil = a - b
print(a,'-',b, '=', hasil)

# Operasi Perkalian
hasil = a * b
print(a, '*',b, "=", hasil)

# Operasi Pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# Operasi Eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi Modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi Floor Division //
hasil = a // b
print(a, '//', b, '=', hasil) # dibulatkan ke bawah

# Prioritas Operasi, operational precedence
'''
    1. ()
    2. Exponen **
    3. Perkalian dan teman-teman * / ** % //
    4. Pertambahan dan pengurangan + - 
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)
# kurung akan mengambil langkah paing pertama
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=', hasil)