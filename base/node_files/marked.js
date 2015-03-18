//var data = require("./data");
//
//var express = require("express");
//var app = express.createServer();
//app.set("view engine", "ejs");
//app.set("views", __dirname + "/views");
//app.set("view options", { layout: false });
//
//app.get("/", function (request, response) {
//    response.render("index");
//});
//
//app.get("/user/:id", function (request, response) {
//    var id = request.params.id;
//    console.log(id);
//    response.json(data[id]);
//});
//
//console.log("Web Server listening ......");
//app.listen(3000);
//
//
var http = require('http');
var querystring = require('querystring');
var util = require('util');
var marked = require('marked');
var renderer = new marked.Renderer();
//var hljs = require('highlight.js');

//renderer.code = function(code, language){
//  return '<pre><code class="hljs ' + language + '">' +
//    hljs.highlight(language, code).value +
//    '</code></pre>';
//};
marked.setOptions({
  renderer: new marked.Renderer(),
  gfm: true,
  //tables: true,
  //breaks: false,
  //pedantic: false,
  sanitize: false,
  //smartLists: true,
  //smartypants: false,
    //langPrefix:'hljs ',
  //  highlight: function (code, lang, callback) {
  //  require('pygmentize-bundled')({ lang: lang, format: 'html' }, code, function (err, result) {
  //    callback(err, result.toString());
  //  });
  //}
    highlight: function (code) {
    return require('highlight.js').highlightAuto(code).value;
  }
});

http.createServer(function(req, res){
    req.setEncoding('utf-8');
    //console.log(req);
    //console.log(res);
    var post = '';     //定义了一个post变量，用于暂存请求体的信息

    req.on('data', function(chunk){    //通过req的data事件监听函数，每当接受到请求体的数据，就累加到post变量中
        post += chunk;
    });

    req.on('end', function(){    //在end事件触发后，通过querystring.parse将post解析为真正的POST请求格式，然后向客户端返回。
        //post = querystring.parse(post);
        post = marked(post);
        console.log(post);
        console.log(typeof(post));
        //var md_res = JSON.parse(post);
        console.log('test');
        res.end(util.inspect(post));
    });
}).listen(17900);

//
//var querystring = require('querystring');
//var http = require('http');
//
//var data = querystring.stringify({
//      username: 'x',
//      password: 'y'
//    });
//
//var options = {
//    host: '127.0.0.1',
//    port: 17900,
//    path: '/md',
//    method: 'POST',
//    headers: {
//        'Content-Type': 'application/x-www-form-urlencoded',
//        'Content-Length': Buffer.byteLength(data)
//    }
//};
//
//var req = http.request(options, function(res) {
//    res.setEncoding('utf8');
//    res.on('data', function (chunk) {
//        console.log("body: " + chunk);
//    });
//});
//
//req.write(data);
//req.end();