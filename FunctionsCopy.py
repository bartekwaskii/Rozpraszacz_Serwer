import numpy
import socket
import numpy
import math
import signal
import time
from time import sleep
import 	RPi.GPIO as GPIO

run=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(3, GPIO.OUT) # trzeba sprawdzić, czy te piny są poprawne
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

pwmB=GPIO.PWM(40,50)
pwmA=GPIO.PWM(32,50)
pwmC=GPIO.PWM(3,50)
pwmD=GPIO.PWM(5,50)
pwmE=GPIO.PWM(22,50)
pwmF=GPIO.PWM(8,50)
pwmG=GPIO.PWM(10,50)
pwmH=GPIO.PWM(11,50)
pwmI=GPIO.PWM(12,50)
pwmJ=GPIO.PWM(13,50)
pwmK=GPIO.PWM(15,50)
pwmL=GPIO.PWM(16,50)
pwmM=GPIO.PWM(18,50)
pwmN=GPIO.PWM(19,50)
pwmO=GPIO.PWM(21,50)

pwmA.start(0)
pwmB.start(0)
pwmC.start(0)
pwmD.start(0)
pwmE.start(0)
pwmF.start(0)
pwmG.start(0)
pwmH.start(0)
pwmI.start(0)
pwmJ.start(0)
pwmK.start(0)
pwmL.start(0)
pwmM.start(0)
pwmN.start(0)
pwmO.start(0)

def CheckMessage(_request):
    if not _request.is_json:
        return 'ERROR: request is not JSON', 400   
    receivedData = _request.get_json()
    if 'Heights' in receivedData:
        return True
    else:
        return 'ERROR: no value named "Heights"', 400
    
