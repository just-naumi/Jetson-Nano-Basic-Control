import Jetson.GPIO as GPIO
import time

# Menggunakan penomoran fisik (BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin 15 terhubung ke pin OUT pada sensor Infrared
IR_Pin = 15

# Atur pin sebagai INPUT
GPIO.setup(IR_Pin, GPIO.IN)

print("Sistem Deteksi Objek Infrared Aktif...")
print("Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        # Membaca status logika dari sensor
        # Umumnya: 0 (LOW) berarti ada objek, 1 (HIGH) berarti tidak ada
        status_sensor = GPIO.input(IR_Pin)
        
        if status_sensor == GPIO.LOW:
            print("Objek Terdeteksi! (Status: LOW)")
        else:
            print("Area Bersih (Status: HIGH)")
            
        # Delay singkat agar terminal tidak terlalu cepat
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    GPIO.cleanup()