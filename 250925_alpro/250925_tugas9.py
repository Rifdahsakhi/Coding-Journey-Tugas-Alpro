ar = 7

while True:
    n = int(input("Masukkan angka dari 1-10: ")) 
    if n < 7 and n >= 1:
        print("Terlalu kecil.")
    elif n > 7 and n <= 10:
        print("Terlalu besar.")
    elif n == 7:
        print("Benar!")
        break