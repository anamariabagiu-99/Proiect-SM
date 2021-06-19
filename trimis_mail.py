import smtplib

# fct pentru a trimite mail
def fct_trimite_mail(msg):
	# deschid serverul web
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	# partea de login
	server.login("zmeuricaraspberry@gmail.com", "RaspberrySA31*")
	# trimit mail
	server.sendmail("zmeuricaraspberry@gmail.com","ana.bagiu1999@gmail.com"
		, msg)
	#server.sendmail("zmeuricaraspberry@gmail.com","sopcastefania@gmail.com", msg)
	
	# inchid serverul
	server.quit()
