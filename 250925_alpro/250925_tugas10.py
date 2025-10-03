ulang = 3
usn = "admin"
psw = "1234"

for i in range (ulang):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if  password != psw and username != usn:
        print("Login gagal! Username atau password salah.") 
        print(f"Sisa percobaan: {ulang - i - 1}")
    elif username == usn and password != psw:
        print("Password salah!")
        print(f"Sisa percobaan: {ulang - i - 1}")
    elif username != usn and password == psw:
        print("Username salah!")
        print(f"Sisa percobaan: {ulang - i - 1}")
    elif username == usn and password == psw:
        print("Login berhasil!")
        break

         
