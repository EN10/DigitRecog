var express = require("express");
var app = express();
var fs = require('fs');
var exec = require('child_process').exec;

app.get("/", function(req, res) {
    fs.writeFile('JSON.txt', req.query.q, function(err){
        console.log(err);
    });

var cmd = 'python predictDigit.py';
    exec(cmd, function(error, stdout, stderr) {
        res.end(stdout);
        console.log(stdout);
        console.log(stderr);
    });

});

app.listen(process.env.PORT, function() {
    console.log("server runnning");
});