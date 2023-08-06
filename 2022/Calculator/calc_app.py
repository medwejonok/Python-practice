'''
  30.09.22
  Malikov Denis PI22-5
'''
# Словари
number_translation = {'один' : 1, 'два' : 2, 'три' : 3, 'четыре' : 4,
                      'пять' : 5, 'шесть' : 6, 'семь' : 7, 'восемь' : 8,
                      'девять' : 9, 'десять': 10, 'одинадцать': 11, 'двенадцать': 12,
                      'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
                      'семнадцать': 17, 'восемьнадцать': 18, 'девятнадцать': 19, 'двадцать': 20,
                      'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
                      'восемьдесят':80, 'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300,
                      'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
                      'девятьсот': 900, 'тысяча': 1000, 'две тысячи': 2000, 'три тысячи': 3000,
                      'четыре тысячи': 4000, 'пять тысяч': 5000, 'шесть тысяч': 6000, 'семь тысяч': 7000,
                      'восемь тысяч': 8000, 'девять тысяч': 9000, 'одна': 1, 'две': 2}
number_translation1 = {'одна' : 1, 'две' : 2, 'три' : 3, 'четыре' : 4,
                      'пять' : 5, 'шесть' : 6, 'семь' : 7, 'восемь' : 8,
                      'девять' : 9, 'десять': 10, 'одинадцать': 11, 'двенадцать': 12,
                      'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
                      'семнадцать': 17, 'восемьнадцать': 18, 'девятнадцать': 19, 'двадцать': 20,
                      'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
                      'восемьдесят':80, 'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300,
                      'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
                      'девятьсот': 900, 'тысяча': 1000, 'две тысячи': 2000, 'три тысячи': 3000,
                      'четыре тысячи': 4000, 'пять тысяч': 5000, 'шесть тысяч': 6000, 'семь тысяч': 7000,
                      'восемь тысяч': 8000, 'девять тысяч': 9000, 'одна': 1, 'две': 2}
operators = {'открывается':'(', 'закрывается':')', 'плюс':'+', 'минус':'-', 'разделить':'/', 'умножить':'*', 'степени':'**'}
digits = {'десятая': 1, 'десятых': 1, 'сотая': 2, 'сотых': 2, 'тысячная':3, 'тысячных':3, 'десятитысячных':4, 'десятитысячная':4}
digits1 = {'1o':'десятая', '1':'десятых', '2o':'сотая', '2':'сотых', '3o':'тысячная', '3':'тысячных', '4o':'десятитысячная', '4':'десятитысячных'}


# Функции
def num_after_point(l):
    '''
    Функция для перевода числа после точки в цифры
    '''
    global number_translation
    digit = l[-1]
    number = 0
    for i in range(len(l)-1):
        number += number_translation[l[i]]
    number = str(number)
    if len(number) < digits[digit]:
        return '0'*(digits[digit] - len(number)) + number 
    return number
# Классы
class Digits:
    '''
    Функции rez_digitN класса Digits отвечают за перевод цифр в слова
    '''
    def rez_digit1(self, num):
        global number_translation
        if num == '0':
            return ''
        for v in number_translation.keys():
            if number_translation[v] == int(num):
                return v
            
    def rez_digit2(self, num):
        global number_translation
        if num[0] == '0':
            return self.rez_digit1(num[1:])
        if 10 <= int(num) <= 19:
            for v in number_translation.keys():
                if number_translation[v] == int(num):
                    return v
        else:
            digit = num[0] + '0'
            for v in number_translation.keys():
                if number_translation[v] == int(digit):
                    return v + " " + self.rez_digit1(num[1])
                        
    def rez_digit3(self, num):
        global number_translation
        if num[0] == '0':
            return self.rez_digit2(num[1:])
        digit = num[0] + '00'
        for v in number_translation.keys():
            if number_translation[v] == int(digit):
                return v + " " + self.rez_digit2(num[1:])

    def rez_digit4(self, num):
        global number_translation
        digit = num[0] + '000'
        for v in number_translation.keys():
            if number_translation[v] == int(digit):
                return v + " " + self.rez_digit3(num[1:])

