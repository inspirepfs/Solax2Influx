# Solax Cloud Data to InfluxDB 2


This container connects to Solax cloud API to collect inverter data and sends the data to InfluxDB2  either hosted locally or cloud hosted.

The Solax token and serial number can be obtained  from the Solax portal and documentation. 
The container support influxDB2 and above.


SOLAX_TOKEN=`YOUR SOLAX CLOUD TOKEN`
SOLAX_SN=`YOUR SOLAX INVERTER SERIAL NUMBER`
INFLUX_TOKEN=`YOUR INFLUX TOKEN`
INFLUX_ORG=`YOUR INFLUX ORGANISATION`
INFLUX_BUCKET=`YOUR INFLUX BUCKET`
INFLUX_URL=`INFLUX URL (IF LOCAL ENSURE PORT IS INCLUDED)`

**Expected output from the container.**

Environment Settings
Solax Token: `YOUR SOLAX CLOUD TOKEN`Solax Serial Number: `YOUR SOLAX INVERTER SERIAL NUMBER`
Influx Token: `YOUR INFLUX TOKEN` Influx Org.: `YOUR INFLUX ORGANISATION` Bucket: `YOUR INFLUX BUCKET` Influx URL and Port: `INFLUX URL (IF LOCAL ENSURE PORT IS INCLUDED)`
Time:2022-09-30 15:24:42
AC Power:23.0
DC Power 1:35.0
DC Power 2:18.0

All Power data is in Watts. The script will loop every 10 seconds this in line with the API limitation from Solax Cloud. 

**docker pull pfsykes/solax2influx**
