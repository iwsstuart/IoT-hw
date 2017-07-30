# IoT_hw

### Outline of what each file does

#### devstatus.py
This is a small python module that defines several functions used to collect real-time data relating to a device (e.g. a Raspberry Pi), using the psutil python package. In this example we have reduced the code to simply read the CPU load (percent of CPU currently being utilized).

#### client.py
Another small module defining several functions used to get the status data obtained using `devstatus.py` and and upload that data to a server. (The server could, for example, be set up using a [Tornado](http://www.tornadoweb.org/en/stable/) file server and web sockets.)

#### mylogger.py
Defines a logging function to be used when collecting real-time data and sending it to the server.

#### plot.js
A d3 script meant to take the device status data that was sent to the server by `client.py` and turn it into a real-time visualization. In this case it would be a plot of current CPU load. The data was sent to the server in json format, therefore `JSON.parse` is used to parse the JSON string to a javascript object. 
