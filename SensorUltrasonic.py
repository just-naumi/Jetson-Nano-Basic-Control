import Jetson.GPIO as GPIO
import time

# Menggunakan penomoran fisik (BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Definisi Pin
TRIG = 11
ECHO = 13

# Setup Pin
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_jarak():
    # Pastikan Trigger LOW
    GPIO.output(TRIG, False)
    time.sleep(0.01)

    # Kirim pulsa 10 microsecond ke Trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Rekam waktu saat Echo mulai HIGH
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    
    # Rekam waktu saat Echo kembali LOW
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Hitung selisih waktu
    durasi = end_time - start_time
    
    # Rumus: (Durasi * Kecepatan Suara 34300 cm/s) / 2 (bolak-balik)
    jarak = (durasi * 34300) / 2
    return jarak

print("Pengukuran Jarak Ultrasonic Aktif...")
print("Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        dist = get_jarak()
        print(f"Jarak Objek: {dist:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    GPIO.cleanup()