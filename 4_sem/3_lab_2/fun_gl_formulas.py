
from dnf_knf_method import *


def fisunction_normal_form_glu(element_row_parts: list):
    output_resultation = list()
    move_in_datatable_c = int(0)
    element_parts_data_look = list()
    new_part_create_whith_data(element_row_parts, element_parts_data_look)

    move_in_datatable_c = move_d(element_parts_data_look, element_row_parts, move_in_datatable_c, output_resultation)

    output_resultation = elem_kof_datatable(element_parts_data_look, element_row_parts, move_in_datatable_c,
                                            output_resultation)
    return output_resultation


def elem_kof_datatable(element_parts_data_look, element_row_parts, move_in_datatable_c, output_resultation):

    if not element_parts_data_look[-1][1] and not element_row_parts[-1] in output_resultation:
        output_resultation.append(element_parts_data_look[-1][0])

    if move_in_datatable_c >= 2:
        output_resultation = fisunction_normal_form_glu(output_resultation)

    return output_resultation


def meinSort(meineListe):
    for i in range(len(meineListe)):
        minindex = i
        for j in range(minindex + 1, len(meineListe)):
            if meineListe[minindex] > meineListe[j]:
                minindex = j

        meineListe[i], meineListe[minindex] = meineListe[minindex], meineListe[i]
    return meineListe


def move_d(element_parts_data_look, element_row_parts, move_in_datatable_c, output_resultation):
    for iterator_i_element in range(len(element_parts_data_look) - 1):
        move_in_datatable_c = iterator_cicle_to_move_elem_in_formulas(
            move_in_datatable_c, iterator_i_element, element_row_parts, element_parts_data_look, output_resultation)
    return move_in_datatable_c


def iterator_cicle_to_move_elem_in_formulas(change_elem, iterator_i_element, parts, parts_whith_check, rez):
    for iterator_j_to_cr_ddat in range(iterator_i_element + 1, len(parts_whith_check)):
        element_1_part = set(row_cr(parts_whith_check[iterator_i_element][0]).split('*'))
        element_2_part = set(row_cr(parts_whith_check[iterator_j_to_cr_ddat][0]).split('*'))

        if len(element_1_part) != len(element_2_part):
            continue

        data_row_comm = element_1_part.intersection(element_2_part)

        change_elem = part_check(change_elem, data_row_comm, element_1_part, element_2_part, iterator_i_element,
                                 iterator_j_to_cr_ddat, parts_whith_check, rez)

    not_elem_in_data(iterator_i_element, parts, parts_whith_check, rez)

    return change_elem


def not_elem_in_data(iterator_i_element, parts, parts_whith_check, rez):
    if not parts_whith_check[iterator_i_element][1] and not parts[iterator_i_element] in rez:
        rez.append(parts_whith_check[iterator_i_element][0])


def part_check(change_elem, data_row_comm, element_1_part, element_2_part, iterator_i_element, iterator_j_to_cr_ddat,
               parts_whith_check, rez):
    if len(data_row_comm) == len(element_1_part) - 1 and data_row_in_mass_check(element_1_part, element_2_part, data_row_comm):
        parts_whith_check[iterator_i_element][1] = True
        parts_whith_check[iterator_j_to_cr_ddat][1] = True
        change_elem += 1
        new_part = dataelem_gl(element_1_part, element_2_part, data_row_comm)
        rez.append('*'.join(new_part))
    return change_elem


def new_part_create_whith_data(parts, parts_whith_check):
    for iterator_i_element in range(len(parts)):
        parts_whith_check.append(create_element_data_table_temp(parts[iterator_i_element]))


def datatable_element_new_parts(common, different, new_element_with_dsata):
    for element_one in range(len(common)):
        new_element_with_dsata.append(common[element_one])

    for element_one in range(len(different)):
        new_element_with_dsata.append(different[element_one])


def gluing_sknf(parts: list):

    rezultation_output_data = list()
    rows_change_data = int(0)
    par_check_d = list()

    for iterator_rows_in_table in range(len(parts)):
        par_check_d.append(create_element_data_table_temp(parts[iterator_rows_in_table]))

    for iterator_rows_in_table in range(len(par_check_d) - 1):

        for itearor_j in range(iterator_rows_in_table + 1, len(par_check_d)):
            element_1_part = set(row_cr(par_check_d[iterator_rows_in_table][0]).split('+'))
            element_2_part = set(row_cr(par_check_d[itearor_j][0]).split('+'))

            if len(element_1_part) != len(element_2_part):
                continue

            element_data_row_comm = element_1_part.intersection(element_2_part)

            rows_change_data = data_chek_part(element_1_part, element_2_part, element_data_row_comm, itearor_j,
                                              iterator_rows_in_table, par_check_d, rezultation_output_data,
                                              rows_change_data)

        if not par_check_d[iterator_rows_in_table][1] and not parts[iterator_rows_in_table] in rezultation_output_data:
            rezultation_output_data.append(parts[iterator_rows_in_table])

    rezultation_output_data = ifel_part(par_check_d, parts, rezultation_output_data, rows_change_data)

    return rezultation_output_data


