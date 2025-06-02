import RPi.GPIO as GPIO
import time

# GPIO Pin Setup
sensor_A = 18  # Sensor 1 input pin
sensor_B = 23  # Sensor 2 input pin
buzzer = 24    # Output for buzzer

# Speed Threshold in m/s (e.g., 30 km/h = 8.33 m/s)
speed_limit = 8.33
distance_meters = 1.0  # Distance between sensors

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_A, GPIO.IN)
GPIO.setup(sensor_B, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

try:
    while True:
        print("Waiting for vehicle...")

        while GPIO.input(sensor_A) == 0:
            pass
        start_time = time.time()
        print("Sensor A triggered")

        while GPIO.input(sensor_B) == 0:
            pass
        end_time = time.time()
        print("Sensor B triggered")

        time_taken = end_time - start_time
        speed = distance_meters / time_taken
        print(f"Vehicle speed: {speed:.2f} m/s")

        if speed > speed_limit:
            print("Over-speeding detected!")
            GPIO.output(buzzer, True)
            time.sleep(1)
            GPIO.output(buzzer, False)
        else:
            print("Speed is within limit.")

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped")
    GPIO.cleanup()
