
def dec_to_bi(number):
    modul_number = abs(number)
    result = str()

    while modul_number > 0:
        result = str(modul_number % 2) + result
        modul_number = modul_number // 2

    result = result.rjust(7, '0')  # Заполняем пустые позиции нулями
    return result


def transform(num_in_10, num_in_2):
    if num_in_10 > 0:  # Прямой
        result = '0' + num_in_2
        return result

    if num_in_10 < 0:  # Дополнительный
        binary_dop_number = '00000001'
        num2_inv = '1' + invert(num_in_2)
        num2_com = plus(num2_inv, binary_dop_number)

        return num2_com


def invert(num2):  # Инвертирует бинарное число
    num2_invert = ''
    for iterator in range(0, len(num2)):
        if num2[iterator] == '0':
            num2_invert += '1'
        elif num2[iterator] == '1':
            num2_invert += '0'
    return num2_invert


def plus(num_1, num_2):
    result = ''
    count = bool(False)
    for iterator in reversed(range(len(num_1))):
        if not count:
            if (num_1[iterator] == '0' and num_2[iterator] == '1') or (num_1[iterator] == '1' and num_2[iterator] == '0'):
                result += '1'
            elif (num_1[iterator] and num_2[iterator]) == '0':
                result += '0'
            elif (num_1[iterator] and num_2[iterator]) == '1':
                result += '0'
                count = True
        elif count:
            if (num_1[iterator] == '0' and num_2[iterator] == '1') or (num_1[iterator] == '1' and num_2[iterator] == '0'):
                result += '0'
                count = True
            elif (num_1[iterator] and num_2[iterator]) == '0':
                result += '1'
                count = False
            elif (num_1[iterator] and num_2[iterator]) == '1':
                result += '1'

    final_rez = result[::-1]
    return final_rez


def multiplication(a2, b2):
    dop_num = '00000000'
    result = ''
    for i in reversed(range(len(b2))):

        if b2[i] == '1':

            end_noll = '0' * (7 - i)
            b = a2[7-i:] + end_noll   # убираем н число нулей в начале и добавляем н нулей в конец
            # result = plus(dop_num, b)   # для функции plus
            intsum = int(dop_num, 2) + int(b, 2)
            result = bin(intsum)
            dop_num = result

    return result


def division(number_1, number_2):
    result = ''
    number1 = '0'
    number2 = number_2
    iterator = 0

    if number_1 < number_2:
        return '0'
    else:
        while True:
            if iterator == len(number_2):
                break
            number1 = number1 + number_1[iterator]

            div_dec = int(number1, 2) / int(number2, 2)  # служит для сравнения среза числителя и полного знаменателя
            if div_dec < 1:  # если знаменатель больше среза знаменателя
                result += '0'

            elif div_dec > 1:
                number1 = bin(int(number1, 2) - int(number2, 2))
                result += '1'

            elif div_dec == 1: # если знаменатель равен срезу числителя
                number1 = '0'
                result += '1'
            iterator += 1

    return result


def bi_to_dec(result):
    dop_number_to_invert = '00000001'
    key = int(result, 2)
    if key > 128:    # условие нужно для выбора правильного перевода кодировок
        inv_res = plus(invert(result), dop_number_to_invert)
        inv_res = int(inv_res, 2)
    else:
        inv_res = int(result, 2)
    if result[0] == '1':
        return - inv_res
    else:
        return inv_res