def ifel_part(par_check_d, parts, rezultation_output_data, elem_r_check):

    if not par_check_d[-1][1] and not parts[-1] in rezultation_output_data:
        rezultation_output_data.append(par_check_d[-1][0])

    if elem_r_check >= 2:
        rezultation_output_data = gluing_sknf(rezultation_output_data)

    return rezultation_output_data


def data_chek_part(element_1_part, element_2_part, element_data_row_comm, itearor_j, iterator_rows_in_table,
                   par_check_d, rezultation_output_data, rows_change_data):
    if len(element_data_row_comm) == len(element_1_part) - 1 \
            and data_row_in_mass_check(element_1_part, element_2_part, element_data_row_comm):
        par_check_d[iterator_rows_in_table][1] = True
        par_check_d[itearor_j][1] = True
        rows_change_data += 1
        new_part = dataelem_gl(element_1_part, element_2_part, element_data_row_comm)
        rezultation_output_data.append('+'.join(new_part))
    return rows_change_data


def data_row_in_mass_check(element_part_1: set, element_part_2: set, datacomm: set):

    with_element_differ = list(element_part_1.union(element_part_2) - datacomm)

    for iterator in range(len(with_element_differ) - 1):
        if str(with_element_differ[iterator]) == str('!' + with_element_differ[iterator+1])\
                or str('!' + with_element_differ[iterator]) == str(
                with_element_differ[iterator+1]):
            return True

    return False


def row_cr(datatable_element_t: str):

    if datatable_element_t[0] == '(' and datatable_element_t[-1] == ')':
        return ecwiwal_row(datatable_element_t)

    else:
        return datatable_element_t


def ecwiwal_row(datatable_element_t):
    return datatable_element_t[1:-1]


def create_element_data_table_temp(element_p: list):
    datatable_element_information_in_binary = list()
    datatable_element_information_in_binary.append(element_p)
    datatable_element_information_in_binary.append(False)
    return datatable_element_information_in_binary


def dataelem_gl(element_part_1: set, element_part_2: set, data_comm_rez: set):

    data_row_diferrent_with_element = list(set(element_part_1.union(element_part_2)) - data_comm_rez)

    for iterator_element_k in range(len(data_row_diferrent_with_element) - 1):
        range_diff(data_row_diferrent_with_element, iterator_element_k)

    data_new_part = list()
    data_comm_rez = list(data_comm_rez)

    datatable_element_new_parts(data_comm_rez, data_row_diferrent_with_element, data_new_part)

    return data_new_part


def range_diff(data_row_diferrent_with_element, iterator_element_k):
    for iterator_elem_t in range(iterator_element_k + 1, len(data_row_diferrent_with_element)):
        if str(data_row_diferrent_with_element[iterator_element_k]) == \
                str('!' + data_row_diferrent_with_element[iterator_elem_t]) or \
                str('!' + data_row_diferrent_with_element[iterator_element_k]) == str(
            data_row_diferrent_with_element[iterator_elem_t]):
            data_row_diferrent_with_element.remove(data_row_diferrent_with_element[iterator_elem_t])
            data_row_diferrent_with_element.remove(data_row_diferrent_with_element[iterator_element_k])


def getSimplified(operator, literals, current):
    result = []
    result.append(operator)

    # If the literal length is 1 append the literal else recursively call for simplification
    if len(literals) == 1:
        result.append(literals[0])
    else:
        result.append(getSimplified(operator, literals[0:len(literals) - 1], literals[len(literals) - 1]))

    # append the current
    result.append(current)

    # return simplified logic
    return result


def propogateNOT(logic):
    result = []

    # Checking if the inward logic is OR then append AND
    if (logic[1][0] == 'or'):
        result.append('and')
    # Chicking if inward logic is AND then append OR
    elif (logic[1][0] == 'and'):
        result.append('or')
    # Checking if inward logic is NOT then return the logic alone
    elif (logic[1][0] == 'not'):
        return logic[1][1]

    # For all arguments of the inner list
    for i in range(1, len(logic[1])):
        # check if the first argument is another list
        if len(logic[1][i]) != 1:
            # recursively call to propogate not further inwards
            result.append(propogateNOT(['not', logic[1][i]]))
        else:
            # else append the negation of the single element
            result.append(['not', logic[1][i]])

    return result


def removeDuplicates(logic):
    # Check if the logic is not a literal or a not
    if len(logic) > 2:
        result = []
        result.append(logic[0])
        result.append(logic[1])

        for i in range(2, len(logic)):
            # Only add the logic to the list if its equivalent is not already present

                result.append(logic[i])

        # check if the cleaned clause is just of size 2
        # Case of the comment above
        if len(result) == 2:
            result = result[1]

        return result
    else:

        return logic


def parseCleanUp(logic):
    # Clean the logic


    # For all the attributes in the logic repeat the process recursively
    for i in range(1, len(logic)):
        if len(logic[i]) > 1:
            logic[i] = parseCleanUp(logic[i])
    # return the final clean logic
    return logic



