from datetime import datetime
from termcolor import colored
from art import text2art

def tampilan_awal():
    ascii_art = text2art("HydroCheck")
    print(ascii_art)
    print(colored("==============================", "black"))
    print(colored("       SELAMAT DATANG", "blue", attrs=["bold"]))
    print(colored("       DI HYDROCHECK", "blue", attrs=["bold"]))
    print("==============================")
    print("\n💧 Aplikasi Cek Keseimbangan Cairan\n")
    print("🔍 Dengan HydroCheck, Anda dapat:")
    print("- Memeriksa warna urine untuk mengetahui status hidrasi")
    print("- Melihat riwayat pengecekan")
    print("- Menerima pengingat minum\n")

def konfirmasi_lanjut():
    while True:
        pengguna = input("Lanjut? Yay/Nay? : ").lower()
        if pengguna in ["y", "yay", "ya"]:
            return True
        elif pengguna in ["n", "nay", "no"]:
            print("Terima kasih telah menggunakan HydroCheck. Sampai jumpa!")
            return False
        else:
            print("Input tidak valid. Silakan masukkan 'Yay' untuk melanjutkan atau 'Nay' untuk keluar.\n")

def menu_utama():
    while True:
        print("=" * 50)
        print(" Menu Utama:")
        print("1. Cek Keseimbangan Cairan")
        print("2. Riwayat Pengecekan")
        print("3. Pengingat Minum")
        print("4. Keluar\n")

        pilihan_input = input("Pilih Menu (1-4): ")
        print("=" * 50)

        if not pilihan_input.isdigit():
            print("Input tidak valid. Silakan masukkan angka antara 1-4.")
            continue

        return int(pilihan_input)

def get_status_hidrasi(warna_urin,frekuensi_pipis):
    """
    Mengembalikan status hidrasi berdasarkan input warna urine.
    """
    if warna_urin in ["1", "bening"]:
        return "Terhidrasi, Tetap Teruskan!"
    elif warna_urin in ["2", "kuning pucat"]:
        return "Tercukupi, Tambah Semangat!"
    elif warna_urin in ["3", "kuning tua"]:
        return "Lumayan terhidrasi, Semangat!"
    elif warna_urin in ["4", "kuning gelap"]:
        return "Cukup Tercukupi, Tambah Lagi!"
    elif warna_urin in ["5", "orange"]:
        return "Dehidrasi, Ayoo Tambah Kenceng Minumnya!"
    elif warna_urin in ["6", "biru", "kehijauan", "biru/kehijauan"]:
        return "Tercukupi, Hanya Pengaruh Obat Aman!"
    elif warna_urin in ["7", "kemerahan"]:
        return "Tidak Tercukupi, Ada Riwayat Penyakit?"
    elif warna_urin in ["8", "cokelat"]:
        return "Tidak Tercukupi, Tambah Terus Kasian Ginjal :)"
    elif warna_urin in ["9", "keruh"]:
        return "Tidak Tercukupi, Ada Riwayat Sakit?"
    else:
        return None

def cek_keseimbangan_cairan(riwayat_cek, pengingat_aktif):
    while True:
        print("Masukkan Warna Urine:")
        print("Pilih dari berikut: \n- Bening (1)\n- Kuning Pucat (2)\n- Kuning Tua (3)\n- Kuning Gelap (4)\n- Orange (5)")
        print("- Biru/Kehijauan (6)\n- Kemerahan (7)\n- Cokelat (8)\n- Keruh (9)")

        warna_urin = input("Warna Urine: ").strip().lower()
        while True: 
            frekuensi_pipis = input("Berapa Kali Warnanya Terulang? ")
            if frekuensi_pipis.isdigit():
                break
            else: 
                print("Input frekuensi harus berupa angka, silahkan ulangi")
            
        status_hidrasi = get_status_hidrasi(warna_urin,frekuensi_pipis)

        if status_hidrasi is None:
            print(colored("Input tidak valid. Masukkan warna urine yang sesuai.\n", attrs=["bold"]))
            continue

        waktu_cek = datetime.now().strftime("%d %B %Y, pukul %H:%M")
        
        riwayat_cek.append({
            "waktu": waktu_cek,
            "warna": warna_urin,
            "status": status_hidrasi,
            "frekuensi": frekuensi_pipis,
        })

        print("\nStatus Hidrasi:", status_hidrasi)
        print("Data pengecekan disimpan.\n")
            
        if pengingat_aktif:
            print("⚠️ Pengingat: Jangan lupa minum air putih minimal 8x dalam sehari!")
            if warna_urin in ["5", "7", "8", "9"]:
                print("⚠️ Kondisi warna urine Anda membutuhkan perhatian lebih. Disarankan untuk konsultasi dengan dokter.")

        print("Kembali ke menu utama...\n")
        return riwayat_cek

def riwayat_pengecekan(riwayat_cek):
    print("\n📋 Riwayat Pengecekan:")
    if not riwayat_cek:
        print("Belum ada riwayat pengecekan.\n")
    else:
        for idx, cek in enumerate(riwayat_cek, start=1):
            print(f"{idx}. Waktu: {cek['waktu']}, Warna Urine: {cek['warna'].title()}, Status: {cek['status']}, Frekuensi: {cek['frekuensi']}")

def pengingat_minum(pengingat_aktif):
    print("Pengingat minum saat ini:", "AKTIF" if pengingat_aktif else "NONAKTIF")
    while True:
        pilihan_pengingat = input("Apakah Anda ingin mengaktifkan/nonaktifkan pengingat minum? (aktif/nonaktif): ").lower()
        if pilihan_pengingat in ["aktif", "aktifkan"]:
            print("Pengingat minum telah diaktifkan.")
            return True
        elif pilihan_pengingat in ["nonaktif", "nonaktifkan"]:
            print("Pengingat minum telah dinonaktifkan.")
            return False
        else:
            print("Input tidak valid. Silakan masukkan 'aktif' atau 'nonaktif'.")

def keluar_program():
    while True:
        konfirmasi_keluar = input("Anda yakin ingin keluar? Semua data tidak akan tersimpan (ya/tidak): ").lower()
        if konfirmasi_keluar in ["ya", "y", "yes", "ye"]:
            print("Keluar dari program. Terima kasih telah menggunakan HydroCheck!")
            return True
        elif konfirmasi_keluar in ["tidak", "t", "no", "n"]:
            print("Kembali ke menu utama.\n")
            return False
        else:
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.\n")

if __name__ == "__main__":
    tampilan_awal()
    if konfirmasi_lanjut():
        riwayat_cek = []
        pengingat_aktif = False

        while True:
            pilihan = menu_utama()
            if pilihan == 1:
                riwayat_cek = cek_keseimbangan_cairan(riwayat_cek, pengingat_aktif)
            elif pilihan == 2:
                riwayat_pengecekan(riwayat_cek)
            elif pilihan == 3:
                pengingat_aktif = pengingat_minum(pengingat_aktif)
            elif pilihan == 4:
                if keluar_program():
                    break
            else:
                print("Input tidak valid, silahkan masukkan nomor 1-4")
                continue
