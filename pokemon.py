'''
This code was developed to use voice commands to control
pokemon GO battles
Author: Botmation Rising
'''
from pynput.mouse import Button, Controller
import speech_recognition as sr
from time import ctime
import time
import threading

mouse = Controller()
  
def listener():
    # Record Audio
	r = sr.Recognizer()
	r.energy_threshold = 800
	with sr.Microphone(sample_rate = 44100) as source:
		print("Say something!")
		audio = r.listen(source,None, 6)

		data = ""
		try:
			print("processing")
			data = r.recognize_google(audio)
			print("Google Speech Recognition " + data)
              
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand your audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		return data
     
  
def command(data):	
	threads = [ ]
	data = data.lower()
	if "use charge" in data:#Charge attack
		t2 = threading.Thread(target=charged)
		threads.append(t2)
		t2.start()
	if "use quick" in data:
		t1 = threading.Thread(target=quick)
		threads.append(t1)
		t1.start()
	if "use thunder" in data:#Charge attack
		t2 = threading.Thread(target=charged2)
		threads.append(t2)
		t2.start()
	if "use wild" in data:#Charge attack
		t2 = threading.Thread(target=charged1)
		threads.append(t2)
		t2.start()	
	if "used tackle" in data:
		t1 = threading.Thread(target=quick)
		threads.append(t1)
		t1.start()	
	if "use tackle" in data:
		t1 = threading.Thread(target=quick)
		threads.append(t1)
		t1.start()		
	if "use fire punch" in data:#Charge attack
		t2 = threading.Thread(target=charged)
		threads.append(t2)
		t2.start()	
	if "use horn" in data:#Charge attack
		t2 = threading.Thread(target=charged)
		threads.append(t2)
		t2.start()	
	if "use counter" in data:	    
		t1 = threading.Thread(target=quick)
		threads.append(t1)
		t1.start()

def quick():
	print("Quick")
	for x in range(0, 14):
		mouse.position = (1600, 336)
		mouse.click(Button.left, 1)	
		time.sleep(0.8)
	
def charged():	
	print("Charged")
	mouse.position = (1608, 741)
	mouse.click(Button.left, 1)
	time.sleep(1)
	for x in range(0, 45):
		mouse.position = (1608, 742)
		mouse.click(Button.left, 1)	
		time.sleep(0.1)

def charged1():	
	print("Charged1")
	mouse.position = (1494, 742)
	mouse.click(Button.left, 1)
	time.sleep(1)
	for x in range(0, 45):
		mouse.position = (1494, 742)
		mouse.click(Button.left, 1)	
		time.sleep(0.1)

def charged2():	
	print("Charged2")
	mouse.position = (1712, 742)
	mouse.click(Button.left, 1)
	time.sleep(1)
	for x in range(0, 45):
		mouse.position = (1712, 742)
		mouse.click(Button.left, 1)	
		time.sleep(0.1)		
	
while 1:
	try:
		input("Press enter to continue") #Can remove this line for continuous listen mode
	except SyntaxError:
		pass
	info = listener()
	command(info)
	
