# 🚀 Jetson Nano Basic Hardware Control

Kumpulan script Python dasar untuk mengontrol berbagai komponen hardware menggunakan **NVIDIA Jetson Nano**. Repositori ini dirancang untuk memudahkan pemula dalam mempelajari antarmuka GPIO pada Jetson Nano.

## 🛠️ Komponen yang Didukung

Repositori ini mencakup contoh kode untuk berbagai sensor dan aktuator:

### 🎮 Aktuator & Output
- **Motor DC**: Kontrol kecepatan (PWM) dan arah menggunakan driver motor.
- **Motor Servo**: Kendali posisi sudut servo.
- **Stepper Motor**: Kontrol langkah presisi untuk motor stepper.
- **Seven Segment**: Menampilkan angka pada display 7-segment.
- **LED**: Kontrol dasar ON/OFF pada lampu LED.

### 📡 Sensor & Input
- **Sensor Ultrasonic**: Mengukur jarak objek (HC-SR04).
- **Sensor PIR**: Deteksi gerakan manusia.
- **Sensor LDR**: Deteksi intensitas cahaya (analog/digital).
- **Sensor Infrared**: Deteksi halangan atau garis.
- **Keypad**: Input matriks tombol.
- **Push Button**: Input digital dari tombol tekan.

---

## ⚙️ Persiapan Sistem

Sebelum menjalankan script, pastikan library `Jetson.GPIO` sudah terinstall di Jetson Nano anda:

```bash
sudo pip3 install Jetson.GPIO
```

Pastikan user anda memiliki izin untuk mengakses GPIO:
```bash
sudo groupadd -f -r gpio
sudo usermod -a -G gpio your_username
```
*(Ganti `your_username` dengan nama user anda, lalu restart Jetson Nano).*

---

## 🚀 Cara Penggunaan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/just-naumi/Jetson-Nano-Basic-Control-.git
   cd Jetson-Nano-Basic-Control-
   ```

2. Jalankan salah satu script (contoh: Motor DC):
   ```bash
   python3 MotorDC.py
   ```

---

## 📂 Struktur File

Setiap file `.py` bersifat mandiri (*standalone*) dan sudah mencakup inisialisasi pin serta logic dasar penggunaan komponen.

- `MotorDC.py`: Kontrol driver motor L298N/sejenis.
- `SensorUltrasonic.py`: Pembacaan jarak dalam cm.
- `Keypad.py`: Pembacaan input 4x4 atau 4x3.
- ... dan file lainnya sesuai nama komponennya.

---

## 📝 Catatan
Script ini menggunakan mode penomoran pin **GPIO.BOARD**. Pastikan kabel jumper anda terpasang sesuai dengan nomor pin fisik pada header 40-pin Jetson Nano.

---
**Author:** [just_naumi](https://github.com/just-naumi)
