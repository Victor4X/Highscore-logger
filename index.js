var request = require("request");
var bodyParser = require("body-parser");
var mongoose = require("mongoose");

var express = require('express');
var app = express();
var expressWs = require('express-ws')(app);

//mongoose.connect(process.env.MONGODB_URI,{useNewUrlParser: true});
mongoose.connect("mongodb://public:public1@ds029454.mlab.com:29454/pygame-highscores",{useNewUrlParser: true});


var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  // we're connected!
});

var scoreSchema = new mongoose.Schema({
    Game: String,
    Score: Number,
    Opt1: String,
    Opt2: String,
    Opt3: String
  });

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
    console.log('get route', req.testing);
    res.send('hello (Database)');
    res.end();
});

app.ws('/db', function (ws, req) {
ws.on('message',function(msg){

    score = JSON.parse(msg)
    
    var Games = mongoose.model('Games',scoreSchema);
    
    Games.insertMany(score, function (err) {
        if (err) return handleError(err);
        // saved!
    });
    try {
        Games.find().lean().exec(function (err, scoreEntries) {
            if (err) return console.error(err);
            //console.log(dotEntries);
            ws.send(JSON.stringify(scoreEntries));
        })
      } catch (err) {
        console.error(err);
      }
});
//console.log('socket', req.testing);
});
   
app.listen(process.env.PORT || 5000);
