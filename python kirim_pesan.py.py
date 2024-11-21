import pywhatkit
import time

# Daftar kontak
contacts = [   
    {"name": "Ahmad Asroni", "number": "+6281338047227"},  
    {"name": "Yanto Yulianto", "number": "+62818436915"},   
    {"name": "Gungde Wahyu", "number": "+6281999555987"},    
]

# Fungsi untuk mengirim pesan WhatsApp otomatis
def send_wa(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    print(f"Mengirim pesan ke {number}")

# Waktu pengiriman
hour = 17  # Jam pengiriman
minute = 22  # Menit pengiriman, tambahkan interval waktu antar pesan

# Mengirim pesan ke setiap kontak
for contact in contacts:
    # Membuat pesan yang dipersonalisasi
    message = f"""Selamat sore {contact['name']}, Mohon maaf mengganggu waktunya. Izin saya mewakili kepanitiaan pendirian Politeknik Digital Bali. Mengucapkan terima kasih atas kesediaan {contact['name']} bergabung dalam grup rekrutmen calon dosen kami.


Saat ini, kami sedang dalam proses pengumpulan data calon dosen untuk penempatan di tiga program studi:
D4 Keamanan Sistem Informasi
D4 Kecerdasan Buatan dan Robotik
D4 Teknologi Rekayasa Transportasi

Izin memohon kiranya {contact['name']} berkenan mengisi formulir data calon dosen melalui tautan berikut:
https://s.id/RecruitmentDosenPolDigBali

Apabila {contact['name']} mengalami kendala dalam pengisian, jangan ragu untuk menghubungi saya kembali.

Atas perhatian dan kerja samanya, kami mengucapkan terima kasih yang sebesar-besarnya 🙏."""

    # Mengirim pesan
    send_wa(contact["number"], message, hour, minute)
    
    # Menunggu beberapa detik untuk mencegah blokir otomatis WhatsApp
    time.sleep(15)
    
    # Menambahkan menit untuk pesan berikutnya
    minute += 1
    if minute >= 60:
        minute = 0
        hour += 1
