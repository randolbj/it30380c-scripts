var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");
const cpuData = os.cpus()
const numOfCpus = os.cpus().length 


//console.log(cpuData)
//console.log(numOfCpus)

var server = http.createServer(function(req, res){
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body)

        })
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html = `
        
        <!DOCTYPE html>
        <head>
        <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: </p>
            <p>Total Memory: ${os.totalmem()} in bytes </p>
            <p>Free Memory: ${os.freemem()} in bytes </p>
            <p>Number of CPUs: ${numOfCpus} </p>
    
        </body>
        </html>

        `
        
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"})
        res.end(`404 File Not Fount at ${req.url}`)
    }

});

server.listen(3000)
console.log("Server Listenting on port 3000");
