#!/usr/bin/env python3

from time import sleep

from Adafruit_BBIO.GPIO import GPIO

GPIO.setup("P8_12", GPIO.IN)


def main() -> None:
    while True:
        print(GPIO.input("P8_12"))
        sleep(0.1)


if __name__ == "__main__":
    main()
