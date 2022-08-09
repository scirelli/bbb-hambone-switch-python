#!/usr/bin/env python3
from Adafruit_BBIO import GPIO  # pylint: disable=no-name-in-module

FRONT_LIMIT_SWITCH_PIN = "P8_12"
REAR_LIMIT_SWITCH_PIN = "P8_10"
DOOR_SWITCH_PIN = "P8_8"

GPIO.setup(
    FRONT_LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP
)  # Front limit switch
GPIO.setup(
    REAR_LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP
)  # Rear limit switch
GPIO.setup(DOOR_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Door switch


def main() -> None:
    while True:
        if GPIO.input(FRONT_LIMIT_SWITCH_PIN):
            print("Front limit switch released")
        else:
            print("Front limit switch pressed")

        if GPIO.input(REAR_LIMIT_SWITCH_PIN):
            print("Rear limit switch released")
        else:
            print("Rear limit switch pressed")

        if GPIO.input(DOOR_SWITCH_PIN):
            print("Door switch released")
        else:
            print("Door switch pressed")


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        print("Handing kb interrupt")
        GPIO.cleanup()
        raise
