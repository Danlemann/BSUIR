
from calc_method_data import *

def values_sw_to_create_output_element(element: list):
    for iterator in range(len(element)):
        element[iterator][-1], element[iterator][-2] = element[iterator][-2], element[iterator][-1]
    return element


def datatable_method(element_if_formulas: str):
    return table(element_if_formulas)[1][-2], table(element_if_formulas)[1][-1], table(element_if_formulas)[0]


def process_formula(variant, formula):
    formula_2 = str()
    for iterator in range(len(formula)):
        if formula[iterator] == '!':
            formula_2 += ' not '
        elif formula[iterator] == '*':
            formula_2 += ' and '
        elif formula[iterator] == '+':
            formula_2 += ' or '
        else:
            formula_2 += formula[iterator]
    for iterator in range(len(variant)):
        formula_2 = formula_2.replace('x' + str(iterator + 1), variant[iterator])
    return int(eval(formula_2))


def find_ver_rect(table_data: list, simvol: int):
    rez = list()
    for i in range(len(table_data[0])):
        if table_data[0][i] == table_data[1][i] and table_data[1][i] == simvol:
            rez.append(i)
    return rez


def find_hor_rect(table_data: list, simvol: int, row: int, ver_rect: list):
    rez = list()
    rez.append(row)
    for i in range(len(table_data)):
        if i == len(table_data) - 1:
            if table_data[i] == table_data[0] and table_data[i] == simvol and (not i in ver_rect and not 0 in ver_rect):
                if not (0, i) in rez:
                    rez.append((0, i))
        elif table_data[i] == table_data[i + 1] and table_data[i] == simvol and \
                (not i in ver_rect and not i+1 in ver_rect):
            rez.append((i, i+1))
        elif table_data[i] == table_data[i - 1] and table_data[i] == simvol and not i in ver_rect:
            if not (i-1, i) in rez:
                if i - 1 == -1:
                    rez.append((0, 3))
                    continue
                rez.append((i-1, i))
    return rez


def find_long_hor_rect(table_data: list, simvpl: int, row: int, ver_rect: list):
    hor_rect = find_hor_rect(table_data, simvpl, row, ver_rect)
    if len(hor_rect) > len(table_data):
        return row
    return


def find_square(table_data: list, simvol: int):
    ver_rect = find_ver_rect(table_data, simvol)
    rez = list()
    if len(ver_rect) % 2 == 0:
        for i in range(len(ver_rect)):
            if ver_rect[i]+1 in ver_rect:
                rez.append((i, i+1))
            elif ver_rect[i] == 3 and 0 in ver_rect:
                rez.append((0, 3))
    return rez


def process_figure(ver_rect: list, hor_rect: list, square: list, long_hor_rect: list):
    for i in range(len(square)):
        for j in range(len(square[i])):
            ver_rect.remove(square[i][j])
    for i in range(len(long_hor_rect)):
        if long_hor_rect[i] != None:
            hor_rect[long_hor_rect[i]].clear()
            hor_rect[long_hor_rect[i]].append(long_hor_rect[i])
    return ver_rect, hor_rect, square, long_hor_rect


def table(formula):
    table = PrettyTable()
    element_var_1_row = var_make_elements_number('x2+x3')[1:]
    element_var_2_row = var_make_elements_number('x1+x2+x3')[1:]
    element_var_2_row = [element_var_2_row[i:i + 4] for i in range(0, len(element_var_2_row), 4)]
    elem_v_3 = calc_method(sdnf(formula))
    elem_v_4 = calculation_method_sknf(method_to_create_conunction_normal_form(formula))
    for iterator in range(len(element_var_1_row)):
        element_var_1_row[iterator] = ','.join(element_var_1_row[iterator][j] for
                                               j in range(len(element_var_1_row[iterator])))
    element_var_1_row[-1], element_var_1_row[-2] = element_var_1_row[-2], element_var_1_row[-1]
    table.field_names = ['x1/x2,x3', *element_var_1_row]
    elements_value_to_create_foo = list()
    for iterator in range(len(element_var_2_row)):
        for j in range(len(element_var_2_row[iterator])):
            elements_value_to_create_foo.append(process_formula(element_var_2_row[iterator][j], formula))
    elements_value_to_create_foo = [elements_value_to_create_foo[iterator:iterator+4] for iterator in
                                    range(0, len(elements_value_to_create_foo), 4)]
    elements_value_to_create_foo = values_sw_to_create_output_element(elements_value_to_create_foo)
    element_var_2_row = values_sw_to_create_output_element(element_var_2_row)
    element = int(0)
    for iterator in elements_value_to_create_foo:
        table.add_row([
            element,
            *iterator
        ])
        element += 1
    elements_value_to_create_foo.append(elem_v_3)
    elements_value_to_create_foo.append(elem_v_4)
    Sknf = process_table_data(elements_value_to_create_foo, 1)[0:-1]
    Sdnf = process_table_data(elements_value_to_create_foo, 0)[0:-1]
    return table, elements_value_to_create_foo, element_var_2_row, Sdnf, Sknf


