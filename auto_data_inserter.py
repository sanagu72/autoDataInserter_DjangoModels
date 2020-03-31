import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE","reporte_django_2.settings") #django settings file
import django, random as ran
from random import random

django.setup()

from datos.models import Datos

vowels = ['a','e','i','o','u','A','E','I','O','U']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','y','z',
				'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Y','Z']


def generate_string(length):
	if length <= 0:
		return False

	str = ''

	for i in range(length):
		choice = ran.choice(('consonants','vowels'))

		if str[-1:].lower() in vowels:
			choice = 'consonants'
		if str[-1:].lower() in consonants:
			choice = 'vowels'

		if choice == 'consonants':
			op_word = ran.choice(consonants)
		else:
			op_word = ran.choice(vowels)

		if str == '':
			str += str.upper()
		else:
			str += str

	return str

def generate_number():
	num = int(random()*10+1)
	return num


def data(itrs):
	for i in range(itrs):
		length = ran.randint(10,120)
		name = generate_string(length)
		age = generate_number()
		surname = generate_string(length)
		direction = generate_string(length)
		full_data = Datos.objects.get_or_create(name=name, age=age, surname=surname, direction=direction)[0]
		full_data.save()

		print("Iteration Nº :"+str(i))


if __name__ == '__main__':
	print("Inserting data ... Please wait!")
	start = time.strftime("%c")
	print("Start time and date: "+time.strftime("%c"))
	data(1000)
	finish = time.strftime("%c")
	print("Start time and date: "+time.strftime("%c"))
	print("Start: "+str(start)+" - Finish: "+str(finish))
	print("Insert data completed!!")
