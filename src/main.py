#!/usr/bin/env python3
from Adafruit_BBIO import GPIO  # pylint: disable=no-name-in-module

GPIO.setup("P8_12", GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main() -> None:
    while True:
        if GPIO.input("P8_12"):
            print("button released")
        else:
            print("button pressed")


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        GPIO.cleanup()
        raise
