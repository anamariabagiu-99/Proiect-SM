def citire():
	f = open("/var/www/html/date_p.txt", "r")
	sir = f.read()
	print(sir)
	lista = sir.split(' ')
	return lista

'''def main():
	lista = citire()
	print(lista)
main()'''
