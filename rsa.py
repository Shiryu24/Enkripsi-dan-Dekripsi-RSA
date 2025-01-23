import random
import time
import base64

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
    # Mengonversi list cipher menjadi string yang dipisahkan koma
    cipher_string = ','.join(map(str, cipher))
    # Encode hasil enkripsi ke dalam format Base64
    cipher_bytes = base64.b64encode(cipher_string.encode('utf-8'))
    return cipher_bytes.decode('utf-8')

# Fungsi untuk dekripsi
def decrypt(dn, ciphertext):
    d, n = dn
    # Decode dari Base64
    cipher_bytes = base64.b64decode(ciphertext)
    cipher_string = cipher_bytes.decode('utf-8')
    # Mengonversi string kembali menjadi list angka
    cipher = list(map(int, cipher_string.split(',')))
    plain = [chr((char ** d) % n) for char in cipher]
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
        print("Kunci privat (simpan dengan baik): ", private)
        
        text = input("Masukkan teks yang akan dienkripsi:\n")
        
        # Mengukur waktu enkripsi
        start_time = time.time()
        encrypted_text = encrypt(public, text)
        end_time = time.time()
        print("Teks hasil enkripsi:\n", encrypted_text)
        print(f"Waktu yang dibutuhkan untuk enkripsi: {end_time - start_time:.6f} detik")
    
    else:
        d = int(input("Masukkan nilai d (kunci privat (d,n)): "))
        n = int(input("Masukkan nilai n (kunci privat (d,n)): "))
        private = (d, n)
        
        encrypted_text = input("Masukkan pesan hasil enkripsi: ")
        
        # Mengukur waktu dekripsi
        start_time = time.time()
        decrypted_text = decrypt(private, encrypted_text)
        end_time = time.time()
        print("Teks hasil dekripsi:\n", decrypted_text)
        print(f"Waktu yang dibutuhkan untuk dekripsi: {end_time - start_time:.6f} detik")

# Memanggil fungsi utama
programUtama()
