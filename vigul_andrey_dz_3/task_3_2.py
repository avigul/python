def num_translate_adv(value: str) -> str:
    number = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'ноль': 'zero',
              'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five', 'шесть': 'six',
              'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten', }

    if str_in[0] == str_in[0].upper():
        i = number.get(value)
        str_out = i.upper().title()
    else:
        str_out = number.get(value)
    return str_out


str_in = input("Пожалуйста, введите чило от 0 до 10 по русски или по английски: ")
my_number = str_in.lower()
print(num_translate_adv(my_number))
