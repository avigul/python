def thesaurus(*names) -> dict:
    list_names = {name for name in names}
    big_letters = [name[0].upper() for name in list_names]
    dict_out = {key: list() for key in big_letters}
    for name in list_names:
        dict_out[name[0]].append(name)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Константин", "Олег", "Дмитрий", "Андрей", "Оскар", "Алексей", "Кирил" ))

'''
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
'''