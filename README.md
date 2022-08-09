# BBB Hamebone Reading a switch
https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black

## Setup
Adafruit_BBIO is not installable on anything but an ARM system. To allow mypy and linting to work the `.venv/lib/python3.10/site-packages` Adafruit_BBIO packages have been tar'd and checked into this project.
For development not on the BBB you can comment out the Adafruit_BBBIO package in the Pipfile, do an normal install `make install-dev && make install-precommit` then extract the tar into the site-packages folder.
