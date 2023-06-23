from prettytable import PrettyTable
from itertools import product
from typing import *
from form_hend import *


def data_repl(datatable, iteratorr, start_index, temp_logic_formula):
    datatable.add_row([
        *iteratorr,
        int(eval(temp_logic_formula)),
        int(eval(temp_logic_formula)),
        start_index,
    ])


def replace_argument_on_number(set_of_values, elem_arg, l_formula_data):
    element_to_count = 0
    for iterator in elem_arg:
        l_formula_data = l_formula_data.replace(iterator, str(set_of_values[element_to_count]))
        element_to_count += 1
    return l_formula_data


def cr_tabl(formula):
    element_arg_to_formula = lements_move_to_form(formula)
    form_log_tocreate_output = hand_for_formila_in_inp(formula)
    table_data = list()
    datatable = PrettyTable()
    datatable.field_names = [
        *element_arg_to_formula, 'f(sknf)', 'f(sdnf)', 'i']
    value_for_arguments: List[Tuple(int)] = product(range(2), repeat=len(element_arg_to_formula))
    start_index = 2 ** (2 ** (len(element_arg_to_formula)) - 1)

    for iteratorr in value_for_arguments:
        temp_logic_formula = form_log_tocreate_output
        temp_logic_formula = replace_argument_on_number(iteratorr, element_arg_to_formula, temp_logic_formula)
        data_repl(datatable, iteratorr, start_index, temp_logic_formula)
        rows_element_data_cr = {element_arg_to_formula[x]: iteratorr[x]
                        for x in range(len(element_arg_to_formula))}
        rows_element_data_cr = {**rows_element_data_cr,
                        'f': int(eval(temp_logic_formula)),
                        'i': start_index,
                        }
        table_data.append(rows_element_data_cr)
        start_index //= 2
    return datatable, table_data