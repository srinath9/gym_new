var http = require('http');

var server = http.createServer();

function handler('req','res'){
	res.write = "hello world" ;
}
server.listen(8080);
