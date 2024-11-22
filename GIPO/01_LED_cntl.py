import RPi.GPIO as GPIO
import time

led_pin = 10

GPIO.setmode(GPIO.BOARD) # 보드의 물리적인 핀 설정
# GPIO.setmode(GPIO.BCM) # BCM 칩의 핀 설정

GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW) # 핀모드 설정

while True:
    GPIO.output(led_pin, GPIO.HIGH) # 핀값 출력
    time.sleep(0.5) # 초
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.5)

