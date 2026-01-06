@echo off
echo Flashing ESP32 with file: %1

call "C:\Users\Public\Documents\Software\esp\esp-idf\export.bat"

python -m esptool -b 900000 write_flash 0x30000 "%~1"