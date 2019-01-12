from flask import Flask, render_template, request, redirect, Response
import random, json, serial, time, struct
app = Flask(__name__)

ser = serial.Serial()
#ser.port = "/dev/ttyUSB0"
ser.port = "/dev/ttyACM1"
#ser.port = "/dev/ttyS2"
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

#ser.open()

#ser.write(bytes(34))


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/receiver', methods = ['POST'])
def worker():
    # read json + reply
    data = request.get_data()
    #TODO: IMPORT SERIAL AND send json data out to arduino'
    #datalist = data.split(":")
    data2 = "".join(map(chr, data))
    datalist = data2.split(":")
    
    
    
    #if(len(datalist) > 1):
    #   dataSerial = struct.pack('bbbbbb',-128,int(datalist[1]),int(datalist[2]),int(datalist[3]),int(datalist[4]),-128)
    #   ser.write(dataSerial)
        
    return "g"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
