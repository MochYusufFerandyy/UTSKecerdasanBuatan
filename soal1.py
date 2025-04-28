def tampilkan_menu():
    print("=== Sistem Pakar Identifikasi Hama Tanaman ===")
    print("Silakan masukkan kondisi tanaman Anda dengan menjawab ya/tidak.")
    print("Gejala yang diamati:")
    print("1. Daun menguning")
    print("2. Bercak hitam pada daun")
    print("3. Daun berlubang")
    print("4. Tanaman layu")
    print("---------------------------------------------")

def input_gejala():
    gm = input("Apakah daun menguning? (ya/tidak): ").strip().lower() == "ya"
    bh = input("Apakah terdapat bercak hitam pada daun? (ya/tidak): ").strip().lower() == "ya"
    db = input("Apakah daun berlubang? (ya/tidak): ").strip().lower() == "ya"
    tl = input("Apakah tanaman layu? (ya/tidak): ").strip().lower() == "ya"
    return gm, bh, db, tl

def identifikasi_hama(daun_menguning, bercak_hitam, daun_berlubang, tanaman_layu):
    if daun_menguning and tanaman_layu:
        return "Ulat Tanah"
    elif bercak_hitam and daun_berlubang:
        return "Kumbang Daun"
    elif daun_menguning and bercak_hitam:
        return "Penyakit Jamur"
    elif daun_berlubang and tanaman_layu:
        return "Ulat Grayak"
    else:
        return "Tidak diketahui, butuh analisis lanjutan."

def main():
    tampilkan_menu()
    gm, bh, db, tl = input_gejala()
    hasil = identifikasi_hama(gm, bh, db, tl)
    print("\n=== HASIL IDENTIFIKASI ===")
    print("Hama atau penyakit yang teridentifikasi:", hasil)
    print("============================")

if __name__ == "__main__":
    main()
