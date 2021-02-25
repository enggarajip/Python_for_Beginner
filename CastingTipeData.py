# Casting adalah merubah tipe  data dari satu tipe ke tipe yg lain
# tipe data = int, float, str, bool

## INTEGER
print("====INTEGER====")
data_int = 9;
print("Data = ", data_int, "Type = ",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # data akan false jika nilai int 0
print("Data = ", data_float, "Type = ",type(data_float))
print("Data = ", data_str, "Type = ",type(data_str))
print("Data = ", data_bool, "Type = ",type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 8.8;
print("Data = ", data_float, "Type = ",type(data_float))

data_int   = int(data_float) # akan dibulatkan ke bawah
data_str   = str(data_float)
data_bool  = bool(data_float) #  akan false jika nilai int 0
print("Data = ", data_int, "Type = ",type(data_int))
print("Data = ", data_str, "Type = ",type(data_str))
print("Data = ", data_bool, "Type = ",type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = False;
print("Data = ", data_bool, "Type = ",type(data_bool))

data_int   = int(data_bool) # akan dibulatkan ke bawah
data_str   = str(data_bool)
data_float  = float(data_bool) #  akan false jika nilai int 0
print("Data = ", data_int, "Type = ",type(data_int))
print("Data = ", data_str, "Type = ",type(data_str))
print("Data = ", data_float, "Type = ",type(data_float))

## STRING
print("====STRING====")
data_str = "30";
print("Data = ", data_str, "Type = ",type(data_str))

data_int   = int(data_str) # string harus angka
data_bool   = bool(data_str) # string harus angka
data_float  = float(data_str) #  false jika string tak ada nilai/kosong
print("Data = ", data_int, "Type = ",type(data_int))
print("Data = ", data_bool, "Type = ",type(data_bool))
print("Data = ", data_float, "Type = ",type(data_float))