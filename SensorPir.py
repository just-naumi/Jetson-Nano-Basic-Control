import Jetson.GPIO as GPIO
import time

# Menggunakan penomoran fisik (BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin 7 terhubung ke pin OUT pada sensor PIR
PIR_Pin = 7

# Atur pin sebagai INPUT
GPIO.setup(PIR_Pin, GPIO.IN)

print("Sistem Deteksi Gerakan Aktif...")
print("Tekan Ctrl+C untuk berhenti.")

# Berikan waktu sensor untuk kalibrasi (sekitar 10-30 detik jika baru dinyalakan)
print("Menunggu kalibrasi sensor...")
time.sleep(2) 

try:
    while True:
        # Membaca status logika dari sensor
        if GPIO.input(PIR_Pin):
            print("Peringatan: Gerakan Terdeteksi!")
        else:
            print("Status: Aman")
            
        # Delay singkat agar terminal mudah dibaca
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    GPIO.cleanup()