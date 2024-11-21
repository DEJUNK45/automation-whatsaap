import pywhatkit
import time

# Daftar kontak
contacts = [
    {"name": "I Putu Yesha Ariwanta", "number": "+6285156330909"},
    {"name": "Ahmad Asroni", "number": "+6281338047227"},
    {"name": "Dinda Maharani", "number": "+6282339855829"},
    {"name": "Eka Apriyanthi", "number": "+6282113112711"},
    {"name": "I Gd Pradipta Adi Nugraha", "number": "+6287861863842"},
    {"name": "Gede Etika", "number": "+6281916712221"},
    {"name": "Gung De Bima", "number": "+6287861492942"},
    {"name": "I Gusti Ayu Nandia", "number": "+6287873338487"},
    {"name": "Ardy Putra", "number": "+6287862221810"},
    {"name": "Putu Happy", "number": "+6282235302418"},
    {"name": "Jana Satvika", "number": "+6282237446606"},
    {"name": "Gungde Wahyu", "number": "+6281999555987"},
    {"name": "Ode Wahyu", "number": "+6281237306595"},
    {"name": "Bapak Reksa", "number": "+628179654381"},
    {"name": "Dwi Raka Mudiarta", "number": "+6287860011780"},
    {"name": "Dwi Suta Atmaja", "number": "+6281999280337"},
    {"name": "Eka Widastra", "number": "+6285216096305"},
    {"name": "Gusmang Wijana", "number": "+6285738399086"},
    {"name": "Wira Kusuma", "number": "+6281236125149"},
]

# Fungsi untuk mengirim pesan WhatsApp otomatis
def send_wa(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    print(f"Mengirim pesan ke {number}")

# Waktu pengiriman
hour = 15  # Jam pengiriman
minute = 23  # Menit pengiriman, tambahkan interval waktu antar pesan

# Mengirim pesan ke setiap kontak
for contact in contacts:
    # Membuat pesan yang dipersonalisasi
    message = f"""Selamat siang {contact['name']}, perkenalkan saya Dewa Gede Agung Aditya. Saya dapat nomor {contact['name']} dari Bli Agus Oka. Izin menjelaskan maksud saya menghubungi {contact['name']} untuk menginformasikan terkait peluang menjadi calon dosen di Politeknik Digital Bali, instansi ini masih dalam proses pengusulan perizinan pendirian oleh pihak kementerian. Apabila {contact['name']} berkenan, mohon kesediaannya untuk mengisi formulir pada tautan berikut:
https://s.id/RecruitmentDosenPolDigBali

Sebagai informasi awal, program studi yang akan diajukan ada 3:
- D4 Keamanan Sistem Informasi;
- D4 Kecerdasan Buatan dan Robotik;
- D4 Teknologi Transportasi.

Pengumpulan data ini diperlukan sebagai salah satu syarat pendirian perguruan tinggi vokasi. Jika secara administrasi sesuai dengan program studi yang ditawarkan, nantinya dari lembaga pengusul pendirian program studi akan memberikan biaya tunggu sebesar 1.000.000;-

Setelah mengisi form, {contact['name']} bisa bergabung pada grup WA melalui tautan berikut untuk menerima update selanjutnya:
https://chat.whatsapp.com/IudIVBoBEV5CMs10wESz3O

Demikian yang ingin saya sampaikan. Mohon maaf jika saya mengganggu waktu {contact['name']}. Terima Kasih."""

    # Mengirim pesan
    send_wa(contact["number"], message, hour, minute)
    
    # Menunggu beberapa detik untuk mencegah blokir otomatis WhatsApp
    time.sleep(30)
    
    # Menambahkan menit untuk pesan berikutnya
    minute += 1
    if minute >= 60:
        minute = 0
        hour += 1
