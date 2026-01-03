import numpy

def CheckMessage(_request): # funkcja sprawdzająca poprawność typu danych w zapytaniu http post
    if _request.is_json:
        receivedData = _request.get_json()
        if 'Heights' in receivedData:
            return True
        else:
            return 'ERROR: no value named "Heights"', 400
    else:
        return 'ERROR: request is not JSON', 400
    
def StartSettingHeights(_heights: numpy.ndarray):
    # tutaj będzie kod odpowiedzialny z sterowanie stdzienkami
    return 0

def StartCalibration(_currentPosition: numpy.ndarray):
    # tutaj będzie kod odpowiedzialny z sterowanie stdzienkami
    return 0