var pathUtil = require('path'),
    log      = require(pathUtil.join(__dirname,'./logger.js')),
    cp       = require('child_process'),
    _        = require('underscore');

function RaspybotController(){
    var self      = this;
    this._cmd     = pathUtil.join(__dirname,"arduino.py");
    this._arduino = null;

    RaspybotController.prototype.shutdown = function(){
        var self = this;
        if(!_.isEmpty(self._arduino)){
            process.kill(self._arduino.pid);
        }
    };

    RaspybotController.prototype.listen = function() {
        var self = this;
        self._arduino = cp.spawn('python', [self._cmd]);
        self._arduino.stdin.setEncoding('utf-8');

        self._arduino.stdout.on('data', (data) => {
            log.info('raspy received stdout from arduino:'+data.toString());
            if(_.isEqual(data.toString(),'CONNECTED')){
                log.info("Successfully started arduino.py script.");
            }
        });

        self._arduino.stderr.on('data', (err) => {
            log.error('Received stderr from arduino:'+err);
        });

        self._arduino.on('close', (code) => {
            log.info('Arduino python process closed with code:'+code);
        });

        self._arduino.on('exit', (code) => {
            log.info('Arduino python process exited with code:'+code);
        });
    };

}//Raspy

module.exports = RaspybotController;