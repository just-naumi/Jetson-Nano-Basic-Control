import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Definisi Pin (Sesuaikan dengan koneksi fisikmu)
# Baris (Rows) terhubung ke pin output
L1, L2, L3, L4 = 7, 11, 13, 15
# Kolom (Columns) terhubung ke pin input
C1, C2, C3, C4 = 19, 21, 23, 29

rows = [L1, L2, L3, L4]
cols = [C1, C2, C3, C4]

# Setup Pin
for r in rows:
    GPIO.setup(r, GPIO.OUT)
    GPIO.output(r, GPIO.HIGH) # Set default HIGH

for c in cols:
    GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pakai Internal Pull-Up

# Matriks Karakter
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

def read_keypad():
    for i, row_pin in enumerate(rows):
        # Tarik baris ke LOW untuk memindai
        GPIO.output(row_pin, GPIO.LOW)
        
        for j, col_pin in enumerate(cols):
            if GPIO.input(col_pin) == GPIO.LOW:
                # Tunggu sampai tombol dilepas (anti-bounce)
                while GPIO.input(col_pin) == GPIO.LOW:
                    pass
                GPIO.output(row_pin, GPIO.HIGH)
                return keys[i][j]
        
        # Kembalikan ke HIGH sebelum pindah ke baris berikutnya
        GPIO.output(row_pin, GPIO.HIGH)
    return None

print("Keypad 4x4 Siap. Tekan tombol pada keypad...")
print("Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        key = read_keypad()
        if key:
            print(f"Tombol Ditekan: {key}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    GPIO.cleanup()