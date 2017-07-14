
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

resp = requests.get('https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature')
while (resp.status_code == 200):
    #print voltage of each turbine
    for i in [1, 2, 3]:
        print('Voltage for turbine {0} is {1}.'.format(i, getVoltage(i)))
    #print temperature of each turbine
    for i in [1, 2, 3]:
        print('Temperature for turbine {0} is {1}.'.format(i, getTemp(i)))
    ## wait 2 seconds before printing again
    time.sleep(2)
    resp = requests.get('https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api')

print('Thanks for playing')


