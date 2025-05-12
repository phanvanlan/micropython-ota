from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://github.com/phanvanlan/micropython-ota/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "boot.py")

ota_updater.download_and_install_update_if_available()


print("version 5");