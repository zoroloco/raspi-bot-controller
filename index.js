var pathUtil = require('path'),
    _        = require('underscore'),
    log      = require(pathUtil.join(__dirname,'./logger.js')),
    RaspybotController = require(pathUtil.join(__dirname,'./raspybotController.js')),
    conf     = require(pathUtil.join(__dirname,'./conf.json')),
    http     = require('http');

log.init();

process.title = conf.title;
var controller  = new RaspybotController();

function shutdown(){
    contoller.shutdown();
    process.exit();
}

//define process handlers
process.on('SIGTERM', function() {
    log.info("Got kill signal. Exiting.");
    shutdown();
});

process.on('SIGINT', function() {
    log.warn("Caught interrupt signal(Ctrl-C)");
    shutdown();
});

process.on('exit', function(){
    log.info("server process exiting...");
});

process.on('uncaughtException', function (err) {
    log.error(err);
});

controller.listen();
