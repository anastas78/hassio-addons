# Add-ons for Home Assistant

## About

This repository collects all of my add-ons for Home Assistant and was intended for easier installation.

## Disclaimer / Potential Issues

This all started with the idea of  [jgoakley] (https://github.com/jgoakley/)  to make an add-on for WeeWx personal weather station to integrate with Hass.Io. Exactly as he wrote, I also have no idea what I'm doing. These Addons are aimed to learn in my spare time and work "as I think it is OK".

## Installation

Follow [the official instructions](https://home-assistant.io/hassio/installing_third_party_addons/) on the Home Assistant website and use the following URL:
```txt
https://github.com/anastas78/hassio-addons
```

## Add-ons provided by this repository


## WeeWX
Uses the WeeWX program and MQTT to receive data from a weather station. 
It is an exact copy of latest version of weewx install on ubuntu. It should work with any weather station supported by weewx. Additionally I have added the Interceptor driver as many stations can be monitored through it.
For correct driver to use, please use the [documentation] (https://weewx.com/docs/) of weewx.

In the addon configuration are left only the most needed parts of weewx.conf in order to start the program. The configuration file weewx.conf will be stored in the config/weewx directory of HA (as well as the skins and html directories) for easier administration.

#### Example configuration:
```
{
  "driver": "weewx.drivers.acurite",
  "latitude": 12.345678,
  "longitude": -12.345678,
  "altitude": 123,
  "altitudeUnit": "foot",
  "location": "Location String for WeeWX",
  "units": "us",
  "database": "mysql"
}
```
I am using a sligthly changed weewx-mqtt plugin for weewx (forked from matthewwall/weewx-mqtt) in order to make all the sensors of the weather station use the Home Assistant auto-discover feature. If NO MQTT credentials are given in the configuration, the addon will use core-mosquitto with automatic user. All data will be published under weather/ topic.

I have included also a MySql integration to store all the data in a table. If you prefer you can still use sqlite (configuration option).


