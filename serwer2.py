# serwer 2 dla, studzienek 16-30

from flask import Flask, request, jsonify
import numpy
import json

app = Flask(__name__)

class HeightsClass:

    def __init__(self):
        self.heights = numpy.zeros(15) # zmienna z wysokościami do ustawienia/aktualnymi po ustawieniu
        self.currentPositions = numpy.zeros(15) # zmienna z wartościami do kalibracji/wyzerowania studzienek przed pracą 

    def Setter(self, _heights: numpy.ndarray): # setter wysokości
        if(self.CheckData(_heights)=='OK', 200):
            self.heights = _heights
        return self.CheckData(_heights)
        
    def currentPositionsSetter(self, _currentPositions: numpy.ndarray): # setter kalibracyjny
        if(self.CheckData(_currentPositions)=='OK'):
            self.currentPositions = _currentPositions
        return self.CheckData(_currentPositions)
    
    def Getter(self): # getter wysokości
        return self.heights
    
    def CheckData(self, _heights): # funkcja sprawdzająca poprawność danych 
        if(numpy.size(_heights)==15 and numpy.min(_heights)>=0 and numpy.max(_heights)<=60):
            return 'OK', 200
        else:
            return 'ERROR: wrong value or size', 400

    
Heights = HeightsClass()

def CheckMessage(_request): # funkcja sprawdzająca poprawność typu danych w zapytaniu http post
    if _request.is_json:
        receivedData = _request.get_json()
        if 'Heights' in receivedData:
            return True
        else:
            return 'ERROR: no value named "Heights"', 400
    else:
        return 'ERROR: request is not JSON', 400

# endpointy

@app.route('/')
def default():
    return "\nRaspberryPi nr 2 (16-30). Stan połączenia: OK ", 200

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
