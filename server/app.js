//require additional libraries needed for app
var express    = require('express');
var bodyParser = require('body-parser');
var config     = require('../lib/config.json');
var redis      = require('redis');


//initialize redisClient and get authorized with service in predix, or in local development environment
/*if(process.env.environment !== 'development'){
    var vcapServices     = JSON.parse(process.env.VCAP_SERVICES);
    var redisCredentials = vcapServices['redis-5'][0].credentials;
    var redisHost        = redisCredentials.host;
    var redisPassword    = redisCredentials.password;
    var redisPort        = redisCredentials.port;
    var redisClient      = redis.createClient({ host: redisHost, port: redisPort });

    redisClient.auth(redisPassword, function(err, reply){
        reply !== null ? console.log(reply) : console.log(err);
    });
}*/
    var redisPort   = 6379;
    var redisClient = redis.createClient({ host: process.platform === 'win32' ? '127.0.0.1' : '0.0.0.0' , port: redisPort });


//connect to redis instance
redisClient.on('connect', function(){
	console.log('The redis instance has been connected successfully on the following port: ' + redisPort);
});


//log any errors that the redis client may have
redisClient.on('error', function(err){
	console.log("Redis Error: " + err);
});


//initialize express app and use any additional libraries with express
var app    = express();
app.use(bodyParser.json());
var router = express.Router();


//functionality that you want to happen anytime the api is accessed.
router.use(function(req, res, next){
    next();
});


//post or get the current read on sensor requested for the turbine specified
router.route('/turbines/:turbine_id/sensors/:sensor_type')
    .get(function(req, res, next){
        redisClient.get(('turbines/' + req.params.turbine_id + '/sensors/' + req.params.sensor_type), function(err, reply){
            reply !== null ? res.status(200).json(JSON.parse(reply)) : res.status(404).json(err);
        });
    })
    .post(function(req, res, next){
        if(req.header("password") === ""){
            redisClient.set(('turbines/' + req.params.turbine_id + '/sensors/' + req.params.sensor_type), JSON.stringify(req.body), function(err, reply){
                reply !== null ? res.status(200).json(reply) : res.status(500).json(err);
            });
        } else{
            res.status(401).json({"Error": "Invalid password."});
        }

        redisClient.expire(('turbines/' + req.params.turbine_id + '/sensors/' + req.params.sensor_type), config.sensorExpirationTime, function(err, reply){});
    });


//post or get the heartbeat of the turbine specified
router.route('/turbines/:turbine_id/heartbeat')
    .get(function(req, res, next){
        redisClient.get(('turbines/' + req.params.turbine_id + '/heartbeat'), function(err, reply){
            reply !== null ? res.status(200).json({"status": reply}) : res.status(200).json({"status": "OFFLINE"});
        });
    })
    .post(function(req, res, next){
        if(req.header("password") === ""){
            redisClient.set(('turbines/' + req.params.turbine_id + '/heartbeat'), req.body.status, function(err, reply){
                reply !== null ? res.status(200).json(reply) : res.status(500).json(err);
            });
        } else{
            res.status(401).json({"Error": "Invalid password."});
        }

        redisClient.expire(('turbines/' + req.params.turbine_id + '/heartbeat'), config.heartbeatExpirationTime, function(err, reply){});
    });

    
//prefix all endpoints and start the server, either on the port decided by predix or port 5000 if local
app.use(config.endpointPrefix, router);
var server = app.listen(process.env.VCAP_APP_PORT, function () {
  console.log('Turbine Farm is now running on the following port: ' + server.address().port);
});
