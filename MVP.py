
import json
import requests
import time
import urllib2





def getTemp(turbine):
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/temperature'
    ##grab value and assign it to temperature
    temperature = urllib2.urlopen(url).read()
    myArray = temperature.split(':')
    myValue = myArray[3].split('}')
    return float(myValue[0])

def getVoltage(turbine):
    str(turbine)
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/voltage'
    ##grab value and assign it to voltage
    voltage = urllib2.urlopen(url).read()
    myArray = voltage.split(':')
    myValue = myArray[3].split('}')
    return float(myValue[0])

def getHeartBeat(turbine):
    url = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/heartbeat'
    heartbeat = urllib2.urlopen(url).read()
    myArray = heartbeat.split(':')
    return myArray[1]

def getTimeStamp(turbine):
    return 1

resp = requests.get('https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature')
while (1):
    #print voltage of each turbine
    for i in [1, 2, 3]:
        print('turbine {0}: Voltage->{1} -- Temperature->{2} -- Heartbeat->{3}'.format(i, getVoltage(i), getTemp(i), getHeartBeat(i)))
    ## wait 2 seconds before printing again
    time.sleep(2)
    resp = requests.get('https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api')

print('Thanks for playing')


