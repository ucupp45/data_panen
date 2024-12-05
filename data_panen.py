data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1040,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# Menampilkan seluruh data dari data_panen
for lokasi, data in data_panen.items():
    print(f"Lokasi: {lokasi}")
    print(f"  Nama Lokasi: {data['nama_lokasi']}")
    print(f"  Hasil Panen:")
    for komoditas, jumlah in data['hasil_panen'].items():
        print(f"    - {komoditas.capitalize()}: {jumlah}")
    print()
    
# Mendapatkan hasil panen jagung dari lokasi2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung dari lokasi2 (Kebun B): {hasil_jagung_lokasi2}")

# # Mendapatkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")

# Membuat variabel terpisah untuk menyimpan hasil panen padi dan kedelai
padi = {}
kedelai = {}

# Menyimpan hasil panen padi dan kedelai ke dalam dictionary baru
hasil_panen_padi_kedelai = {}

# for lokasi, data in data_panen.items():
#     nama_lokasi = data['nama_lokasi']
#     hasil_panen_padi_kedelai[nama_lokasi] = {
#         'padi': data['hasil_panen']['padi'],
#         'kedelai': data['hasil_panen']['kedelai']
#     }

# # Menampilkan hasil
# print("Hasil Panen Padi dan Kedelai:")
# for nama_lokasi, hasil in hasil_panen_padi_kedelai.items():
#     print(f"{nama_lokasi}: Padi = {hasil['padi']}, Kedelai = {hasil['kedelai']}")


# for lokasi, data in data_panen.items():
#     nama_lokasi = lokasi  # Menggunakan nama lokasi sebagai kunci
#     padi[nama_lokasi] = data['hasil_panen']['padi']
#     kedelai[nama_lokasi] = data['hasil_panen']['kedelai']

# # Menampilkan hasil
# print("Jumlah Hasil Panen Padi:")
# for lokasi, jumlah in padi.items():
#     print(f"{lokasi}: {jumlah}")

# print("\nJumlah Hasil Panen Kedelai:")
# for lokasi, jumlah in kedelai.items():
#     print(f"{lokasi}: {jumlah}")
    
# Mengevaluasi setiap lokasi berdasarkan hasil panen
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    hasil_padi = data['hasil_panen']['padi']
    hasil_jagung = data['hasil_panen']['jagung']
    
    # Percabangan untuk menentukan status lokasi
    if hasil_padi > 1300 or hasil_jagung > 800:
        print(f"Lokasi {nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {nama_lokasi} dalam kondisi baik.")