def convert_list_in_str(list_in: list) -> str:
    str_out = []
    for i in list_in:
        if i.replace('+', '').replace('-', '').isnumeric():
            sign = ''
            f = '02d'
            if '+' in i:
                sign = '+'
            if '-' in i:
                f = '03d'

            i = int(i)
            i = f'"{sign}{i:{f}}"'
            str_out.append(i)
        else:
            str_out.append(i)

    str_out = (' '.join(str_out))
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)