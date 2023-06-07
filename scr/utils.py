import json
from datetime import datetime
from collections import defaultdict
import time
FILE_JSON = "../operations.json"



# def open_json():
#     # with open(FILE_JSON, 'r', encoding='utf-8') as file:
#     #     number = json.load(file)
#     #     print(number['date'])
#     #     # new_json = defaultdict(lambda x=None: 'Ключ не найден',number)
#     #     # g=sorted(number, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
#     # return  print(number['date'])
#
# open_json()
def conversion_date(date):
    """dfdfdfdfdfddfsdfdfdfdf"""
    date_operaton = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    day = date_operaton.date().day
    month=date_operaton.date().month
    year = date_operaton.date().year
    date_new = f"{day}.{month}.{year}"
    return date_new

with open(FILE_JSON, 'r', encoding='utf-8') as file:
    json_object = json.load(file)
    data = [trans for trans in json_object if trans]
    g = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),reverse=True)
    data2 = [trans for trans in g if trans]
    for i in data2[:6]:
        if i['state'] == 'EXECUTED':

            print(conversion_date(i['date']))
            # try:
            #     print(f"{i['date']} {i['description']}\n {i['to']} \n {i['from']} {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            # except KeyError:
            #     print(f"{i['date']} {i['description']}\n {i['to']} \n  {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")

        # try:
        #     print(i['from'])
        # except KeyError:
        #     print(i['from'])
        # finally:
        #     print(i['from'])
       # if i['from'] in ("", [], None, 0, False):
       #     print("d")


        # if not i['from']:
        #     print(i)




        # if i['state'] =='EXECUTED' :
        #     # data = [trans for trans in i if trans]
        #     print(f"{i['date']} {i['description']}\n {i['to']} \n {i['operationAmount']}" )
            #{data['from']}
            #{i['amount']}







    # try:
    #     json_object = json.load(file)
    #     g = sorted(json_object, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    #     print(g)
    # except:
    #     pass


    # try:
    #     number = json.load(file)
    #     # print(number)
    # except (KeyError):
    #     g = sorted(number, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    #     print(g)




    # raw_questions = json.load(file)
    # for i in raw_questions:
    #     if len(i)!=0:
    #         g = sorted(i, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))

    # g = sorted(raw_questions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    # print(g)

    # print(raw_questions['date'])
    # if isinstance(raw_questions, dict)=="":
    #    pass
    # else:
    #     g = sorted(raw_questions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    #     print(g)

    # print(raw_questions)
    # for i in raw_questions:
    #     # print(f"{raw_questions}\n")
    #     if not i:
    #         print("ffgfgfg")
    #     else:
    #         g = sorted(raw_questions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))

            # g = sorted(raw_questions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))

    # print(i['date'])

        # print(sorted_date)
    # for i in raw_questions[-2:]:
    #     if i['state']=='EXECUTED':
    #         h = i['date'].split(":")[0][:-3]
    #         # print(sorted(i.items(), key=lambda x: datetime.strptime(x[1]['date'], '%Y-%m-%d')))
    #
    #         print(i)
    #         # print(sorted(i,key=lambda x: time.strptime(x['date'], '%Y-%m-%d')))
    #         print(sorted(i['date'].split(":")))
    #
    #         print(i['date'].split(":"))


    #         spisok.append(h)
    #         # spisok.append(i['date'])
    #         print(h)
    #         # h.sort(key=lambda x: time.mktime(time.strptime(x, "%Y-%m-%d")))
    #
    #
    #
    #         # print(f"{sorted(h)} {i['description']}")
    #         # print(list(h))
    #         # h.sort(key=lambda x: time.mktime(time.strptime(x, "%Y-%m-%d")))
    #         spisok.append(h)
    #         # spisok.append(i['description'])
    # spisok.sort(key=lambda x: time.mktime(time.strptime(x, "%Y-%m-%d")))
    # print(spisok)

            # out = sorted(h, key=lambda d: map(int, d.split('-')))

            # out = sorted(i['date'].split(':'))
            # print(i['date'])
            # print(out)
            # print(i['date'].split('.')[0])