# Turbine Farm
## What Is It?
Turbine Farm is a server for toy wind turbines, equiped with sensors and a Raspberry Pi, to connect to and allows the turbines sensor data to be accessed from the internet.

## Tell Me More!
This is a redis-based implementation of Turbine Farm. The ideal situation for this flavor of Turbine Farm is primarily for educational purposes. Normally, you'd use a websocket implementation for faster speeds and when you are writing directly to a time series database. Because I built Turbine Farm for teaching, this was the implementation that worked best for me. Running the redis-based implementation of Turbine Farm also takes the data load off of the turbine's Raspberry Pi (non-gigabit network) and puts it onto your express application and redis service. You may also want to consider adding security if you're using this for anything other than teaching or self-learning.

## How Does It Work?
Turbine Farm was built with the following hardware in mind:
  * Thames & Kosmos V3.0 Wind Power Science Kit
  * Raspberry Pi 3 Model B
  * Yoctopuce Yocto-Volt
  * Yoctopuce Yocto-Thermocouple

# Getting Started
## Predix/Cloud Foundry
To run in predix, you must first create a redis instance, and update your `manifest.yml` to reflect your new redis instance.
```
> git clone https://github.com/jtviolet/turbine-farm.git
> cf push
```

## Running Locally
To run locally, you must first have redis installed and running on your machine. This also assumes you left redis running at the default port.
```
> git clone https://github.com/jtviolet/turbine-farm.git
> cd turbine-farm
> npm start
```

## Usage
See API.md folder for examples.
URI's:
 * `/api/turbines/:turbine_id/sensors/:sensor_id`
 * `/api/turbines/:turbine_id/heartbeat`

## Contributing
If you feel you can improve this application in any way, I'm happy to accept pull requests for the good of the service. I'm pretty new to the development world, and there is always room for improvement. Feel free to submit pull requests, bugs, features, etc.

## License
MIT
