#!/usr/bin/env python3
from Adafruit_BBIO import GPIO  # pylint: disable=no-name-in-module

FRONT_LIMIT_SWITCH_PIN = "P8_12"
REAR_LIMIT_SWITCH_PIN = "P8_10"
DOOR_SWITCH_PIN = "P8_8"
MOTOR_IN1_PIN = "P8_7"  # Drive backward (toward BBB)
MOTOR_IN2_PIN = "P8_9"  # Drive forward (away from BBB)

GPIO.setup(FRONT_LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(REAR_LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOOR_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOOR_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(MOTOR_IN1_PIN, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MOTOR_IN2_PIN, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)


def main() -> None:
    while True:
        if GPIO.input(FRONT_LIMIT_SWITCH_PIN):
            print("Front limit switch released")
        else:
            print("Front limit switch pressed")
            driveBackward()

        if GPIO.input(REAR_LIMIT_SWITCH_PIN):
            print("Rear limit switch released")
        else:
            print("Rear limit switch pressed")
            driveForward()

        if GPIO.input(DOOR_SWITCH_PIN):
            print("Door switch released")
        else:
            print("Door switch pressed")


def driveForward() -> None:
    GPIO.output(MOTOR_IN1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_IN2_PIN, GPIO.HIGH)


def driveBackward() -> None:
    GPIO.output(MOTOR_IN2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_IN1_PIN, GPIO.HIGH)


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        print("Handing kb interrupt")
        GPIO.cleanup()
        raise
