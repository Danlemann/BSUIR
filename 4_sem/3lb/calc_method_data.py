from fun_gl_formulas import *


def calc_method(formula: str):
    formula_new_disunction_normal_form = (fisunction_normal_form_glu(formula.split('+')))
    iteratir_a = False

    for iterator in range(len(formula_new_disunction_normal_form)):

        if formula_new_disunction_normal_form[iterator].find('*') == -1:
            iteratir_a = True

    if not iteratir_a:
        formula_new_disunction_normal_form = check_for_redundant_implications_sdnf(formula_new_disunction_normal_form)

    for iterator in range(len(formula_new_disunction_normal_form)):
        formula_new_disunction_normal_form[iterator] = '(' + formula_new_disunction_normal_form[iterator] + ')'

    new_data_f = '+'.join(formula_new_disunction_normal_form[i] for i in range(len(formula_new_disunction_normal_form)))

    return new_data_f


def calculation_method_sknf(formula: str):

    elements_new_conunction_normal_form = elements_formula_check_to_rad(gluing_sknf(formula.split('*')))
    iterator_a = False

    for iterator_elem in range(len(elements_new_conunction_normal_form)):
        if elements_new_conunction_normal_form[iterator_elem].find('+') == -1:
            iterator_a = True

    if not iterator_a:
        elements_new_conunction_normal_form = check_for_redundant_implications_sdnf(elements_new_conunction_normal_form)
    for iterator_elem in range(len(elements_new_conunction_normal_form)):
        elements_new_conunction_normal_form[iterator_elem] = \
            '(' + elements_new_conunction_normal_form[iterator_elem] + ')'

    formula_to_cr_new = '*'.join(elements_new_conunction_normal_form[i] for i
                           in range(len(elements_new_conunction_normal_form)))
    return formula_to_cr_new


def elements_formula_check_to_rad(elements_parts_data: list):
    rezultat_element = list()

    for iterator_main in range(len(elements_parts_data)):
        nabor = element_dnf_mv(elements_parts_data, iterator_main)

        if not check_for_needing_sknf(elements_parts_data, nabor, elements_parts_data[iterator_main]):
            rezultat_element.append(elements_parts_data[iterator_main])
        else:
            continue
    return rezultat_element


def element_dnf_mv(elements_parts_data, iterator_main):
    elem_k_i_t = var_make_elements_number(elements_parts_data[iterator_main])
    p_t = elem_conv(elements_parts_data[iterator_main])
    nabor = true_var_k(p_t, elem_k_i_t)
    return nabor


def check_for_redundant_implications_sdnf(parts: list):

    output_elements_data_result = list()

    for iterator_elem in range(len(parts)):
        nabor = kit_temp(iterator_elem, parts)

        if not check_for_needing_sdnf(parts, nabor, parts[iterator_elem]):
            output_elements_data_result.append(parts[iterator_elem])
        else:
            continue
    return output_elements_data_result


def kit_temp(iterator_elem, parts):
    kit = var_make_elements_number(parts[iterator_elem])
    temp_part = elem_conv(parts[iterator_elem])
    nabor = true_varient_formulas_dnf(temp_part, kit)
    return nabor


def elem_conv(part: str):
    elements_temp_move_part = str()
    for iterator_j_to_move in range(len(part)):
        if part[iterator_j_to_move] == '!':
            elements_temp_move_part += ' not '
        elif part[iterator_j_to_move] == '+':
            elements_temp_move_part += ' or '
        elif part[iterator_j_to_move] == '*':
            elements_temp_move_part += ' and '
        else:
            elements_temp_move_part += part[iterator_j_to_move]

    return elements_temp_move_part


def true_varient_formulas_dnf(part: str, kit: list):
    for element_iterator_k in range(1, len(kit)):
        part_element = part
        for i in range(len(kit[0])):
            part_element = part_element.replace(kit[0][i], kit[element_iterator_k][i])
        if int(eval(part_element)) == 1:
            return [kit[0], kit[element_iterator_k]]


def true_var_k(part: str, kit: list):

    for iterator_element_k in range(1, len(kit)):
        element_data_temp = part

        for iterator_element_temp in range(len(kit[0])):
            element_data_temp = element_data_temp.replace(kit[0][iterator_element_temp],
                                                          kit[iterator_element_k][iterator_element_temp])

        if int(eval(element_data_temp)) == 0:
            return [kit[0], kit[iterator_element_k]]


def change_value(temp_rez: str, elem_take_arguments: bool):

    rezult_to_data_output = str()

    for iterator_for_data_element in range(len(temp_rez)):

        if temp_rez[iterator_for_data_element] == '!' and temp_rez[iterator_for_data_element + 1] == '0':
            rezult_to_data_output += '1'
            elem_take_arguments = True

        elif temp_rez[iterator_for_data_element] == '!' and temp_rez[iterator_for_data_element + 1] == '1':
            rezult_to_data_output += '0'

            elem_take_arguments = True

        elif temp_rez[iterator_for_data_element] == '1' and \
                not elem_take_arguments and temp_rez[iterator_for_data_element - 1] != 'x':
            rezult_to_data_output += '1'

        elif temp_rez[iterator_for_data_element] == '0' and not elem_take_arguments:
            rezult_to_data_output += '0'

        elif not elem_take_arguments:
            rezult_to_data_output += temp_rez[iterator_for_data_element]

        else:
            elem_take_arguments = False

    return rezult_to_data_output


