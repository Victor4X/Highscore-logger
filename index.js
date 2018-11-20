var request = require("request");
var bodyParser = require("body-parser");
var mongoose = require("mongoose");

var express = require('express');
var app = express();
var expressWs = require('express-ws')(app);

//mongoose.connect(process.env.MONGODB_URI,{useNewUrlParser: true});
mongoose.connect("mongodb://heroku-server:hejmeddig1@ds261570.mlab.com:61570/drawing-pygame",{useNewUrlParser: true});


var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  // we're connected!
});

var dotSchema = new mongoose.Schema({
    x: Number,
    y: Number,
    color: [Number]
  });

var Dots = mongoose.model('Dot',dotSchema);


app.use(function (req, res, next) {
//console.log('middleware');
req.testing = 'testing';
return next();
});

app.get('/', function(req, res, next){
console.log('get route', req.testing);
res.send('hello');
res.end();
});

app.ws('/', function(ws, req) {
ws.on('message', function(msg) {
    console.log(msg);
    ws.send(msg);
});
console.log('socket', req.testing);
});

app.get('/db', function (req, res) {
    
    try {
        Dots.find(function (err, dotEntries) {
            if (err) return console.error(err);
            res.send(dotEntries);
          })
      } catch (err) {
        console.error(err);
        res.send("Error " + err);
      }
});

app.ws('/db', function (ws, req) {
ws.on('message',function(msg){
    if (msg != "get"){

        /*
        console.log(msg);
        console.log(typeof(msg));
        console.log(JSON.parse(msg))
        console.log(typeof(JSON.parse(msg)))
        */

        dot = JSON.parse(msg)
        
        Dots.insertMany(dot, function (err) {
            if (err) return handleError(err);
            // saved!
          });
        
        
    }
    try {
        Dots.find().lean().exec(function (err, dotEntries) {
            if (err) return console.error(err);
            //console.log(dotEntries);
            ws.send(JSON.stringify(dotEntries));
        })
      } catch (err) {
        console.error(err);
      }
});
//console.log('socket', req.testing);
});
   
app.listen(process.env.PORT || 5000);


/* 
var app = express();
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.listen((process.env.PORT || 5000));

// Server index page
app.get("/", function (req, res) {
  res.send("Deployed!");
});
app.get('/db', function (req, res) {
    
    try {
        Dots.find(function (err, dotEntries) {
            if (err) return console.error(err);
            console.log(dotEntries);
            res.send(dotEntries);
          })
      } catch (err) {
        console.error(err);
        res.send("Error " + err);
      }
});

*/
