"""Constants used in the Mikrotik components."""
from typing import Final

DOMAIN: Final = "mikrotik2"
DEFAULT_NAME: Final = "Mikrotik2"
DEFAULT_API_PORT: Final = 8728
DEFAULT_DETECTION_TIME: Final = 300

ATTR_MANUFACTURER: Final = "Mikrotik2"
ATTR_SERIAL_NUMBER: Final = "serial-number"
ATTR_FIRMWARE: Final = "current-firmware"
ATTR_MODEL: Final = "model"

CONF_ARP_PING: Final = "arp_ping"
CONF_FORCE_DHCP: Final = "force_dhcp"
CONF_DETECTION_TIME: Final = "detection_time"


NAME: Final = "name"
INFO: Final = "info"
IDENTITY: Final = "identity"
ARP: Final = "arp"

CAPSMAN: Final = "capsman"
DHCP: Final = "dhcp"
WIRELESS: Final = "wireless"
WIFIWAVE2: Final = "wifiwave2"
WIFI: Final = "wifi"
IS_WIRELESS: Final = "is_wireless"
IS_CAPSMAN: Final = "is_capsman"
IS_WIFIWAVE2: Final = "is_wifiwave2"
IS_WIFI: Final = "is_wifi"


MIKROTIK_SERVICES: Final = {
    ARP: "/ip/arp/print",
    CAPSMAN: "/caps-man/registration-table/print",
    DHCP: "/ip/dhcp-server/lease/print",
    IDENTITY: "/system/identity/print",
    INFO: "/system/routerboard/print",
    WIRELESS: "/interface/wireless/registration-table/print",
    WIFIWAVE2: "/interface/wifiwave2/registration-table/print",
    WIFI: "/interface/wifi/registration-table/print",
    IS_WIRELESS: "/interface/wireless/print",
    IS_CAPSMAN: "/caps-man/interface/print",
    IS_WIFIWAVE2: "/interface/wifiwave2/print",
    IS_WIFI: "/interface/wifi/print",
}


ATTR_DEVICE_TRACKER: Final = [
    "comment",
    "ssid",
    "interface",
    "signal-strength",
    "signal-to-noise",
    "rx-rate",
    "tx-rate",
    "uptime",
]
