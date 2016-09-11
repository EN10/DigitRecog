var express = require("express");
var app = express();
var fs = require('fs');
var exec = require('child_process').exec;

app.get("/", function(req, res) {
var data = req.query.q.replace(/^data:image\/\w+;base64,/, '');
    fs.writeFile('digit.png', data, {encoding: 'base64'}, function(err){
        console.log(err);
    });

var cmd = 'python predictDigit.py';
    exec(cmd, function(error, stdout, stderr) {
        res.end(stdout);
        console.log(stdout);
    });
});

app.listen(process.env.PORT, function() {
    console.log("server runnning");
});