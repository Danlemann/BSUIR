def summ_of_floating(number_1, number_2):  # сумма чисел с плавающей точкой
    number_1 = _to_fix(number_1)
    number_2 = _to_fix(number_2)
    unit_number_1 = number_1.find("1", 0, number_1.find("."))
    unit_number_2 = number_2.find("1", 0, number_2.find("."))
    exp_1 = number_1.find(".") - unit_number_1 - 1
    exp_2 = number_2.find(".") - unit_number_2 - 1
    if number_1.find("1", 0, number_1.find(".")) == -1:
        exp_1 = 0
    if number_2.find("1", 0, number_2.find(".")) == -1:
        exp_2 = 0
    if exp_1 >= exp_2:
        diff_exp = exp_1 - exp_2  # Таким образом мы находим бОльшее число (число, где запятая находится дальше)
        number_summ2 = "0" * diff_exp + number_2[:(number_2.find("."))] + number_2[(number_2.find(".") + 1):(
                len(number_2) - diff_exp)]  # Преобразуем меньшее число, смещая его вправо на diff_exp кол-во знаков
        number_summ1 = number_1[:(number_1.find("."))] + number_1[(number_1.find(".") + 1):]
    else:
        diff_exp = exp_2 - exp_1
        number_summ1 = "0" * diff_exp + number_1[:(number_1.find("."))] + number_1[(number_1.find(".") +
                                                                                    1):(len(number_1) - diff_exp)]
        number_summ2 = number_2[:(number_2.find("."))] + number_2[(number_2.find(".") + 1):]
    temp_floating_summ = sum_diff_of_numbers(number_summ1, number_summ2)
    add_numbers = len(temp_floating_summ) - len(number_summ2)
    result = temp_floating_summ[:(max(number_1.find("."), number_2.find("."))) + add_numbers] + "." + \
             temp_floating_summ[(max(exp_1, exp_2) + add_numbers + 1):]

    result = from_decimal_to_float(result)
    return result


def _to_fix(number):
    if number == 0:
        return 0
    number_temp_1 = int(number)
    iterator = 0
    mantissa_size = 23
    fraction_part = number - float(number_temp_1)
    number_temp2 = dec_to_bin_add(number_temp_1)
    if number_temp2.find("1") == -1:
        result = "0" + "."
    else:
        result = number_temp2[number_temp2.find("1"):] + "."
    while iterator <= (mantissa_size - len(result)):
        fraction_part *= 2
        if int(fraction_part) == 0:
            result += "0"
        elif int(fraction_part) == 1:
            fraction_part -= 1
            result += "1"
            if fraction_part == 0:
                result = result.ljust(23, "0")
    return result


def sum_diff_of_numbers(number_1, number_2):  # Сумма/разность чисел
    summa = ""
    carry = 0
    number_1, number_2 = (comparing_length(number_1, number_2))
    for i in reversed(range(0, len(number_1))):
        if (int(number_1[i]) + int(number_2[i]) == 1) and (carry == 0):
            summa = "1" + summa
        elif (int(number_1[i]) + int(number_2[i]) == 1) and (carry > 0):
            summa = "0" + summa
        elif (int(number_1[i]) + int(number_2[i]) == 2) and (carry > 0):
            summa = "1" + summa
        elif (int(number_1[i]) + int(number_2[i]) == 0) and (carry > 0):
            summa = "1" + summa
            carry -= 1
        elif (int(number_1[i]) + int(number_2[i]) == 0) and (carry == 0):
            summa = "0" + summa
        elif (int(number_1[i]) + int(number_2[i]) == 2) and (carry == 0):
            summa = "0" + summa
            carry += 1

    if carry > 0:
        summa = "1" + summa

    return summa


