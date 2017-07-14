
import json
import requests
import time
import urrlib2





def getTemp(turbine):
    str(turbine)
    string url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + turbine + '/sensors/temperature'
    float temperature = urrlib2.urlopen(url).read()
    return voltage

def getVoltage(turbine):
    str(turbine)
    string url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + turbine + '/sensors/voltage'
    float voltage = urrlib2.urlopen(url).read()
    return voltage

resp = requests.get('https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api')
while resp.status_code = 200
    #print voltage of each turbine
    for i in [1, 2, 3]:
        print('Voltage for turbine {0} is {1}.'.format(i, getVoltage(i)))
    #print temperature of each turbine
    for i in [1, 2, 3]:
        print('Temperature for turbine {0} is {1}.'.format(i, getTemp(i)))
    ## wait 2 seconds before printing again
    time.sleep(2)


