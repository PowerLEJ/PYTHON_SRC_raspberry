# SW : active high로 설계 -> 24,26
# LED : active high로 설계 -> 10,36

import RPi.GPIO as GPIO
import time

led_pin = [10, 36]
sw_pin = [24, 26]

# Define the LED states
ON = GPIO.HIGH
OFF = GPIO.LOW

GPIO.setmode(GPIO.BOARD) # 보드의 물리적인 핀 설정
# GPIO.setmode(GPIO.BCM) # BCM 칩의 핀 설정

for pin in sw_pin:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for pin in led_pin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, OFF)

sw_pre = [GPIO.LOW, GPIO.LOW]
sw_cur = [GPIO.LOW, GPIO.LOW]

status_led = [OFF, OFF]

try:
    while True:
        for i in range(len(led_pin)):
            sw_cur[i] = GPIO.input(sw_pin[i])

            if GPIO.LOW == sw_pre[i] and GPIO.HIGH == sw_cur[i]:
                if status_led[i] == ON:
                    GPIO.output(led_pin[i], OFF)
                    status_led[i] = OFF
                else:
                    GPIO.output(led_pin[i], ON)
                    status_led[i] = ON

            sw_pre[i] = sw_cur[i]

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    # Clean up GPIO pins when the program exits
    GPIO.cleanup()