def check_for_needing_sdnf(parts: list, nabor: list, part: str):
    data_elem_t = ''

    data_elem_t = cikle_dnf_need(data_elem_t, nabor, part, parts)

    rez = change_value(data_elem_t, False)

    rez = rez.split('+')
    elem_check(rez)

    for iterator_elements_data_move in range(len(rez) - 1):
        for iterator_j_elem in range(iterator_elements_data_move + 1, len(rez)):

            if rez[iterator_elements_data_move] == '' or rez[iterator_j_elem] == '':
                continue

            elements_p_one = set(rez[iterator_elements_data_move].split('*'))
            elements_p2 = set(rez[iterator_j_elem].split('*'))

            different = list(set(elements_p_one.union(elements_p2) - elements_p_one.intersection(elements_p2)))

            for iterator_elem_k in range(len(different) - 1):

                for iterator_t in range(iterator_elem_k + 1, len(different)):
                    diff_method(different, iterator_elem_k, iterator_t)
            if len(different) == 0:
                return True
    return False


def diff_method(different, iterator_elem_k, iterator_t):

    if str(different[iterator_elem_k]) == \
            str('!' + different[iterator_t]) or str('!' + different[iterator_elem_k]) == str(
        different[iterator_t]):
        different.remove(different[iterator_t])
        different.remove(different[iterator_elem_k])


def elem_check(rez):
    for iterator_elements_data_move in range(len(rez)):
        if rez[iterator_elements_data_move].find('0') != -1:
            rez[iterator_elements_data_move] = ''


def cikle_dnf_need(data_elem_t, nabor, part, parts):
    for iterator_elements_data_move in range(len(parts)):
        if parts[iterator_elements_data_move] == part:
            continue
        temp_part = parts[iterator_elements_data_move]
        for k in range(len(nabor[0])):
            temp_part = temp_part.replace(nabor[0][k], nabor[1][k])
        data_elem_t += temp_part + '+'
    return data_elem_t


def check_for_needing_sknf(parts: list, nabor: list, part: str):
    element_data_temp_result = ''

    for iterator_to_element_data_move in range(len(parts)):
        if parts[iterator_to_element_data_move] == part:
            continue
        temp_part = parts[iterator_to_element_data_move]
        for iterator_k in range(len(nabor[0])):
            temp_part = temp_part.replace(nabor[0][iterator_k], nabor[1][iterator_k])
        element_data_temp_result += temp_part + '*'

    rezultation_data_element = change_value(element_data_temp_result, False)

    rezultation_data_element = rezultation_data_element.split('*')
    for iterator_to_element_data_move in range(len(rezultation_data_element)):
        if rezultation_data_element[iterator_to_element_data_move].find('1') != -1 \
                and rezultation_data_element[iterator_to_element_data_move][rezultation_data_element
                                                                            [iterator_to_element_data_move]
                                                                                    .find('1') - 1] != 'x':
            rezultation_data_element[iterator_to_element_data_move] = ''

    for iterator_to_element_data_move in range(len(rezultation_data_element) - 1):
        for iterator_j_elem in range(iterator_to_element_data_move + 1, len(rezultation_data_element)):

            if rezultation_data_element[iterator_to_element_data_move] == '' \
                    or rezultation_data_element[iterator_j_elem] == '':
                continue

            p1 = set(rezultation_data_element[iterator_to_element_data_move].split('+'))
            p2 = set(rezultation_data_element[iterator_j_elem].split('+'))

            different = list(set(p1.union(p2) - p1.intersection(p2)))

            for iterator_k in range(len(different) - 1):

                for iterator_j in range(iterator_k + 1, len(different)):
                    if str(different[iterator_k]) == str('!' + different[iterator_j]) \
                            or str('!' + different[iterator_k]) == str(
                            different[iterator_j]):
                        new_count(different, iterator_j, iterator_k)
            if len(different) == 0:
                return True
    return False


def var_make_elements_number(part):
    elements_cout_output_data = int(0)
    kit = []
    k_i_t_arg_key = []
    for iterator_element_d in range(len(part)):
        if part[iterator_element_d] == 'x':
            elements_cout_output_data += 1
            k_i_t_arg_key.append(str(part[iterator_element_d] + part[iterator_element_d + 1]))
    kit.append(k_i_t_arg_key)
    method_kit_check(elements_cout_output_data, kit)

    return kit


def method_kit_check(elements_cout_output_data, kit):
    for iterator_element_d in range(2 ** elements_cout_output_data):
        binary = bin(iterator_element_d)[2:].zfill(elements_cout_output_data)
        kit.append([str(x) for x in binary])


def new_count(different, iterator_j, iterator_k):
    different.remove(different[iterator_j])
    different.remove(different[iterator_k])
