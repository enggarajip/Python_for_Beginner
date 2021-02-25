"""
    Loop
    - while - For In
"""

count = 0

while count < 5:
    print("Yaay kita menikah!")
    count = count+1
else:
    print("akhirnya selesai di count = ", count)

print('===For IN===')

text = 'Python'
orang = ['Rijal', 'Ami', 'Mia']
nomor = '1234'

for angka in nomor:
    print("Berhitung ", nomor)

print("BIKIN SEGITIGA")
# Nested loop

x = 0

while x < 5:
    y = 0
    while y < x:
        print("*", end='')
        y = y+1
    print()
    x = x+1


print("==PERKALIAN==")
# Nested for in

for a in range(1,7):
    for b in range(1,7):
        c = a*b
        print(c, end=" ")
    print()