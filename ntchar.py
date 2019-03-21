import sys
import time
from networktables import NetworkTables
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Create realtime MatPlotLib charts based on NetworkTable data')
parser.add_argument('--team', dest='team',
                    help='Team number to connect to robot NT')
parser.add_argument('--ip', dest='server_ip',
                    help='Server IP')
parser.add_argument('--port', dest='server_port',
                    help='Server Port')
parser.add_argument('-k', dest='keys', action='append', 
                    help='Keys to monitor')
args = parser.parse_args()
print(args)



# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)
keys = args.keys
ip = args.server_ip
port = args.server_port
print(port)
NetworkTables.initialize(ip)
NetworkTables.startClient((ip, port));

sd = NetworkTables.getTable("SmartDashboard")
plt.ion();
tick = 0
states = []

while True:
    values = []
    for key in keys:
        val = sd.getValue(key, "n/a")
        print(val)
        if val is not "n/a":
            values.append(val)
            
    if len(values) > 0:
        states.append(values)

    plt.cla()
    print(keys)
    plt.plot(states)
    plt.legend(keys, loc='upper left', shadow=True)
    plt.pause(0.0001)
    plt.show()
    tick += 1
    time.sleep(0.01)
