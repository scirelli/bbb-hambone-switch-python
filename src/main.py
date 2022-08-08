#!/usr/bin/env python3
from Adafruit_BBIO import GPIO

GPIO.setup("P8_12", GPIO.IN)


def main() -> None:
    old_pin_state = 0
    while True:
        new_pin_state = GPIO.input("P8_12")
        if new_pin_state != old_pin_state:
            print("button pressed")
            old_pin_state = new_pin_state


if __name__ == "__main__":
    main()
