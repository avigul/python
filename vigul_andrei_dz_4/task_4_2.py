import requests
import xml.etree.ElementTree as ET


def currency_rates(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    my_str = response.text
    xml = ET.fromstring(my_str)
    code = code.upper()

    for my_value in xml.findall('Valute'):
        name = my_value.find('Name').text
        char_name = my_value.find('CharCode').text
        value = my_value.find('Value').text
        if char_name == code:
            result_value = float(value.replace(',', '.'))
            result_value = (f'Курс валюты на сегодня: {name} {result_value:.2f} рублей')
            break
        else:
            result_value = (f'Валюта не найдена')
    return result_value


code = input('Введите буквенный код валюты: ')
result_value = currency_rates(code)
print(result_value)