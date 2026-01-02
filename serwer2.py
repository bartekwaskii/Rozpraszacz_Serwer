from flask import Flask, request, jsonify
import numpy
import json

app = Flask(__name__)

current_positions=numpy.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

class HeightsClass:

    def __init__(self):
        self.heights = numpy.zeros(15)

    def Setter(self, _heights):
        if(numpy.size(_heights)==15 and numpy.min(_heights)>=0 and numpy.max(_heights)<=60):
            self.heights = _heights
            print(self.heights)
    
    def Getter(self):
        return self.heights

Heights = HeightsClass()

@app.route('/')
def default():
    return "\nRaspberryPi nr 1. Stan połączenia: OK "

@app.route('/SetHeights', methods=['POST'])
def SetHeights():
    if request.is_json:
        receivedData = request.get_json()
        Heights.Setter(numpy.array(receivedData['Heights']))
        return 'OK', 200
    else:
        return 'ERROR', 400

@app.route('/GetHeights', methods=['GET'])
def GetHeights():
    return {'Heights':Heights.Getter().tolist()}, 200

@app.route('/isReady', methods=['GET'])
def IsReadyFunction():
    return "not ready yet"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555)
