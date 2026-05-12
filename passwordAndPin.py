import os
import platform
import socket
import subprocess
from datetime import datetime

def pause():
    input("\nTekan Enter untuk lanjut...")

def clear():
    os.system("clear")

def menu():
    clear()
    print("=====================================")
    print("          MENU PYTHON SCRIPT         ")
    print("=====================================")
    print("1. Tampilkan tanggal")
    print("2. Tampilkan waktu")
    print("3. Lihat user aktif")
    print("4. Lihat folder sekarang")
    print("5. Lihat isi folder")
    print("6. Lihat hostname")
    print("7. Lihat sistem operasi")
    print("8. Lihat uptime")
    print("9. Lihat kapasitas storage")
    print("10. Lihat penggunaan RAM")
    print("11. Lihat proses berjalan")
    print("12. Lihat koneksi jaringan")
    print("13. Ping Google")
    print("14. Bersihkan layar")
    print("15. Tampilkan path shell")
    print("16. Tampilkan file tersembunyi")
    print("17. Buat folder baru")
    print("18. Buat file baru")
    print("19. Edit isi file")
    print("20. Lihat isi file")
    print("21. Hapus file")
    print("22. Keluar")
    print("=====================================")

def run(cmd):
    os.system(cmd)

def edit_file_manual(file):
    print("Mode edit manual.")
    print("Ketik isi file. Selesai kalau kamu ketik satu titik saja: .")

    with open(file, "w") as f:
        while True:
            line = input("> ")
            if line == ".":
                break
            f.write(line + "\n")

    print("Isi file berhasil disimpan.")

while True:
    menu()
    pil = input("Pilih menu: ")

    if pil == "1":
        print(datetime.now().date())

    elif pil == "2":
        print(datetime.now().strftime("%H:%M:%S"))

    elif pil == "3":
        run("whoami")

    elif pil == "4":
        print(os.getcwd())

    elif pil == "5":
        run("ls")

    elif pil == "6":
        print(socket.gethostname())

    elif pil == "7":
        print(platform.platform())

    elif pil == "8":
        run("uptime")

    elif pil == "9":
        run("df -h")

    elif pil == "10":
        run("free -h")

    elif pil == "11":
        run("ps")

    elif pil == "12":
        if os.system("which ip > /dev/null 2>&1") == 0:
            run("ip addr")
        elif os.system("which ifconfig > /dev/null 2>&1") == 0:
            run("ifconfig")
        else:
            print("Perintah jaringan tidak tersedia.")

    elif pil == "13":
        run("ping -c 4 google.com")

    elif pil == "14":
        clear()

    elif pil == "15":
        print(os.environ.get("SHELL", "Shell tidak ditemukan"))

    elif pil == "16":
        run("ls -la")

    elif pil == "17":
        folder = input("Nama folder: ")

        if folder == "":
            print("Batal, nama folder kosong.")
        else:
            os.makedirs(folder, exist_ok=True)
            print(f"Folder dibuat: {folder}")

    elif pil == "18":
        file = input("Nama file: ")

        if file == "":
            print("Batal, nama file kosong.")
        else:
            open(file, "w").close()
            print(f"File dibuat: {file}")

    elif pil == "19":
        file = input("Nama file yang mau diedit: ")

        if file == "":
            print("Batal, nama file kosong.")
        else:
            edit_file_manual(file)

    elif pil == "20":
        file = input("Nama file yang mau dilihat: ")

        if file == "":
            print("Batal, nama file kosong.")

        elif os.path.isfile(file):
            with open(file, "r") as f:
                print(f.read())

        else:
            print("File tidak ditemukan.")

    elif pil == "21":
        file = input("Nama file yang mau dihapus: ")

        if file == "":
            print("Batal, nama file kosong.")

        elif os.path.isfile(file):
            os.remove(file)
            print("File berhasil dihapus.")

        else:
            print("File tidak ditemukan.")

    elif pil == "22":
        print("Keluar...")
        break

    else:
        print("Pilihan tidak valid!")

    pause()