class Digits_after_point:
    '''
    Функции rez_digitN класса Digits_after_point отвечают за перевод цифр после точки в слова
    Функция last_digit класса Digit определяет разряд числа
    '''

    def last_digit(self, num_a_p):
        global digits1
        
        x = str(len(num_a_p))
        if num_a_p[-1] == '1':
            x += 'o'
        y = digits1[x]
        return y
    
    def rez_digit1(self, num):
        global number_translation1
        if num == '0':
            return ''
        for v in number_translation1.keys():
            if number_translation1[v] == int(num):
                return v
            
    def rez_digit2(self, num):
        global number_translation1
        if num[0] == '0':
            return self.rez_digit1(num[1:])
        if 10 <= int(num) <= 19:
            for v in number_translation1.keys():
                if number_translation1[v] == int(num):
                    return v
        else:
            digit = num[0] + '0'
            for v in number_translation1.keys():
                if number_translation1[v] == int(digit):
                    return v + " " + self.rez_digit1(num[1])
                        
    def rez_digit3(self, num):
        global number_translation1
        if num[0] == '0':
            return self.rez_digit2(num[1:])
        digit = num[0] + '00'
        for v in number_translation1.keys():
            if number_translation1[v] == int(digit):
                return v + " " + self.rez_digit2(num[1:])

    def rez_digit4(self, num):
        global number_translation1
        digit = num[0] + '000'
        for v in number_translation1.keys():
            if number_translation1[v] == int(digit):
                return v + " " + self.rez_digit3(num[1:])
dig = Digits()
digap = Digits_after_point()

'''
Цикл текстового калькулятора (прекрощается после ввода пустой строки)
'''
while True:
    string = input().split()
    if string == []:
        break
    
    # Удаление лишних элементов массива
    try:
        while True:
            string.remove('на')
    except ValueError:
        pass
    try:
        while True:
            string.remove('скобка')
    except ValueError:
        pass
    try:
        while True:
            string.remove('в')
    except ValueError:
        pass
    
    res = ''
    flag_for_point = False
    number = 0

    '''
    Переводим входные данные в нужный нам вид (Например: "два плюс три" -> "2+3"
    '''
    for i in range(len(string)):
        # Проверка на оператор, скобку 
        if string[i] in operators:
            res += operators[string[i]]

        # Пропуск цифр после точки если точка уже найдена
        if flag_for_point:
            if string[i] not in operators:
                continue
            else:
                flag_for_point = False
                
        # Перевод числа после точки в цифры
        if string[i] == 'и':
            res += '.'
            num_af = []
            for j in range(i+1, len(string)):
                if string[j] in operators:
                    break
                else:
                    num_af.append(string[j])
            res += num_after_point(num_af)
            flag_for_point = True
            
        # Обработка чисел
        if string[i] in number_translation:
            number += number_translation[string[i]]
            if i == len(string)-1:
                res += str(number)
                number = 0
            else:
                if string[i+1] in number_translation:
                    continue
                else:
                    res += str(number)
                    number = 0
    # Производим вычисление
    res = eval(res)
    num = str(res)
    first_part, second_part, third_part = 0, 0, 0
    minus = False
    point = False

    if num[0] == '-':
        minus = True
        num = num[1:]

    if '.' in num:
        point = True
        num_a_p = num[num.index('.')+1:]
        third_part = digap.last_digit(num_a_p)
        index_of_zero = 0
        num = num[:num.index('.')]

        for i in range(len(num_a_p)):
            if num_a_p[i] != '0':
                break
            else:
                index_of_zero = i
        if index_of_zero != 0:
            index_of_zero += 1
         
        num_a_p = num_a_p[index_of_zero:]
        if len(num_a_p) == 1:
            second_part = digap.rez_digit1(num_a_p)
        if len(num_a_p) == 2:
            second_part = digap.rez_digit2(num_a_p)
        if len(num_a_p) == 3:
            second_part = digap.rez_digit3(num_a_p)
        if len(num_a_p) == 4:
            second_part = digap.rez_digit4(num_a_p)

                
    if num == '0':
        first_part = 'ноль'
    else:
        if len(num) == 1:
            first_part = dig.rez_digit1(num)
        if len(num) == 2:
            first_part = dig.rez_digit2(num)
        if len(num) == 3:
            first_part = dig.rez_digit3(num)
        if len(num) == 4:
            first_part = dig.rez_digit4(num)

    if point:
        if minus:
            print('минус', first_part, 'и', second_part, third_part)
        else:
            print(first_part, 'и', second_part, third_part)
    else:
        if minus:
            print('минус', first_part)
        else:
            print(first_part)
        
