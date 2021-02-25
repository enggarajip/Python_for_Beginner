# setiap hasil operasi komparasi adalah boolean

# >,<,>=,>=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("===Lebih dari (>)===")
hasil = a > 3
print(a,'>',3,'=', hasil)
hasil = b > 3
print(b,'>',3,'=', hasil)
hasil = b > 2
print(b,'>',2,'=', hasil)

# Lebih kecil dari <
print("===Kurang dari (<)===")
hasil = a < 3
print(a,'<',3,'=', hasil)
hasil = b < 3
print(b,'<',3,'=', hasil)
hasil = b < 2
print(b,'<',2,'=', hasil)

# Lebih dari sama dengan
print("===Lebih dari sama dengan (>=)===")
hasil = a >= 3
print(a,'>=',3,'=', hasil)
hasil = b >= 3
print(b,'>=',3,'=', hasil)
hasil = b >= 2
print(b,'>=',2,'=', hasil)

# Kurang dari sama dengan
print("===Kurang dari sama dengan (<=)===")
hasil = a <= 3
print(a,'<=',3,'=', hasil)
hasil = b <= 3
print(b,'<=',3,'=', hasil)
hasil = b <= 2
print(b,'<=',2,'=', hasil)

# Sama dengan
print("===Sama dengan (==)===")
hasil = a == 4
print(a,'==',4,'=', hasil)
hasil = b == 3
print(b,'==',3,'=', hasil)
hasil = b == 2
print(b,'==',2,'=', hasil)

# Tidak sama dengan
print("===Tidak sama dengan (!=)===")
hasil = a != 3
print(a,'!=',3,'=', hasil)
hasil = b != 3
print(b,'!=',3,'=', hasil)
hasil = b != 2
print(b,'!=',2,'=', hasil)

# is sebagai komparasi object identity
print("===Object identity (is)===")
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai y =",y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 7 # ini adalah assigment membuat object
y = 6
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai y =",y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# is not sebagai komparasi object identity
print("===Object identity (is not)===")
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai y =",y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 7 # ini adalah assigment membuat object
y = 6
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai y =",y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)