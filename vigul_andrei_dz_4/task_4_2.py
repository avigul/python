'''
Программа поиска курса валют по обозначению на сайте центробанка

import requests
import xml.etree.ElementTree as ET

r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
str = r.text
count = 0
xml = ET.fromstring(str)
ChC = input('Введите буквенный код валюты: ')
ChC_UP = ChC.upper()
for val in xml.findall('Valute'):
	CharName = val.find('CharCode').text
	Value = val.find('Value').text
	Name = val.find('Name').text
	if CharName == ChC_UP:
		count = 1
		print('Курс валюты '+ Name + ' ' + Value + ' ' + 'рублей')
if count != 1:
	print('Валюта не найдена')
'''
import requests
import xml.etree.ElementTree as ET


def currency_rates(code: str) -> float:
	response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
	my_str = response.text
	count = 0
	xml = ET.fromstring(my_str)
	ChC = input('Введите буквенный код валюты: ')
	ChC_UP = ChC.upper()
	for val in xml.findall('Valute'):
		CharName = val.find('CharCode').text
		Value = val.find('Value').text
		Name = val.find('Name').text
		if CharName == ChC_UP:
			count = 1
			result_value = f'Курс валюты ' + {Name} + ' ' + {Value} + ' ' + 'рублей'
		if count != 1:
			result_value = f'Валюта не найдена'

    	return result_value


result = result_value
print(currency_rates(result))