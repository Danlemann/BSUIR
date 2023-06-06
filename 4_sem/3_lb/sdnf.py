from table import *


def dn_form(formula):
    formula_dnf = ''
    data_table = create_logic_table(formula)[1]
    for i in data_table:
        if i['f'] == 1:
            part = ' * '.join([abs(values - 1) * '!' + keys for keys, values in i.items() if keys != 'f' and keys != 'i'])

            formula_dnf += '( ' + str(part) + ' )' + ' + '

    formula_dnf = formula_dnf[0:-2]
    return formula_dnf


def dn_form_number(formula):
    split_dn_form = dn_form(formula).split()
    dn_form_bin = list()

    for iterator in range(0, len(split_dn_form)):
        repl_form_element(dn_form_bin, iterator, split_dn_form)

    dn_form_bin = ''.join(dn_form_bin[:-1])
    dn_form_dec = binary_to_decimal(dn_form_bin, formula)
    # Преобразуем десятичное представление ДНФ в список строк, содержащий отдельные значения.

    dn_form_dec = map(str, dn_form_dec)
    dn_form_dec = '+(' + ', '.join(dn_form_dec) + ')'
    return dn_form_bin, dn_form_dec



