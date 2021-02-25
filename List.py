Data = [1,4,9,16,25,36,49,64]

# mengakses list
Subdata1 = Data[3]
Subdata2 = Data[-4]

# memotong list
Subdata3 = Data[2:5]
Subdata4 = Data[-5:]

Data2 = [100,200,300,400,500,600,700,800]

# menambah list
Data3 = Data + Data2

# merubah content dari list

Data[5] = 56

# Mengcopy list ke variabel baru
a = Data[:] # a akan mengakses semua komponen di-copy ke a
a[4] = 87

# Merubah content list dengan menggunakan metode slicing

Data[3:5] = [11,12]

# List dalam list

x = [Data, Data2,]

# mengakses list dalam multidimensional list

y = x[0][4]

# methods untuk list
Data.append(76) # untuk menambah member

# Function yang bisa kita gunakan kepada list

panjang_list = len(Data)

print(Data)
print(panjang_list)