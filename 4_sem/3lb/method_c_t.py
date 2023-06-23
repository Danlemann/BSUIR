from fun_gl_formulas import *

from prettytable import PrettyTable


def main_processor_table(data_element_to_temp, element_input_in_table, elements_in_row_part, rezultation):
    for iterator_i in range(len(elements_in_row_part)):

        for iterator_j in element_input_in_table[0]:

            if iterator_j == 'impl':
                continue

            data_element_to_temp.clear()
            data_for(data_element_to_temp, element_input_in_table, elements_in_row_part, iterator_i, iterator_j)

            if not 'X' in data_element_to_temp:
                rezultation.append(elements_in_row_part[iterator_i])
                break


def function_create_knf_method(iput_form_element: str):

    data_table_with_info, input_data_to_move = c_datatable_create(gluing_sknf(iput_form_element.split('*')),
                                                                  iput_form_element.split('*'), 'sknf')
    list_output_elem = datatab_element_proc(input_data_to_move, gluing_sknf(iput_form_element.split('*')))

    method_range_elem(list_output_elem)
    rezultat_out = '*'.join(list_output_elem)

    return rezultat_out, data_table_with_info


def method_range_elem(list_output_elem):
    for iterator in range(len(list_output_elem)):
        list_output_elem[iterator] = '(' + list_output_elem[iterator] + ')'


def funcrion_reate_c_t_m_disunction_form(input_form: str):

    data_tab, input_data_to_move = c_datatable_create(fisunction_normal_form_glu(input_form.split('+')), input_form.split('+'), 'sdnf')
    rezult_output_element_list = datatab_element_proc(input_data_to_move, fisunction_normal_form_glu(input_form.split('+')))

    rezult_for_out(rezult_output_element_list)
    rezultat_out = '+'.join(rezult_output_element_list)
    return rezultat_out, data_tab


def rezult_for_out(rezult_output_element_list):
    for iterator in range(len(rezult_output_element_list)):
        rezult_output_element_list[iterator] = '(' + rezult_output_element_list[iterator] + ')'


def c_datatable_create(data_element_in_table_implecant: list, element_to_move_const: list, tipe_formula: str):
    d_table_input = list()
    info_input_table = PrettyTable()
    info_input_table.field_names = [
       'impl/kon', *element_to_move_const]
    value_for_arguments = []
    bool_method_cnf(data_element_in_table_implecant, element_to_move_const, tipe_formula, value_for_arguments)

    for iterator_in_row in range(len(value_for_arguments)):
        info_input_table.add_row([
            data_element_in_table_implecant[iterator_in_row],
            *value_for_arguments[iterator_in_row]
        ])
        data_for_row = {element_to_move_const[x]: value_for_arguments[iterator_in_row][x]
                        for x in range(len(element_to_move_const))}
        data_for_row = {**data_for_row,
                        'impl': data_element_in_table_implecant[iterator_in_row]
                        }
        d_table_input.append(data_for_row)

    return info_input_table, d_table_input


def bool_method_cnf(data_element_in_table_implecant, element_to_move_const, tipe_formula, value_for_arguments):

    if tipe_formula == 'sdnf':
        for iterator_in_row in range(len(data_element_in_table_implecant)):
            value_for_arguments.append(lab_disunction_form(element_to_move_const,
                                                           data_element_in_table_implecant[iterator_in_row]))
    else:
        for iterator_in_row in range(len(data_element_in_table_implecant)):
            value_for_arguments.append(lab_k_datalable(element_to_move_const,
                                                       data_element_in_table_implecant[iterator_in_row]))


def lab_disunction_form(data_table_konst: list, element_in_table_part: str):
    rezultation_output = list()

    if element_in_table_part[0] == '(' and element_in_table_part[-1] == ')':
        element_in_table_part = element_in_table_part[1:-1]

    for iterator_to_table in range(len(data_table_konst)):
        element_key_count = 0
        lab_dis_for(data_table_konst, element_in_table_part, element_key_count, iterator_to_table, rezultation_output)

    return rezultation_output


def lab_k_datalable(element_input_const: list, element_in_datata_input_with_part: str):

    rezultation_input_formula = list()

    if element_in_datata_input_with_part[0] == '(' and element_in_datata_input_with_part[-1] == ')':
        element_in_datata_input_with_part = element_in_datata_input_with_part[1:-1]

    for iterator_to_move in range(len(element_input_const)):
        key_element_c = 0
        lab_k_for(element_in_datata_input_with_part, element_input_const, iterator_to_move, key_element_c,
                  rezultation_input_formula)

    return rezultation_input_formula


def lab_k_for(element_in_datata_input_with_part, element_input_const, iterator_to_move, key_element_c,
              rezultation_input_formula):
    for iterator in range(len(element_in_datata_input_with_part.split('+'))):
        if not element_in_datata_input_with_part.split('+')[iterator] in \
               element_input_const[iterator_to_move][1:-1].split('+'):
            rezultation_input_formula.append('')
            break
        else:
            key_element_c += 1
    if key_element_c == len(element_in_datata_input_with_part.split('+')):
        rezultation_input_formula.append('X')


def data_for(data_element_to_temp, element_input_in_table, elements_in_row_part, iterator_i, iterator_j):
    for iterator_k in range(len(element_input_in_table)):
        if element_input_in_table[iterator_k]['impl'] == elements_in_row_part[iterator_i]:
            continue
        data_element_to_temp.append(element_input_in_table[iterator_k][iterator_j])


def lab_dis_for(data_table_konst, element_in_table_part, element_key_count, iterator_to_table, rezultation_output):
    for iterator in range(len(element_in_table_part.split('*'))):
        if not element_in_table_part.split('*')[iterator] in data_table_konst[iterator_to_table][1:-1].split('*'):
            rezultation_output.append('')
            break
        else:
            element_key_count += 1
    if element_key_count == len(element_in_table_part.split('*')):
        rezultation_output.append('X')

def datatab_element_proc(element_input_in_table, elements_in_row_part):
    rezultation = list()
    data_element_to_temp = list()
    main_processor_table(data_element_to_temp, element_input_in_table, elements_in_row_part, rezultation)
    return rezultation




