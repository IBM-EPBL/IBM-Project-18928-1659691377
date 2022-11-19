import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

# IBM
organization = "“jztdcw”"
deviceType = "NodeMCU"
deviceId = " node-mcu-4321 "
authMethod = "use-token-auth"
authToken = "987654321"
# Gpio
def mycommandCallback(cmd):
    print("Command Received: %s" % cmd.data["command"])
    status = cmd.data["command"]
    if status == "lighton":
        print("LED is ON")
    elif status == "lightoff":
        print("LED is OFF")
    else:
        print("please send proper command")
try:
    deviceOptions = {
        "org": organization,
        "type": deviceType,
        "id": deviceId,
        "auth-method": authMethod,
        "auth-token": authToken,
    }
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()
# CONNECCT
deviceCli.connect()
while True:
    temp = random.randint(0, 100)
    hum = random.randint(0, 100)
    data = {"temp": temp, "hum": hum}
    def myOnPublishCallback():
        print(
            "Published Temperature = %s C" % temp,
            "Humidity = %s %%" % hum,
            "to IBM Watson",
        )
    success = deviceCli.publishEvent(
        "IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback
    )
    if not success:
        print("Not connected to IoTF")
    time.sleep(10)
    deviceCli.commandCallback = mycommandCallback
# Disconnect
deviceCli.disconnect()

// Sprint 3:  For Reference
import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device
#Provide your IBM Watson Device Credentials
organization = "jztdcw"
deviceType = "NodeMCU"
deviceId = " node-mcu-4321 "
authMethod = "use-token-auth"
authToken = "987654321"
def myCommandCallback(cmd): # function for Callback
    print("Command received: %s" % cmd.data)
    if cmd.data['command']=='motoron':
        print("Turn Motor ON")
    elif cmd.data['command']=='motoroff':
        print("Turn Motor OFF")
    elif cmd.data['command']=='lighton':
        print("Turn Light ON")
    elif cmd.data['command']=='lightoff':
        print("Turn Light OFF")
        
    if cmd.data['command']=='ACTIVATE IRRIGATION':
        print("TurnON")
    elif cmd.data['command']=='DEACTIVATE IRRIGATION':
        print("TurnOFF")
    elif cmd.data['command']=='HIGH TEMPERATURE':
        print("TurnON")
    elif cmd.data['command']=='LOW TEMPERATURE':
        print("TurnOFF")
        
    if cmd.data['command']=='BAD WEATHER':
        print("TurnON")
    elif cmd.data['command']=='GOOD WEATHER':
        print("TurnOFF")
    elif cmd.data['command']=='HUMIDITY HIGH':
        print("TurnON")
    elif cmd.data['command']=='HUMIDITY LOW':
        print("TurnOFF")
        
    if cmd.command == "setInterval":
        if 'interval' not in cmd.data:
        print("Error - command is missing required information: 'interval'")
    else:
        interval = cmd.data['interval']
    elif cmd.command == "print":
        if 'message' not in cmd.data:
            print("Error - command is missing required information: 'message'")
        else:
             output=cmd.data['message']
    print(output) 
try:
    deviceOptions = {"org": organization, "type":
    deviceType, "id": deviceId, "auth-method": authMethod,
    "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
#..............................................
except Exception as e:
    print("Caught exception connecting device: %s" %
    str(e))
    sys.exit()
    # Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
    deviceCli.connect()
while True:
    deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()

// Code For Temperature
from random import * 
from random import * 
while True: 
    temperature = randrange(0,100) 
    humidity = randrange(0,100) 
    if (temperature>=50): 
        print("Alarm") 
    else: 
        print("No Alarm")

