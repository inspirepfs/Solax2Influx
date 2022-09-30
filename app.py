#!/usr/bin/env python
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import json
import requests
import time
import os
import sys


# Environment Variables
# SolaxCloud Env.
solax_token = os.getenv('SOLAX_TOKEN')
solax_sn = os.getenv('SOLAX_SN')
# Influx Env.
token = os.getenv('INFLUX_TOKEN')
org = os.getenv('INFLUX_ORG')
bucket = os.getenv('INFLUX_BUCKET')
influx_url = os.getenv('INFLUX_URL')


#print("Environment Settings")
#print("Solax Token: ", solax_token, " Solax Serial Number: ", solax_sn)
#print("Influx Token: ", token, " Influx Org.: ", org, " Influx Bucket: ", bucket, " Influx URL and Port: ", influx_url)
sys.stdout.write("Environment Settings\n")
sys.stdout.write("Solax Token: " + solax_token + " Solax Serial Number: " + solax_sn + "\n")
sys.stdout.write("Influx Token: " + token + " Influx Org.: " + org + " Influx Bucket: " + bucket + " Influx URL and Port: " + influx_url)

while True:
# SolaxCloud - URL with Token and Serial Number (API end point)
# Collect SolaxCloud Data
    url = "https://www.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=" + solax_token + "&sn=" + solax_sn

    response_API = requests.get(url)

    data = response_API.text
    parse_json = json.loads(data)
    dateTimeObj = datetime.now()
    dateTimeObjStr = str(dateTimeObj)[:19]
    power_ac = parse_json['result']['acpower']
    power_dc1 = parse_json['result']['powerdc1']
    power_dc2 = parse_json['result']['powerdc2']
# Print SolaxCloud Data
    #print("Time:", dateTimeObj, "\nAC Power:", power_ac, "\nDC Power 1:", power_dc1, "\nDC Power 2:", power_dc2)
    sys.stdout.write("Time:" + dateTimeObjStr + "\n")
    sys.stdout.write("AC Power:" + str(power_ac) + "\n")
    sys.stdout.write("DC Power 1:" + str(power_dc1) + "\n")
    sys.stdout.write("DC Power 2:" + str(power_dc2) + "\n")
# End SolaxCloud

# Influx DB Clean and set data points
    client = InfluxDBClient(url=influx_url,token=token,org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()

    _point1 = Point("Solax_Measurment").tag("location", "Home").field("PowerAC", int(power_ac))
    _point2 = Point("Solax_Measurment").tag("location", "Home").field("PowerDC1", int(power_dc1))
    _point3 = Point("Solax_Measurment").tag("location", "Home").field("PowerDC2", int(power_dc2))

# Send the Data to Influx
    write_api.write(bucket=bucket, record=[_point1, _point2, _point3])

# Influx Close the connection
    client.close()

    time.sleep(10)
