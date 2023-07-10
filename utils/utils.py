import json


def get_data(path):
    """
    Получение данных из файла
    """
    if path == 0:
        return path
    else:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data


def get_filtered_data(data):
    """
    Поиск исполненных операций
    """
    filtered_data = []
    for operation in data:
        if operation.get('state') == 'EXECUTED':
            filtered_data.append(operation)

    return filtered_data


def get_sorted_data(data):
    """
    Сортировка операций по дате
    """
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    return sorted_data[0:5]


def get_formate_data(data):
    """
    Вывод списка операций в правильной форме
    """
    formate_data = []
    for operation in data:
        date = f"{operation['date'][8:10]}.{operation['date'][5:7]}.{operation['date'][0:4]}"
        description = f"{operation['description']}"
        from_who = ""
        to_who = ""
        operation_summ = f"{operation['operationAmount']['amount']}"
        operation_currenscy = f"{operation['operationAmount']['currency']['name']}"

        if 'from' in operation:
            from_list = operation['from'].split(" ")
            cards_num = f'{from_list[-1][0:4]} {from_list[-1][5:7]}** **** {from_list[-1][-4:]}'
            del from_list[-1]
            from_list.append(cards_num)
            from_who = ' '.join(from_list)


        if 'to' in operation:
            list_to = operation['to'].split(" ")
            to_card_num = f"**{list_to[-1][-4:]}"
            del list_to[-1]
            list_to.append(to_card_num)
            to_who = ' '.join(list_to)

        right_form = (f"{date} {description}\n"
                     f"{from_who} -> {to_who}\n"
                     f"{operation_summ} {operation_currenscy}\n")

        formate_data.append(right_form)

    return "\n".join(formate_data)
