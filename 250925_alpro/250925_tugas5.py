n = int (input ("Masukkan angka: "))

i = 1
jumlah = 0
while i <= n :
    if i % 2 == 1 :
        print (i)
        jumlah += i
        
    i += 1
print ("Jumlah angka ganjil dari 1 sampai ", n, "adalah", jumlah)