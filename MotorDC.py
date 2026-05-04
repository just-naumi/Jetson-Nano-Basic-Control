import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Deklarasi Pin
ENA, IN1, IN2 = 33, 11, 13

# Setup Output
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Inisialisasi PWM pada pin ENA dengan frekuensi 1000Hz
pwm_speed = GPIO.PWM(ENA, 1000)
pwm_speed.start(0)

def motor_maju(kecepatan):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm_speed.ChangeDutyCycle(kecepatan)
    print(f"Motor Maju Speed: {kecepatan}%")

def motor_mundur(kecepatan):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_speed.ChangeDutyCycle(kecepatan)
    print(f"Motor Mundur Speed: {kecepatan}%")

def motor_berhenti():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm_speed.ChangeDutyCycle(0)
    print("Motor Berhenti")

print("Menguji Motor DC. Tekan Ctrl+C untuk stop.")

try:
    while True:
        motor_maju(40)  # Maju Pelan
        time.sleep(2)
        motor_maju(90)  # Maju Cepat
        time.sleep(2)
        motor_berhenti()
        time.sleep(1)
        motor_mundur(60) # Mundur
        time.sleep(2)
        motor_berhenti()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Berhenti.")
    pwm_speed.stop()
    GPIO.cleanup()