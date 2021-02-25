data = "ini adalah string"
print(data)
print(type(data))

#  1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('Mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Ucup")

# tab
print("Ucup\tOtong, jauhan")

# backspace
print("ucup\botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF => line feed => unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR => carriage return => commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF => line feed carriage return => windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
nama : ucup
kelas : 3 sd
""")

# multiline literal string dan raw
print(r"""
nama : ucup
kelas : 3\sd\new normal
website : www.ucup.com/newID
""")