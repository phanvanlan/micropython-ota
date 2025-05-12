from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin
from neopixel import NeoPixel
from time import sleep

firmware_url = "https://github.com/phanvanlan/micropython-ota/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "boot.py")
ota_updater.download_and_install_update_if_available()

pin = Pin(8, Pin.OUT)  
np = NeoPixel(pin, 1)  
np[0] = (0, 0, 25)  
np.write()            