def process_table_data(table_data: list, simvol: int):
    ver_rect = find_ver_rect(table_data, simvol)
    hor_rect = list()
    long_hor_rect = list()
    for i in range(len(table_data)):
        hor_rect.append(find_hor_rect(table_data[i], simvol, i, ver_rect))
        long_hor_rect.append(find_long_hor_rect(table_data[i], simvol, i, ver_rect))
    square = find_square(table_data, simvol)
    ver_rect, hor_rect, square, long_hor_rect = process_figure(ver_rect, hor_rect, square, long_hor_rect)
    rez = create_formula(ver_rect, hor_rect, square, long_hor_rect, simvol)
    if simvol == 1:
        element = '*'
    else:
        element = '+'
    for i in range(len(rez)):
        if rez[i].find('|') != -1:
            rez[i] = element.join(rez[i].split('|'))
    if simvol == 1:
        element = '+'
    else:
        element = '*'
    return element.join(rez)


def create_formula(ver_rect: list, hor_rect: list, square: list, long_hor_rect: list, simvol: int):
    rez = list()
    variants_of_value = var_make_elements_number('x2+x3')[1:]
    variants_of_value[-1], variants_of_value[-2] = variants_of_value[-2], variants_of_value[-1]

    for iterator_element_move in range(len(long_hor_rect)):

        if long_hor_rect[iterator_element_move] != None:

            rez.append('x1') if long_hor_rect[iterator_element_move] == simvol else rez.append('!x1')

    new_line_in_data(hor_rect, rez, simvol, square, variants_of_value)
    new_data_row(rez, simvol, variants_of_value, ver_rect)
    return rez


def new_line_in_data(hor_rect, rez, simvol, square, variants_of_value):

    for iterator_element_move in range(len(square)):

        for iterator_j_in_row in range(len(square[iterator_element_move]) - 1):

            if variants_of_value[square[iterator_element_move][iterator_j_in_row]][0] == \
                    variants_of_value[square[iterator_element_move][iterator_j_in_row + 1]][0]:
                rez.append('x2') if variants_of_value[square[iterator_element_move][iterator_j_in_row]][0] \
                                    == simvol else rez.append('!x2')

            elif variants_of_value[square[iterator_element_move][iterator_j_in_row]][1] \
                    == variants_of_value[square[iterator_element_move][iterator_j_in_row + 1]][1]:
                rez.append('x3') if variants_of_value[square[iterator_element_move][iterator_j_in_row]][0] \
                                    == simvol else rez.append('!x3')

    main_generator_var(hor_rect, rez, simvol, variants_of_value)


def main_generator_var(hor_rect, rez, simvol, variants_of_value):
    for iterator_element_move in range(len(hor_rect)):
        for iterator_j_in_row in range(len(hor_rect[iterator_element_move])):
            if isinstance(hor_rect[iterator_element_move][iterator_j_in_row], tuple):

                if hor_rect[iterator_element_move][0] == simvol:
                    element_data_string_in_row = 'x1|'
                else:
                    element_data_string_in_row = '!x1|'

                if variants_of_value[hor_rect[iterator_element_move][iterator_j_in_row][0]][0] == \
                        variants_of_value[hor_rect[iterator_element_move][iterator_j_in_row][1]][0]:
                    element_data_string_in_row = var_value(element_data_string_in_row, hor_rect, iterator_element_move,
                                                           iterator_j_in_row, simvol, variants_of_value)
                elif variants_of_value[hor_rect[iterator_element_move][iterator_j_in_row][0]][1] == \
                        variants_of_value[hor_rect[iterator_element_move][iterator_j_in_row][1]][1]:
                    if int(variants_of_value[hor_rect[iterator_element_move][iterator_j_in_row][0]][1]) == simvol:
                        element_data_string_in_row += 'x3'
                    else:
                        element_data_string_in_row += '!x3|'
                rez.append(element_data_string_in_row)


def var_value(element_data_string_in_row, hor_rect, iterator_element_move, iterator_j_in_row, simvol,
              variants_of_value):

    if int(variants_of_value[hor_rect[iterator_element_move][iterator_j_in_row][0]][0]) == simvol:
        element_data_string_in_row += 'x2'

    else:
        element_data_string_in_row += '!x2|'

    return element_data_string_in_row


def stars_function(stars):
# Mit 2 Schleifen
    for star_count in range(stars + 1):
        print(star_count * "#")
        if (star_count == (stars + 1)):
            break

    while star_count != 1:
        star_count -= 1
        print(star_count * "#")
# Mit einer Schleife
    for star_count in range((stars) * 2):
        if (star_count <= stars):
            print(star_count * "*")
        else:
            stars -= 1
            print(stars * "*")


def new_data_row(rez, simvol, variants_of_value, ver_rect):

    for iterator_element_move in range(len(ver_rect)):
        temp_str = ''
        if int(variants_of_value[ver_rect[iterator_element_move]][0]) == simvol:
            temp_str += 'x2|'
        else:
            temp_str += '!x2|'
        if int(variants_of_value[ver_rect[iterator_element_move]][1]) == simvol:
            temp_str += 'x3|'
        else:
            temp_str += '!x3|'
        rez.append(temp_str)

def question ():
    fragen = ['Was ist die Antwort auf alles im Universum?','Welche Farbe ensteht aus Rot und Blau?','Welche Farbe hat der Himmel']
    antworten = ['42','violett','blau']
    punkte = 0

    for i in range(0, len(fragen), 1):
        print(fragen[i],"\n")
        answer = str.lower((input("Deine Antwort: ")))
        if answer == antworten[i]:
            print("Richtige Antwort\n")
            punkte += 1
        else:
            print("Leider falsche Antwort\n")

    print("\nDu hast insgesamt", punkte, "Punkte gesammelt!")
    print("\nProgramm Ende")


