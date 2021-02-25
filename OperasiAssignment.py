# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5  # adalah assignment
print("nilai a =",a)

a += 1 # artinya adalah a = a + 1
print("nilai a +=1, nilai a menjadi",a)

# nilai a (6) lalu dikurang 1 = 5
a -= 1 # artinya adalah a = a - 1
print("nilai a -=1, nilai a menjadi",a)


a *= 5 # artinya adalah a = a * 5
print("nilai a *=5, nilai a menjadi",a)

a /= 2 # artinya adalah a = a / 2
print("nilai a /=2, nilai a menjadi",a)

b = 10
print("\nnilai b =",b)

# modulus dan floor division
b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10
print("nilai b =",b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

# pangkat atau eksponen
a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 3, nilai a adalah", a)

# operasi bitwise
# OR
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= false, nilai c adalah",c)
c = False
print("nilai c =",c)
c |= False
print("nilai c |= false, nilai c adalah",c)

# AND
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= false, nilai c adalah",c)
c = True
print("nilai c =",c)
c &= True
print("nilai c &= true, nilai c adalah",c)

# XOR
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= false, nilai c adalah",c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= true, nilai c adalah",c)

# geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d adalah",format(d,'04b'))

d = 0b0100
print("\nnilai d =",format(d,'04b'))
d <<=  2
print("nilai d <<= 2, nilai d adalah",format(d,'04b'))