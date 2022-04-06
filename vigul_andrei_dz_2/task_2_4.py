def convert_name_extract(list_in: list) -> list:
    name_list = [i.split()[-1].capitalize() for i in list_in]
    list_out = [f'Привет, {i}!' for i in name_list]
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)