from flask import Flask, request, jsonify
import numpy
import json

app = Flask(__name__)

class HeightsClass:

    def __init__(self):
        self.heights = numpy.zeros(15)

    def Setter(self, _heights: numpy.ndarray):
        if(numpy.size(_heights)==15 and numpy.min(_heights)>=0 and numpy.max(_heights)<=60):
            self.heights = _heights
            return 0
        else:
            return -1
    
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
        isOK = Heights.Setter(numpy.array(receivedData['Heights']))
        if(isOK == 0):
            return 'OK', 200
        else:
            return 'ERROR: wrong value or size', 400
    else:
        return 'ERROR: request is not JSON', 400

@app.route('/GetHeights', methods=['GET'])
def GetHeights():
    return {'Heights':Heights.Getter().tolist()}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555)
