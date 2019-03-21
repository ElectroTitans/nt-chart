import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)
NetworkTables.startServer("test.ini", "127.0.0.1", 4056)

def valueChanged(table, key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))


def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)


NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

sd = NetworkTables.getTable("SmartDashboard")
sd.addEntryListener(valueChanged)
count = 0
while True:
    
    sd.putNumber("test1", count)
    sd.putNumber("test2", count / 2)
    count += 1
    time.sleep(0.01)