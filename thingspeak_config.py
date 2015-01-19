__author__ = 'Leenix'

# Mapping between data id keys and Thingspeak fields
KEY_MAP = {
    "air_temp": "field1",
    "surface_temp": "field2",
    "humidity": "field3",
    "illuminance": "field4",
    "noise_level": "field5",
    "motion": "field6"
}

# Mapping between unit ID and Thingspeak channel
CHANNEL_MAP = {
    "lurker1": "13IIKMBZ68C6QE9E",
    "lurker2": "JLLN86V2D0X1ZMDU"
}

# Thingspeak server address (change if using a custom server)
# default: "api.thingspeak.com:80"
SERVER_ADDRESS = "api.thingspeak.com:80"