def StartSettingHeights(_heights: numpy.ndarray, _previousPositions: numpy.ndarray):
	
	# position_vector=numpy.fromstring(well_positions, sep=',')
	Z=13/10
	magic_numbers= numpy.array([Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z,Z])
	delta_vector=numpy.subtract(_heights, _previousPositions)
	servo_runtimes=numpy.multiply(delta_vector, magic_numbers)

	RuntimeA=servo_runtimes[0]
	RuntimeB=servo_runtimes[1]
	RuntimeC=servo_runtimes[2]
	RuntimeD=servo_runtimes[3]
	RuntimeE=servo_runtimes[4]
	RuntimeF=servo_runtimes[5]
	RuntimeG=servo_runtimes[6]
	RuntimeH=servo_runtimes[7]
	RuntimeI=servo_runtimes[8]
	RuntimeJ=servo_runtimes[9]
	RuntimeK=servo_runtimes[10]
	RuntimeL=servo_runtimes[11]
	RuntimeM=servo_runtimes[12]
	RuntimeN=servo_runtimes[13]
	RuntimeO=servo_runtimes[14]
	
	if RuntimeA > 0:
		DutyCycleA=10
	elif RuntimeA < 0:
		DutyCycleA=5
	else:
		DutyCycleA=7.5
	
	if RuntimeB > 0:
		DutyCycleB=10
	elif RuntimeB < 0:
		DutyCycleB=5
	else:
		DutyCycleB=7.5
	
	if RuntimeC > 0:
		DutyCycleC=10
	elif RuntimeC < 0:
		DutyCycleC=5
	else:
		DutyCycleC=7.5
	
	if RuntimeD > 0:
		DutyCycleD=10
	elif RuntimeD < 0:
		DutyCycleD=5
	else:
		DutyCycleD=7.5

	if RuntimeE > 0:
		DutyCycleE=10
	elif RuntimeE < 0:
		DutyCycleE=5
	else:
		DutyCycleE=7.5
	
	if RuntimeF > 0:
		DutyCycleF=10
	elif RuntimeF < 0:
		DutyCycleF=5
	else:
		DutyCycleF=7.5
	
	if RuntimeG > 0:
		DutyCycleG=10
	elif RuntimeG < 0:
		DutyCycleG=5
	else:
		DutyCycleG=7.5
	
	if RuntimeH > 0:
		DutyCycleH=10
	elif RuntimeH < 0:
		DutyCycleH=5
	else:
		DutyCycleH=7.5
	
	if RuntimeI > 0:
		DutyCycleI=10
	elif RuntimeI < 0:
		DutyCycleI=5
	else:
		DutyCycleI=7.5
	
	if RuntimeJ > 0:
		DutyCycleJ=10
	elif RuntimeJ < 0:
		DutyCycleJ=5
	else:
		DutyCycleJ=7.5
	
	if RuntimeK > 0:
		DutyCycleK=10
	elif RuntimeK < 0:
		DutyCycleK=5
	else:
		DutyCycleK=7.5
	
	if RuntimeL > 0:
		DutyCycleL=10
	elif RuntimeL < 0:
		DutyCycleL=5
	else:
		DutyCycleL=7.5
	
	if RuntimeM > 0:
		DutyCycleM=10
	elif RuntimeM < 0:
		DutyCycleM=5
	else:
		DutyCycleM=7.5
	
	if RuntimeN > 0:
		DutyCycleN=10
	elif RuntimeN < 0:
		DutyCycleN=5
	else:
		DutyCycleN=7.5
	
	if RuntimeO > 0:
		DutyCycleO=10
	elif RuntimeO < 0:
		DutyCycleO=5
	else:
		DutyCycleO=7.5
	
	RuntimeA=abs(RuntimeA)
	RuntimeB=abs(RuntimeB)
	RuntimeC=abs(RuntimeC)
	RuntimeD=abs(RuntimeD)
	RuntimeE=abs(RuntimeE)
	RuntimeF=abs(RuntimeF)
	RuntimeG=abs(RuntimeG)
	RuntimeH=abs(RuntimeH)
	RuntimeI=abs(RuntimeI)
	RuntimeJ=abs(RuntimeJ)
	RuntimeK=abs(RuntimeK)
	RuntimeL=abs(RuntimeL)
	RuntimeM=abs(RuntimeM)
	RuntimeN=abs(RuntimeN)
	RuntimeO=abs(RuntimeO)
	
	pwmA.ChangeDutyCycle(DutyCycleA)
	pwmB.ChangeDutyCycle(DutyCycleB)
	pwmC.ChangeDutyCycle(DutyCycleC)
	pwmD.ChangeDutyCycle(DutyCycleD)
	pwmE.ChangeDutyCycle(DutyCycleE)
	pwmF.ChangeDutyCycle(DutyCycleF)
	pwmG.ChangeDutyCycle(DutyCycleG)
	pwmH.ChangeDutyCycle(DutyCycleH)
	pwmI.ChangeDutyCycle(DutyCycleI)
	pwmJ.ChangeDutyCycle(DutyCycleJ)
	pwmK.ChangeDutyCycle(DutyCycleK)
	pwmL.ChangeDutyCycle(DutyCycleL)
	pwmM.ChangeDutyCycle(DutyCycleM)
	pwmN.ChangeDutyCycle(DutyCycleN)
	pwmO.ChangeDutyCycle(DutyCycleO)
	
	while True:
		sleep(0.1)
		RuntimeA=RuntimeA-0.1
		RuntimeB=RuntimeB-0.1
		RuntimeC=RuntimeC-0.1
		RuntimeD=RuntimeD-0.1
		RuntimeE=RuntimeE-0.1
		RuntimeF=RuntimeF-0.1
		RuntimeG=RuntimeG-0.1
		RuntimeH=RuntimeH-0.1
		RuntimeI=RuntimeI-0.1
		RuntimeJ=RuntimeJ-0.1
		RuntimeK=RuntimeK-0.1
		RuntimeL=RuntimeL-0.1
		RuntimeM=RuntimeM-0.1
		RuntimeN=RuntimeN-0.1
		RuntimeO=RuntimeO-0.1
		
		if RuntimeA < 0:
			pwmA.ChangeDutyCycle(7.5)
		if RuntimeB < 0:
			pwmB.ChangeDutyCycle(7.5)
		if RuntimeC < 0:
			pwmC.ChangeDutyCycle(7.5)
		if RuntimeD < 0:
			pwmD.ChangeDutyCycle(7.5)
		if RuntimeE < 0:
			pwmE.ChangeDutyCycle(7.5)
		if RuntimeF < 0:
			pwmF.ChangeDutyCycle(7.5)
		if RuntimeG < 0:
			pwmG.ChangeDutyCycle(7.5)
		if RuntimeH < 0:
			pwmH.ChangeDutyCycle(7.5)
		if RuntimeI < 0:
			pwmI.ChangeDutyCycle(7.5)
		if RuntimeJ < 0:
			pwmJ.ChangeDutyCycle(7.5)
		if RuntimeK < 0:
			pwmK.ChangeDutyCycle(7.5)
		if RuntimeL < 0:
			pwmL.ChangeDutyCycle(7.5)
		if RuntimeM < 0:
			pwmM.ChangeDutyCycle(7.5)
		if RuntimeN < 0:
			pwmN.ChangeDutyCycle(7.5)
		if RuntimeO < 0:
			pwmO.ChangeDutyCycle(7.5)
		if (RuntimeA < 0 and RuntimeB < 0 and RuntimeC < 0 and RuntimeD < 0 and RuntimeE < 0 and RuntimeF < 0 and RuntimeG < 0 and RuntimeH < 0 and RuntimeI < 0 and RuntimeJ < 0 and RuntimeK < 0 and RuntimeL < 0 and RuntimeM < 0 and RuntimeN < 0):
			break
	return 0

def StartCalibration(_currentPosition: numpy.ndarray):
    # tutaj będzie kod odpowiedzialny z sterowanie stdzienkami
    return 0
