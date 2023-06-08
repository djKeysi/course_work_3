import json
from datetime import datetime
from scr.utils import check_on_score

FILE_JSON = "../operations.json"



def conversion_date(date):
    """Функция перевода даты (2019-01-05T00:52:30.108534) из файла .json в нормальный вид (8.12.2019)"""
    date_operaton = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    day = date_operaton.date().day
    month=date_operaton.date().month
    year = date_operaton.date().year
    date_new = f"{day}.{month}.{year}"
    return date_new


def main():
    """Функция точки входа в программу и чтение с файла .json и окончательный вывод результата"""
    with open(FILE_JSON, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        null_dict = [trans for trans in json_file if trans]
        sort_json_files = sorted(null_dict, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse = True)

        for sort_json_file in sort_json_files[:6]:

            status_translate= sort_json_file['state']
            data = conversion_date(sort_json_file['date'])
            description_translate = sort_json_file['description']
            transfer_to = sort_json_file['to']
            sum_operation = sort_json_file['operationAmount']['amount']
            currency_operation = sort_json_file['operationAmount']['currency']['name']

            if status_translate == 'EXECUTED':

                try:
                    transfer_from =sort_json_file['from']
                    print(f"{data} {description_translate}\n{check_on_score(transfer_from)} -> {check_on_score(transfer_to)} \n{sum_operation} {currency_operation}")
                    print()
                except KeyError:
                    print(f"{data} {description_translate}\n{check_on_score(transfer_to)} \n{sum_operation} {currency_operation}")
                    print()


if __name__ == "__main__":
    main()
