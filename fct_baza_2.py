import RPi.GPIO as GPIO
# setez valorile de high si de low ale  vectorului de iesire
unu_logic = GPIO.HIGH
zero_logic = GPIO.LOW

# scriu functie pentru a transforma in b2
def baza_2(numar):
	# setez iesirea pe  o logic
	iesire =[zero_logic, zero_logic, zero_logic, zero_logic, zero_logic]
	i = 0 # pastrez un contor pentru a stii ce pozitie din vector modific
	# descompun numarul prin impartirii succesive la 2
	while numar>0:
		# in fct de restul impartirii la 2 modific starea pinului 
	# iesire
		if numar % 2 == 1:	
			iesire[i] = unu_logic
		numar = numar/2 
		i = i+1 #  
	print("am iesit din fct de baza 2")
	return iesire

