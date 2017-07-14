
import json
import requests
import time
import urllib2





def getTemp(turbine):
    str(turbine)
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + turbine + '/sensors/temperature'
    ##grab value and assign it to temperature
    temperature = urrlib2.urlopen(url).read()
    return temperature

def getVoltage(turbine):
    str(turbine)
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + turbine + '/sensors/voltage'
    ##grab value and assign it to voltage
    voltage = urrlib2.urlopen(url).read()
    return voltage

resp = requests.get('https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api')
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


