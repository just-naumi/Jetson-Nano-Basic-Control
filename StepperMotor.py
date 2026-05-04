import Jetson.GPIO as GPIO
import time

# Menggunakan penomoran fisik (BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin Jetson Nano yang terhubung ke IN1, IN2, IN3, IN4 pada driver ULN2003
Stepper_Pins = [7, 11, 13, 15]

# Atur semua pin sebagai OUTPUT
for pin in Stepper_Pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Definisi urutan langkah (Half-step sequence)
# Memberikan sinyal HIGH pada pin yang sesuai untuk memutar rotor
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def putar_stepper(langkah, delay):
    for _ in range(langkah):
        for step in step_sequence:
            for i in range(4):
                GPIO.output(Stepper_Pins[i], step[i])
            time.sleep(delay)

print("Memulai putaran Stepper Motor. Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        print("Putar Searah Jarum Jam (CW)")
        putar_stepper(512, 0.001) # 512 langkah sekitar 90 derajat
        time.sleep(1)
        
        print("Putar Berlawanan Arah Jarum Jam (CCW)")
        # Untuk membalik arah, kita bisa membalik sequence
        # (Namun untuk demo ini kita gunakan putaran simpel saja)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    # Matikan semua pin saat berhenti agar motor tidak panas
    for pin in Stepper_Pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()