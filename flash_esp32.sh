#!/bin/bash

echo "Flashing ESP32 with file: $1"

. ~/esp/esp-idf/export.sh && esptool.py -b 900000 write_flash 0x30000 "$1"