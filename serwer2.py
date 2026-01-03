# serwer 2 dla, studzienek 16-30

from flask import Flask, request, jsonify
import numpy
import json

app = Flask(__name__)

class HeightsClass:

    def __init__(self):
        self.heights = numpy.zeros(15)
        self.currentPositions = numpy.zeros(15)

    def Setter(self, _heights: numpy.ndarray):
        if(numpy.size(_heights)==15 and numpy.min(_heights)>=0 and numpy.max(_heights)<=60):
            self.heights = _heights
            return 'OK', 200
        else:
            return 'ERROR: wrong value or size', 400
    
    def currentPositionsSetter(self, _currentPositions: numpy.ndarray):
        if(numpy.size(_currentPositions)==15 and numpy.min(_currentPositions)>=0 and numpy.max(_currentPositions)<=60):
            self.currentPositions = _currentPositions
            return 'OK', 200
        else:
            return 'ERROR: wrong value or size', 400
    
    def Getter(self):
        return self.heights
    
Heights = HeightsClass()

def CheckMessage(_request):
    if _request.is_json:
        receivedData = _request.get_json()
        if 'Heights' in receivedData and isinstance(receivedData['Heights'],list):
            return True
        else:
            return 'ERROR: no value named "Heights"', 400
    else:
        return 'ERROR: request is not JSON', 400

@app.route('/')
def default():
    return "\nRaspberryPi nr 2 (16-30). Stan połączenia: OK "

@app.route('/SetHeights', methods=['POST'])
def SetHeights():
    if(CheckMessage(request)==True):
        receivedData = request.get_json()
        return Heights.Setter(numpy.array(receivedData['Heights']))
    else:
        return CheckMessage(request)


@app.route('/GetHeights', methods=['GET'])
def GetHeights():
    return {'Heights':Heights.Getter().tolist()}, 200

@app.route('/Calibration', methods=['POST'])
def Calibration():
    if(CheckMessage(request)==True):
        receivedData = request.get_json()
        return Heights.currentPositionsSetter(numpy.array(receivedData['Heights']))
    else:
        return CheckMessage(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55556)
