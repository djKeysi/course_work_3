
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

def get_hidden_score(score):
    """Скрываем номер счета в формате **2869"""
    return "**" + score[-4:]

def check_on_score(word):
    """Главная функция проверки счет это или карта"""
    if word[:4] == "Счет":
        return word[:4]+ " " + get_hidden_score(get_is_digit(word))
    else:
        return ''.join(w for w in word if w.isalpha() or w == ' ') + get_hidden_card(get_is_digit(word))










