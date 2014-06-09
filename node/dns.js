var dns = require('dns');

dns.lookup('google.com',function(err,ip){
console.log(ip);
});

