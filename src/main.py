#!/usr/bin/env python3
from json import dump
from sys import stderr, stdout
from time import perf_counter_ns

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


def eprint(*args, **kwargs) -> None:  # type: ignore
    print(*args, file=stderr, **kwargs)


def main(times: list[int]) -> None:  # pylint: disable=redefined-outer-name
    motorStop()
    startTime: int = perf_counter_ns()
    totalTime: int = 10 * 1000000000
    elaspsedTime: int = 0

    while True:
        elaspsedTime += perf_counter_ns() - startTime
        if elaspsedTime >= totalTime:
            break

        if GPIO.input(FRONT_LIMIT_SWITCH_PIN):
            pass
        else:
            eprint("Front limit switch pressed")
            motorBackward()
            times.append(perf_counter_ns())

        if GPIO.input(REAR_LIMIT_SWITCH_PIN):
            pass
        else:
            eprint("Rear limit switch pressed")
            motorForward()
            times.append(perf_counter_ns())

        if GPIO.input(DOOR_SWITCH_PIN):
            eprint("Door switch pressed")
        else:
            eprint("Door switch released")


def motorForward() -> None:
    GPIO.output(MOTOR_IN1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_IN2_PIN, GPIO.HIGH)


def motorBackward() -> None:
    GPIO.output(MOTOR_IN2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_IN1_PIN, GPIO.HIGH)


def motorStop() -> None:
    GPIO.output(MOTOR_IN2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_IN1_PIN, GPIO.LOW)


if __name__ == "__main__":
    times: list[int] = []
    try:
        main(times)
    except BaseException:
        eprint("Handing kb interrupt")
        raise
    finally:
        motorStop()
        GPIO.cleanup()
        dump(times, stdout, indent="\t")
