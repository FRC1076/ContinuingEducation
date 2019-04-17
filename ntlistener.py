#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# This shows how to use a listener to listen for changes in NetworkTables
# values. This will print out any changes detected on the SmartDashboard
# table.
#

import sys
import time
from networktables import NetworkTables
from networktables.util import ntproperty
# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

NetworkTables.initialize(server=ip)


def valueChanged(table, key, value, isNew):
    if key == "senttime":
        print("roundtrip: '%f' valueChanged: key: '%s'; value: %s; isNew: %s" % ((time.time() - value), key, value, isNew))


def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)

class someClient(object):
    dsTime = ntproperty("/SmartDashboard/dsTime", 0.0)
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

sd = NetworkTables.getTable("SmartDashboard")
sd.addEntryListener(valueChanged)
c = someClient()
while True:
    time.sleep(1)
    c.dsTime = time.time()
