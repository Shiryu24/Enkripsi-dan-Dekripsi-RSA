import random
import os
import time

# Fungsi untuk mencari Greatest Common Divisor (GCD)
def pbb(a, b):
    while b:
        a, b = b, a % b
    return a

# Fungsi untuk mengecek apakah angka prima
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# Fungsi untuk mencari Modulo Invers
def mod_invers(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Fungsi untuk menghasilkan bilangan prima p dan q
def generate_pq():
    while True:
        p = random.randrange(1, 100)
        if isPrime(p):
            break
    while True:
        q = random.randrange(1, 100)
        if isPrime(q):
            break
    return p, q

# Fungsi untuk menghasilkan kunci publik dan privat
def generate_key(p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    e = random.randrange(1, m)
    g = pbb(e, m)
    while True:
        e = random.randrange(1, m)
        g = pbb(e, m)
        d = mod_invers(e, m)
        if g == 1 and e != d:
            break
    d = mod_invers(e, m)
    return (e, n), (d, n)

# Fungsi untuk enkripsi
def encrypt(en, plaintext):
    e, n = en
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Fungsi untuk dekripsi
def decrypt(dn, ciphertext):
    d, n = dn
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Fungsi utama program
def programUtama():
    print("Pilih tujuan Anda:\n 1. Enkripsi\n 2. Dekripsi")
    pil = int(input("Masukkan pilihan: "))
    while pil not in [1, 2]:
        print("Pilihan tidak valid")
        pil = int(input("Masukkan pilihan: "))
        
    if pil == 1:
        p, q = generate_pq()
        print("Hasil nilai p dan q (bilangan prima): ")
        print("p = ", p)
        print("q = ", q)
        public, private = generate_key(p, q)
        print("Kunci publik (tidak bersifat rahasia): ", public)
        print("Kunci privat (simpan dengan baik): ", private)
        print("Pilih input teks :\n 1. File\n 2. Ketik sendiri")
        pil = int(input("Masukkan pilihan: "))
        while pil not in [1, 2]:
            print("Pilihan tidak valid")
            pil = int(input("Masukkan pilihan: "))
        if pil == 1:
            path = os.getcwd()
            files = os.listdir(path + "\\files")
            namafile = input("Masukkan nama file yang terletak di folder bernama \"files\": ")
            while namafile not in files:
                print("File tidak ditemukan")
                namafile = input("Masukkan nama file yang terletak di folder bernama \"files\": ")
            namafile = path + "\\files\\" + namafile
            with open(namafile, "r") as f:
                text = f.read()
            print("Teks yang akan dienkripsi:\n", text)
        else:
            text = input("Masukkan teks yang akan dienkripsi:\n")
        
        # Mengukur waktu enkripsi
        start_time = time.time()
        encrypted_text = encrypt(public, text)
        end_time = time.time()
        print("Teks hasil enkripsi:\n", ' '.join(str(c) for c in encrypted_text))
        print(f"Waktu yang dibutuhkan untuk enkripsi: {end_time - start_time:.6f} detik")
    
    else:
        d = int(input("Masukkan nilai d (kunci privat (d,n)): "))
        n = int(input("Masukkan nilai n (kunci privat (d,n)): "))
        private = (d, n)
        pil = int(input("Pilih input teks :\n 1. File\n 2. Ketik sendiri\n Masukkan pilihan: "))
        while pil not in [1, 2]:
            print("Pilihan tidak valid")
            pil = int(input("Masukkan pilihan: "))
        if pil == 1:
            path = os.getcwd()
            files = os.listdir(path + "\\files")
            namafile = input("Masukkan nama file yang terletak di folder bernama \"files\": ")
            while namafile not in files:
                print("File tidak ditemukan")
                namafile = input("Masukkan nama file yang terletak di folder bernama \"files\": ")
            namafile = path + "\\files\\" + namafile
            with open(namafile, "r") as f:
                encrypted_text = f.read()
            print("Teks yang akan didekripsi:\n", encrypted_text)
        else:
            encrypted_text = input("Masukkan pesan hasil enkripsi: ")
        
        encrypted_text = encrypted_text.split(' ')
        encrypted_text = list(map(int, encrypted_text))
        
        # Mengukur waktu dekripsi
        start_time = time.time()
        decrypted_text = decrypt(private, encrypted_text)
        end_time = time.time()
        print("Teks hasil dekripsi:\n", decrypted_text)
        print(f"Waktu yang dibutuhkan untuk dekripsi: {end_time - start_time:.6f} detik")

# Memanggil fungsi utama
programUtama()