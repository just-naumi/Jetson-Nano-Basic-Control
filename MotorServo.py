import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin 33 mendukung hardware PWM
SERVO_PIN = 33
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Inisialisasi PWM dengan frekuensi 50Hz (standar servo)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def map_range(x, in_min, in_max, out_min, out_max):
    """Memetakan derajat (0-180) ke Duty Cycle (2-12)"""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(sudut):
    # Batasi input derajat
    if sudut < 0: sudut = 0
    if sudut > 180: sudut = 180
    
    # Konversi sudut ke duty cycle
    duty = map_range(sudut, 0, 180, 2, 12)
    pwm.ChangeDutyCycle(duty)
    
    # Beri waktu motor bergerak
    time.sleep(0.3)
    # Set duty ke 0 agar motor tidak bergetar (jitter)
    pwm.ChangeDutyCycle(0)

print("Menggerakkan Servo. Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        print("Sudut 0 derajat")
        servo_write(0)
        time.sleep(1)
        
        print("Sudut 90 derajat")
        servo_write(90)
        time.sleep(1)
        
        print("Sudut 180 derajat")
        servo_write(180)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    pwm.stop()
    GPIO.cleanup()