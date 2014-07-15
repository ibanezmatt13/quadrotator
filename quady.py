import math
import time
import socket

base_pos = (53.5287953, -2.7169288)
callsign = "$$$$NORB2"

def get_bearing(pointA, pointB):

    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7322))
handle = sock.makefile()

dl_line = handle.readline().strip()

while True:
    dl_line = handle.readline().strip()
    data = dl_line.split(",")
    payload_pos = (float(data[3]), float(data[4]))
    bearing = round(get_bearing(payload_pos, base_pos), 2)
    print bearing
    
    



