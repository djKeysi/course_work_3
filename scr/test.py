
def get_is_digit(words):
    """"Вытаскиваем из строки цифры перебором"""
    number = ""
    for word in words:
        if word.isdigit():
            number = number + word
    return number

def get_hidden_card(card):
    """Скрываем номер карты в формате 2842 87** **** 9012"""
    return card[:4]+' '+card[4:6] + '** **** ' + card[-4:]
    # return '*' * len(card[:-4]) + card[-4:]


print(get_hidden_card(get_is_digit('Maestro 7810846596785568')))#2842 87** **** 9012

def get_hidden_score(score):
    """Скрываем номер счета в формате **2869"""
    return "**" + score[-4:]

print(get_hidden_score(get_is_digit("Счет 43241152692663622869")))

def check_on_score(word):
    """Главная функция проверки счет это или карта"""
    if word[:4] == "Счет":
        return get_hidden_score(get_is_digit(word))
    else:
        return get_hidden_card(get_is_digit(word))


print(check_on_score('Maestro 7810846596785568'))






