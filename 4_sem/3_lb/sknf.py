from table import *


def cn_form_number(formula):
    split_knf = cn_form(formula).split()
    cn_binary_form = list()
    split_numbers(cn_binary_form, split_knf)
    cn_binary_form = ''.join(cn_binary_form[:-1])
    cn_form_dec = binary_to_decimal(cn_binary_form, formula)
    cn_form_dec = map(str, cn_form_dec)
    cn_form_dec = '*(' + ', '.join(cn_form_dec) + ')'

    return cn_binary_form, cn_form_dec


def split_numbers(cn_form_bin, cn_form_split):
    for iterator in range(0, len(cn_form_split)):

        if cn_form_split[iterator][0] == 'x':
            cn_form_bin.append('0')
        elif cn_form_split[iterator][0] == ')':
            cn_form_bin.append('*')

def cn_form(formula):

    formula_cn_form = ''
    data_table = create_logic_table(formula)[1]
    formula_cn_form = data_table_iteration(data_table, formula_cn_form)

    return formula_cn_form

