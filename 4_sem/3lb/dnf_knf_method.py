from create_table import *


def formula_to_create_conunction_normal_form(formula):
    sdf_splut_formula = sdnf(formula).split()
    binary_sdnf_elements_formula = list()
    for i in range(0, len(sdf_splut_formula)):
        if sdf_splut_formula[i][0] == 'x':
            binary_sdnf_elements_formula.append('1')
        elif sdf_splut_formula[i][0] == '!':
            binary_sdnf_elements_formula.append('0')
        elif sdf_splut_formula[i][0] == ')':
            binary_sdnf_elements_formula.append('+')
    binary_sdnf_elements_formula = ''.join(binary_sdnf_elements_formula[:-1])
    sdnf_dec = bin_to_dec(binary_sdnf_elements_formula, formula)
    sdnf_dec = map(str, sdnf_dec)
    sdnf_dec = '+(' + ', '.join(sdnf_dec) + ')'
    return binary_sdnf_elements_formula, sdnf_dec


def method_to_create_conunction_normal_form(formula):
    sknf_form_to_create_output = ''
    data_with_elements = cr_tabl(formula)[1]
    for iterator in data_with_elements:
        if iterator['f'] == 0:
            part = '+'.join([values * '!' + keys for keys, values in iterator.items() if keys != 'f' and keys != 'i'])
            sknf_form_to_create_output += '(' + str(part) + ')' + '*'
    sknf_form_to_create_output = sknf_form_to_create_output[:-1]
    return sknf_form_to_create_output


def numb_to_create_conunction_normal_form(formula):
    perfect_conunction_form_in_number = method_to_create_conunction_normal_form(formula).split()
    binary_conunction_normal_elements = list()
    for iterator in range(0, len(perfect_conunction_form_in_number)):
        if perfect_conunction_form_in_number[iterator][0] == 'x':
            binary_conunction_normal_elements.append('0')
        elif perfect_conunction_form_in_number[iterator][0] == '!':
            binary_conunction_normal_elements.append('1')
        elif perfect_conunction_form_in_number[iterator][0] == ')':
            binary_conunction_normal_elements.append('*')
    binary_conunction_normal_elements = ''.join(binary_conunction_normal_elements[:-1])
    decembary_conunction_element_in = bin_to_dec(binary_conunction_normal_elements, formula)
    decembary_conunction_element_in = map(str, decembary_conunction_element_in)
    decembary_conunction_element_in = '*(' + ', '.join(decembary_conunction_element_in) + ')'

    return binary_conunction_normal_elements, decembary_conunction_element_in


def sdnf(formula):
    formula_to_create_disunction_normal_form = ''
    data_table = cr_tabl(formula)[1]
    for iterator in data_table:
        if iterator['f'] == 1:
            part = '*'.join([abs(values - 1) * '!' + keys for keys, values in iterator.items()
                             if keys != 'f' and keys != 'i'])
            formula_to_create_disunction_normal_form += '(' + str(part) + ')' + '+'
    formula_to_create_disunction_normal_form = formula_to_create_disunction_normal_form[0:-1]
    return formula_to_create_disunction_normal_form