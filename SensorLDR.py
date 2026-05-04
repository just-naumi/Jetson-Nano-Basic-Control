import Jetson.GPIO as GPIO
import time

# Menggunakan penomoran fisik (BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin 7 terhubung ke pin DO (Digital Output) pada modul LDR
LDR_Pin = 7

# Atur pin sebagai INPUT
GPIO.setup(LDR_Pin, GPIO.IN)

print("Sistem Monitoring Cahaya Aktif...")
print("Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        # Membaca status logika dari sensor
        # Umumnya: 1 (HIGH) berarti gelap, 0 (LOW) berarti terang (tergantung modul)
        status_cahaya = GPIO.input(LDR_Pin)
        
        if status_cahaya == GPIO.HIGH:
            print("Kondisi: GELAP (Lampu Seharusnya Nyala)")
        else:
            print("Kondisi: TERANG (Lampu Seharusnya Mati)")
            
        # Delay agar pembacaan stabil
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    GPIO.cleanup()