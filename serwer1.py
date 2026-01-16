# serwer 1 dla, studzienek 1-15

from flask import Flask, request, jsonify
import numpy
import Functions

app = Flask(__name__)

class HeightsClass:

    def __init__(self):
        self.__heights = numpy.zeros(15) # zmienna z wysokościami do ustawienia/aktualnymi po ustawieniu
        self.__currentPositions = numpy.zeros(15) # zmienna z wartościami do kalibracji/wyzerowania studzienek przed pracą 

    def Setter(self, _heights: numpy.ndarray): # setter wysokości
        if(self.CheckData(_heights)=='OK', 200):
            self.__heights = _heights
            Functions.StartSettingHeights(self.__heights)
        return self.CheckData(_heights)
        
    def CurrentPositionsSetter(self, _currentPositions: numpy.ndarray): # setter kalibracyjny
        if(self.CheckData(_currentPositions)=='OK'):
            self.__currentPositions = _currentPositions
            Functions.StartCalibration(self.__currentPositions)
        return self.CheckData(_currentPositions)
    
    def Getter(self): # getter wysokości
        return self.__heights
    
    def CheckData(self, _heights): # funkcja sprawdzająca poprawność danych 
        if(numpy.size(_heights)==15 and numpy.min(_heights)>=0 and numpy.max(_heights)<=60):
            return 'OK', 200
        else:
            return 'ERROR: wrong value or size', 400

Heights = HeightsClass() # tworzenie obiektu Heights przechowującego informacje o wysokościach studzienek

# endpointy

@app.route('/')
def default():
    return "\nRaspberryPi nr 1 (1-15). Stan połączenia: OK "

@app.route('/SetHeights', methods=['POST'])
def SetHeights():
    if(Functions.CheckMessage(request)==True):
        receivedData = request.get_json()
        return Heights.Setter(numpy.array(receivedData['Heights']))
    else:
        return Functions.CheckMessage(request)


@app.route('/GetHeights', methods=['GET'])
def GetHeights():
    return {'Heights':Heights.Getter().tolist()}, 200

@app.route('/Calibration', methods=['POST'])
def Calibration():
    if(Functions.CheckMessage(request)==True):
        receivedData = request.get_json()
        return Heights.CurrentPositionsSetter(numpy.array(receivedData['Heights']))
    else:
        return Functions.CheckMessage(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555)
