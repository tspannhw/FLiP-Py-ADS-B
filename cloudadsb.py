from datetime import datetime, timezone
import time
import pulsar
import logging
import sys
import subprocess
import os
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import time
import psutil
import uuid
import requests
from time import sleep
from math import isnan
from subprocess import PIPE, Popen
import socket
from pulsar import Client, AuthenticationOauth2
import argparse
import os.path
import re
import sys
import os

### Schema Object
# https://pulsar.apache.org/docs/en/client-libraries-python/

# IP Address
def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
# Random Word
def randomword(length):
 return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) for i in range(length))

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

#parse arguments
parse = argparse.ArgumentParser(prog='cloudadsb.py')
parse.add_argument('-su', '--service-url', dest='service_url', type=str, required=True,
                   help='The pulsar service you want to connect to')
parse.add_argument('-t', '--topic', dest='topic', type=str, required=True,
                   help='The topic you want to produce to')
parse.add_argument('--auth-params', dest='auth_params', type=str, default="",
                   help='The auth params which you need to configure the client')
args = parse.parse_args()

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET
# Timer
packet_size=3000

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ipaddress = IP_address()

print(args.service_url)
print(args.topic)
print(args.auth_params)

if (len(args.auth_params) == 0 ):
   client = pulsar.Client(args.service_url)
else:
   client = pulsar.Client(args.service_url, authentication=AuthenticationOauth2(args.auth_params))

producer = client.create_producer(topic=args.topic ,properties={"producer-name": "adsb-rest","producer-id": "adsb-py" })

try:
    while True:
        # Create unique id
        uniqueid = 'thrml_{0}_{1}'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())

        url_data = "http://localhost:8080/data/aircraft.json?_=" + str(uuid.uuid4())
        response = json.dumps(requests.get(url_data).json())

        producer.send(response.encode('utf-8'),partition_key=uniqueid)
        print("Sent aircraft data: " + str(len(str(response))))
        sleep(1)

except KeyboardInterrupt:
    pass

client.close()
