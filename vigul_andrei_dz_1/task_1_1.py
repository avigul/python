def convert_time(duration: int) -> str:
    if duration >= 86400:
        return f"{duration // 86400} дн {duration // 3600 %24} час {duration // 60 % 60} мин {duration % 60} сек"
    elif duration >= 3600:
        return f"{duration // 3600 %24} час {duration // 60 % 60} мин {duration % 60} сек"
    elif duration >= 60:
        return f"{duration // 60 % 60} мин {duration % 60} сек"
    else:
        return f"{duration % 60} сек"


str_in = int(input("Введите время в секундах: "))
print(convert_time(str_in))