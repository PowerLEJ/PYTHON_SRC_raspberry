import RPi.GPIO as GPIO
import time

# 상수 정의
ON = True
OFF = False

LED0 = 10
LED1 = 36

SW0 = 24
SW1 = 26

# 전역변수 선언
status_led0 = OFF
status_led1 = OFF

# 버튼 인터럽트 처리 함수
def btn_interrupt(channel):
    global status_led0
    # 상태값 변경
    if status_led0 == ON:
        status_led0 = OFF
    else:
        status_led0 = ON

def btn_interrupt_2(channel):
    global status_led1
    # 상태값 변경
    if status_led1 == ON:
        status_led1 = OFF
    else:
        status_led1 = ON

# 메인 함수
def main():
    global status_led0, status_led1
    
    # 경고 비활성화
    GPIO.setwarnings(False)
    
    # GPIO 초기화
    GPIO.cleanup()  # 모든 GPIO 핀 상태 초기화
    GPIO.setmode(GPIO.BOARD)  # Physical pin 번호 사용

    # 핀 설정
    GPIO.setup(SW0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 스위치 A (Pull-down 설정)
    GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 스위치 B (Pull-down 설정)
    GPIO.setup(LED0, GPIO.OUT)  # LED 0
    GPIO.setup(LED1, GPIO.OUT)  # LED 1

    GPIO.output(LED0, GPIO.LOW)
    GPIO.output(LED1, GPIO.LOW)

    # 이전 이벤트 감지 제거
    GPIO.remove_event_detect(SW0)
    GPIO.remove_event_detect(SW1)

    # 인터럽트 설정
    try:
        GPIO.add_event_detect(SW0, GPIO.RISING, callback=btn_interrupt, bouncetime=300)  # 버튼 A
        GPIO.add_event_detect(SW1, GPIO.RISING, callback=btn_interrupt_2, bouncetime=300)  # 버튼 B
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        GPIO.cleanup()  # GPIO 핀 해제
        return
    
    try:
        while True:
            # 상태값에 따른 동작 구현
            if status_led0 == ON:
                GPIO.output(LED0, not GPIO.input(LED0))  # LED 토글
                time.sleep(0.3)  # 300ms 지연
            else:
                GPIO.output(LED0, GPIO.LOW)  # LED 끄기

            if status_led1 == ON:
                GPIO.output(LED1, not GPIO.input(LED1))  # LED 토글
                time.sleep(0.3)  # 300ms 지연
            else:
                GPIO.output(LED1, GPIO.LOW)  # LED 끄기

    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        GPIO.cleanup()  # GPIO 핀 해제

# 프로그램 실행
if __name__ == "__main__":
    main()
