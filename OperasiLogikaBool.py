# Operasi Logika atau Boolean

# not, or, and, xor

# Not
print("====NOT====")
a = False
c = not a

print("data a =",a)
print("--------------NOT")
print("data c =", c)

# Or (jika salah satu True maka hasilnya True)
print("====OR====")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)

# And (jika dua buah nilai True maka hasilnya True)
print("====AND====")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,'AND',b,' =',c)
a = True
b = True
c = a and b
print(a,'AND',b,'  =',c)

# XOR (akan true jika salah satunya true, sisanya false)
print("====XOR====")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'  =',c)