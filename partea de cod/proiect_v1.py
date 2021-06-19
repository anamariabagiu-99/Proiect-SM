import time # biblioteca pentru timp
import RPi.GPIO as GPIO # biblioteca pentru setarea pinilor

import pigpio # import biblioteca pentru buzzer
pi = pigpio.pi() # creez o instanta a acesteia

# functiile scrise in fisiere
from fct_dist import * # import fisierele scrise 
from fct_baza_2 import * 
from trimis_mail import * # fct pentru trimiterea mailului
from citire_fisier import *

buzzer =18  # setez pinii de pe placuta conform cu pigpio
	# pinul 12
buton = 8 # pinul 24 pe placa
pi.set_mode(buzzer, pigpio.OUTPUT) # setez ca pin de iesire
pi.hardware_PWM(buzzer, 0, 0)
pi.set_pull_up_down(buton,pigpio.PUD_UP) # setez valoarea initiala pe 1

GPIO.setmode(GPIO.BOARD) # setez reprezentarea pinilor pentru a fi la fel ca pe placa

#pinii pentru primul sensor
trig1 = 35  # semnalul de trimis
echo1 = 36 # primirea ecoului

# pinii pentru leduri
zero = 8
unu = 10
doi = 11
trei = 16
patru = 18

# setez pinii de intrare/iesire
# pentru sensorul 1
GPIO.setup(trig1, GPIO.OUT)
GPIO.setup(echo1, GPIO.IN)

# pentru senzorul 2
#GPIO.setup(trig2, GPIO.OUT)
#GPIO.setup(echo2, GPIO.IN)

# pentru leduri
GPIO.setup(zero, GPIO.OUT)
GPIO.setup(unu,GPIO.OUT)
GPIO.setup(doi, GPIO.OUT)
GPIO.setup(trei, GPIO.OUT)
GPIO.setup(patru, GPIO.OUT)

# distantele  intre care consider ca intra o persoana 
d_min = 5
d_max = 10

# numarul de persoane care sunt in  camera
nr_persoane = 0

# numarul maxim de persoane care poate  intra in camera
nr_maxim  = 10 

# numarul mediu de persoane 
nr_mediu = 5

# flaguri pentru a nu trimite prea multe mail-uri
flag_nr_mediu = True
flag_nr_max = True
# functie pentru a actualiza parametrii in timp real 
def actualizare():
	lista = citire()
	nr_mediu = int(lista[0])
	nr_maxim = int(lista[1])
	d_min = int(lista[2])
	d_max = int(lista[3])
	

# functie pentru aprinderea led
def aprinde(vector):
	# setez  pinii de iesire in fct de vectorul primit ca input
	GPIO.output(zero, vector[0])
	GPIO.output(unu, vector[1])
	GPIO.output(doi, vector[2])
	GPIO.output(trei, vector[3])
	GPIO.output(patru, vector[4])

# fct pentru a determina faptul ca o persoana a intrat in incapere
def incrementare():
	print("incrementare")
	# folosesc variabila globala
	global nr_persoane
	# calculez distanta si verific ca aceasta sa fie in interval de
	# 2 ms  in intervalul precizat
	dist1 = calculate_distance(trig1, echo1)
	print(dist1)
	if( d_min <= dist1 <=  d_max):
		time.sleep(0.1)
		dist1 =  calculate_distance(trig1, echo1)
		if( d_min <= dist1 <= d_max):
			time.sleep(0.1)
			dist1 = calculate_distance(trig1, echo1)
			print(dist1)
			if(d_min <= dist1 <= d_max):
				nr_persoane = nr_persoane + 1	
	print("persoane = "+str(nr_persoane))



try:
	stinge = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
	# intru in bucla programului
	while True:
		actualizare()
		incrementare()
		# verific daca nu a iesit o persoana prin apasarea butonului
		if(pi.read(buton)==0):
			time.sleep(0.5)
			nr_persoane = nr_persoane - 1

		# verific daca nr de persoane a depasit maximul permis, 
		# dau un semnal sonor
		if nr_persoane >= nr_mediu:
		        pi.hardware_PWM(buzzer, 500, 500000)
		if nr_persoane >= nr_maxim:
		        pi.hardware_PWM(buzzer, 700, 500000)

		# verific cazurile in care trimit mail
		if nr_persoane == nr_mediu and flag_nr_mediu:
			msg ="Atentie! Se depaseste numarul mediu de persoane"
			#fct_trimite_mail(msg)
			flag_nr_mediu = False # modific starea flagului
				# pentru a  nu mai trimite mail-uri 
		if(nr_persoane == nr_maxim and flag_nr_max):
			msg ="ATENTIE! PREA MULTE PERSOANE IN CAMERA!!!"
		        #fct_trimite_mail(msg)
			flag_nr_max = False
		# verific sa nu depasesc 31, numarul maxim reprezentabil pe 5 biti
		if( nr_persoane < 32):

			vector = baza_2(nr_persoane) # transform nr de persoane in B2
			aprinde(vector) # setez configuratia led-urilor
			time.sleep(0.1)
			aprinde(stinge) # sting ledurile
		pi.hardware_PWM(buzzer, 0, 0) # inchid semnalul sonor



except KeyboardInterrupt:
	pass

GPIO.cleanup()
pi.hardware_PWM(buzzer, 0, 0)
