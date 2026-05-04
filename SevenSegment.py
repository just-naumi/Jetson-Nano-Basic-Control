import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Definisi pin fisik yang terhubung ke segmen a, b, c, d, e, f, g, dp
pins = [7, 11, 13, 15, 19, 21, 23, 29]

# Inisialisasi semua pin sebagai OUTPUT dan set HIGH (mati untuk Common Anode)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Matriks pola angka 0-7 (0 = Nyala, 1 = Mati untuk Common Anode)
matrix_angka = [
    [0, 0, 0, 0, 0, 0, 1, 1], # Angka 0
    [1, 0, 0, 1, 1, 1, 1, 1], # Angka 1
    [0, 0, 1, 0, 0, 1, 0, 1], # Angka 2
    [0, 0, 0, 0, 1, 1, 0, 1], # Angka 3
    [1, 0, 0, 1, 1, 0, 0, 1], # Angka 4
    [0, 1, 0, 0, 1, 0, 0, 1], # Angka 5
    [0, 1, 0, 0, 0, 0, 0, 1], # Angka 6
    [0, 0, 0, 1, 1, 1, 1, 1]  # Angka 7
]

def set_angka(indeks):
    pola = matrix_angka[indeks]
    for i in range(8):
        GPIO.output(pins[i], pola[i])

print("Mulai Loop Angka 0-7. Tekan Ctrl+C untuk stop.")

try:
    while True:
        for i in range(8):
            print(f"Menampilkan Angka: {i}")
            set_angka(i)
            time.sleep(1.5)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    GPIO.cleanup()