def from_decimal_to_float(number):
    if "1" in number[:number.find(".")]:
        exp_sign = 1
    else:
        exp_sign = -1
    sign_bit = "0"
    if number.find("1", 0, number.find(".")) == -1:
        exp_bits = dec_to_bin_straight(127 + ((number.find("1") - number.find(".")) * exp_sign))[-8:]
    else:
        exp_bits = dec_to_bin_straight(127 + ((number.find(".") - number.find("1") - 1) * exp_sign))[-8:]
    number = number[:number.find(".")] + number[number.find(".") + 1:]
    mantissa = number[number.find("1") + 1:]
    result = sign_bit + " " + exp_bits + " " + mantissa
    print("(01) = " + result)
    return result


def dec_to_bin_straight(number):  # Прямой код
    binary = ""
    tick_of_actions, clone_of_num, tick_of_bits = 0, number, 0
    result = ""
    if abs(number) < 100:
        bit_size = 8
    else:
        bit_size = 16
    if number < 0:
        clone_of_num = -number
    if number == 0:
        binary = str(0)
    while clone_of_num >= 1:
        s1 = str(int(clone_of_num % 2))
        binary = binary + s1
        tick_of_bits += 1
        clone_of_num /= 2
        tick_of_actions = tick_of_actions + 1
        result = binary[::-1]
    if tick_of_bits < bit_size:
        result = result.zfill(bit_size)
    if number < 0:
        result = str(1) + result[1:]
    else:
        result = str(0) + result[1:]
    return result


def dec_to_bin_add(num):  # Дополненный код
    if num < 0:
        result = dec_to_bin_rev(num)
        iterator = 1
        help_add = True
        while help_add:
            temp_result = result[-iterator:len(result)]
            if result[-iterator] == "0":
                temp_result = temp_result.replace('1', '2')
                temp_result = temp_result.replace('0', '1')
                temp_result = temp_result.replace('2', '0')
                result = result[:-iterator] + temp_result
                help_add = False
            else:
                iterator += 1
    else:
        result = dec_to_bin_straight(num)
    return result


def dec_to_bin_rev(num):  # Обратный код
    sign = ''
    if num < 0:
        sign += '1'
        result = dec_to_bin_straight(num)
        result = result.replace('1', '2')
        result = result.replace('0', '1')
        result = result.replace('2', '0')
    else:
        sign += '0'
        result = dec_to_bin_straight(num)
    result = sign + result[1:]
    return result


def comparing_length(number_1, number_2):  # Comparing length of binary codes
    max_length = max(len(number_1), len(number_2))
    if number_1[0] and number_2[0] == "0":
        number_1 = number_1.zfill(max_length)
        number_2 = number_2.zfill(max_length)
    if number_1[0] == "1":
        number_1 = number_1.rjust(max_length, "1")
    if number_2[0] == "1":
        number_2 = number_2.rjust(max_length, "1")
    return number_1, number_2


def from_float_to_decimal(number_in_float):
    spec_exp_number = 127
    number_in_float = number_in_float[:number_in_float.find(" ")] + \
                      number_in_float[(number_in_float.find(" ") + 1):number_in_float.rfind(" ")] + \
                      number_in_float[number_in_float.rfind(" ") + 1:]
    decimal_mantissa = 0.0
    for i in range(9, len(number_in_float)):
        decimal_mantissa += int(number_in_float[i]) * pow(2, -(i - 8))
    exp = int(from_binary_to_decimal("0" + number_in_float[1:9])) - spec_exp_number
    if number_in_float[0] == "1":
        sign_before = "-"
    else:
        sign_before = ""
    result = sign_before + str((1 + decimal_mantissa) * pow(2, exp))
    return result


def from_binary_to_decimal(number_in_bin):
    result = 0
    if number_in_bin.startswith("1"):
        result += ((-int(number_in_bin[1])) * pow(2, (len(number_in_bin) - 2)))
        for iterator in range(2, len(number_in_bin)):
            result += ((int(number_in_bin[iterator])) * pow(2, (len(number_in_bin) - (iterator + 1))))
    elif number_in_bin.startswith("0"):
        for iterator in range(0, len(number_in_bin)):
            result += (int(number_in_bin[iterator]) * pow(2, (len(number_in_bin) - (iterator + 1))))
    return result
