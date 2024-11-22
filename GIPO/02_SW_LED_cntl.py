# SW : active high로 설계 -> 24,26
# LED : active high로 설계 -> 10,36

import RPi.GPIO as GPIO

led_pin = [10, 36]
sw_pin = [24, 26]

GPIO.setmode(GPIO.BOARD) # 보드의 물리적인 핀 설정
# GPIO.setmode(GPIO.BCM) # BCM 칩의 핀 설정

for i in range(len(led_pin)):
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW) # 핀모드 설정
    GPIO.setup(sw_pin, GPIO.IN, GPIO.PUD_DOWN)

while True:
    for i in range(len(led_pin)):
        if GPIO.input(sw_pin[i]):
            GPIO.output(led_pin[i], GPIO.HIGH) # 핀값 출력
        else:
            GPIO.output(led_pin[i], GPIO.LOW)