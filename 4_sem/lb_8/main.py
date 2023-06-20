
import random


class create_matrix:

    MATRIX_SIZE = 16

    def __init__(self):
        self.dynamic_matrix_handler = [[0] * self.MATRIX_SIZE for _ in range(self.MATRIX_SIZE)]

    def __setitem__(self, multiple_index_values, isolated_value_instance):
        if isinstance(multiple_index_values, tuple):
            single_row_entry, single_column_entry = multiple_index_values
            self.dynamic_matrix_handler[single_row_entry][single_column_entry] = isolated_value_instance
        else:
            self.dynamic_matrix_handler[multiple_index_values] = isolated_value_instance

    def __getitem__(self, multiple_index_values):
        if isinstance(multiple_index_values, tuple):
            single_row_entry, single_column_entry = multiple_index_values
            return self.dynamic_matrix_handler[single_row_entry][single_column_entry]
        else:
            return self.dynamic_matrix_handler[multiple_index_values]

    def matrix_entries_fll(self):
        for iterator in range(self.MATRIX_SIZE):
            for iterator_j in range(self.MATRIX_SIZE):
                self.dynamic_matrix_handler[iterator][iterator_j] = random.randint(0, 1)

    def visualize_mx(self):
        for matrix_row in self.dynamic_matrix_handler:
            print(' '.join(str(element) for element in matrix_row))

    @staticmethod
    def interchange_vertical_sequence(complex_matrix_structure: 'create_matrix') -> 'create_matrix':
        revamped_matrix_construction = create_matrix()
        for iterator in range(revamped_matrix_construction.MATRIX_SIZE):
            for iterator_j in range(revamped_matrix_construction.MATRIX_SIZE):
                modernized_j_component = iterator_j + iterator
                if modernized_j_component >= revamped_matrix_construction.MATRIX_SIZE:
                    modernized_j_component = iterator_j + iterator - revamped_matrix_construction.MATRIX_SIZE
                revamped_matrix_construction[modernized_j_component, iterator] = \
                    complex_matrix_structure[iterator, iterator_j]
        return revamped_matrix_construction

    @staticmethod
    def acquire_vertical_expression(versatile_matrix_representation: 'create_matrix', individual_index_value):
        single_wd = []
        for iterator in range(versatile_matrix_representation.MATRIX_SIZE):
            supplementary_i_component = iterator + individual_index_value
            if supplementary_i_component >= versatile_matrix_representation.MATRIX_SIZE:
                supplementary_i_component -= versatile_matrix_representation.MATRIX_SIZE
            single_wd.append(versatile_matrix_representation[supplementary_i_component, individual_index_value])
        return single_wd
    



def method_2x_or_f(introductory_value_elements, next_elements_value):
    if not introductory_value_elements and next_elements_value:
        return next_elements_value
    elif not next_elements_value and introductory_value_elements:
        return introductory_value_elements
    elif introductory_value_elements and not next_elements_value:
        return introductory_value_elements
    elif next_elements_value and not introductory_value_elements:
        return next_elements_value
    else:
        return introductory_value_elements



def method_once_no_f4(introductory_value_elements, next_elements_value):
    return not introductory_value_elements and next_elements_value


def method_0_not_f11(introductory_value_elements, next_elements_value):
    return introductory_value_elements or not next_elements_value


def transformative_operation_f4(introductory_value_elements, next_elements_value):
    transformation_res = []
    for iterator_x in range(len(introductory_value_elements)):
        transformation_res.append(int(method_once_no_f4(introductory_value_elements[iterator_x]
                                                        , next_elements_value[iterator_x])))
    return transformation_res


def method_2x_or_f6(introductory_value, subsequent_val):
    return (not introductory_value and subsequent_val) or (not subsequent_val and introductory_value)


def transformative_operation_f6(introductory_value_elements, next_elements_value):
    transformation_res = []
    for iterator_x in range(len(introductory_value_elements)):
        transformation_res.append(int(method_2x_or_f(introductory_value_elements[iterator_x],
                                                     next_elements_value[iterator_x])))
    return transformation_res


def transformative_operation_f9(introductory_value_elements, next_elements_value):
    transformation_res = []
    for iterator_x in range(len(introductory_value_elements)):
        transformation_res.append(int(and_and_f9_f(introductory_value_elements[iterator_x],
                                                   next_elements_value[iterator_x])))
    return transformation_res


def proc_element_summation(element_transformation, introductory_value_elements, iterator_x, next_elements_value,
                           summation_two_elements_res):
    if introductory_value_elements[iterator_x] + next_elements_value[iterator_x] + element_transformation == 0:
        summation_two_elements_res[iterator_x + 1] = 0
    if introductory_value_elements[iterator_x] + next_elements_value[iterator_x] == 1:
        summ_two_1(element_transformation, iterator_x, summation_two_elements_res)
    if introductory_value_elements[iterator_x] + next_elements_value[iterator_x] == 2:
        element_transformation = sum_two_2(element_transformation, iterator_x, summation_two_elements_res)
    return element_transformation


def method_2x_and_f9(introductory_value_elements, next_elements_value):
    return (introductory_value_elements and next_elements_value) or \
        (not next_elements_value and not introductory_value_elements)

def transformative_operation_f11(introductory_value_elements, next_elements_value):
    transformation_res = []
    for iterator_x in range(len(introductory_value_elements)):
        transformation_res.append(int(method_0_not_f11(introductory_value_elements[iterator_x],
                                                       next_elements_value[iterator_x])))
    return transformation_res


def comprehensive_search(main_matrx: create_matrix, id_elem):
    print(main_matrx[id_elem])


def attribute_setter(main_matrix: create_matrix, elements_val, elements_id):
    main_matrix[elements_id] = elements_val


def and_and_f9_f(introductory_value_elements, next_elements_value):
    if introductory_value_elements and next_elements_value:
        return True
    elif not next_elements_value and not introductory_value_elements:
        return False
    elif introductory_value_elements and not next_elements_value:
        return False
    elif next_elements_value and not introductory_value_elements:
        return False
    else:
        return False


def sum_2_elements_in_matrix(introductory_value_elements, next_elements_value):

    summation_two_elements_res = [0, 0, 0, 0, 0]
    element_transformation = 0

    for iterator_x in range(len(introductory_value_elements) - 1, -1, -1):
        element_transformation = proc_element_summation(element_transformation, introductory_value_elements, iterator_x,
                                                        next_elements_value, summation_two_elements_res)
    if element_transformation == 1:
        summation_two_elements_res[0] = 1
    return summation_two_elements_res


def sum_two_2(element_transformation, iterator_x, summation_two_elements_res):

    if element_transformation == 1:
        summation_two_elements_res[iterator_x + 1] = 1

    if element_transformation == 0:
        element_transformation = 1
        summation_two_elements_res[iterator_x + 1] = 0

    return element_transformation


def summ_two_1(element_transformation, iterator_x, summation_two_elements_res):

    if element_transformation == 0:
        summation_two_elements_res[iterator_x + 1] = 1

    if element_transformation == 1:
        summation_two_elements_res[iterator_x + 1] = 0


def element_val_1(accumulation, individual_value, iterator_x, matrx_arr):
    for iterator_y in range(len(matrx_arr)):
        if individual_value == 1:
            if matrx_arr[iterator_y][iterator_x] != 1:
                accumulation[iterator_y] = 0


def summation_in_row(check_key, matrix_arr):
    for iterator_x in range(matrix_arr.MATRIX_SIZE):
        if check_key[:3] == matrix_arr[iterator_x][:3]:
            first_w = matrix_arr[iterator_x][3:7]
            second_w = matrix_arr[iterator_x][7:11]
            print()
            matrix_arr[iterator_x][11:16] = sum_2_elements_in_matrix(first_w, second_w)

    
def find_maximum(matrx_arr):

    finding_maximum_element = []
    accumulation = [1 for _ in range(len(matrx_arr))]

    for iterator_x in range(len(matrx_arr[0])):
        individual_value = 0

        individual_value = arr_1_1(accumulation, individual_value, iterator_x, matrx_arr)

        element_val_1(accumulation, individual_value, iterator_x, matrx_arr)

        for iterator_y in range(len(matrx_arr)):
            if individual_value == 1 and accumulation[iterator_y] == 1:
                finding_maximum_element.append(1)
                break

            if individual_value == 0 and accumulation[iterator_y] == 1:
                finding_maximum_element.append(0)
                break

    return finding_maximum_element


def arr_1_1(accumulation, individual_value, iterator_x, matrx_arr):

    for iterator_y in range(len(matrx_arr)):
        if matrx_arr[iterator_y][iterator_x] == 1 and accumulation[iterator_y] == 1:
            individual_value = 1
            break
    return individual_value


def search_min_element(arrange_answ, matx_array):
    while len(matx_array) > 0:
        minimal_flag = find_min(matx_array)
        arrange_answ.append(minimal_flag)
        matx_array.remove(minimal_flag)


def search_max_element(arrange_answ, matx_array):
    while len(matx_array) > 0:
        maximum_flag = find_maximum(matx_array)
        arrange_answ.append(maximum_flag)
        matx_array.remove(maximum_flag)


def find_min(array):

    finding_result = []
    accumulation = [1 for _ in range(len(array))]

    for iterator_x in range(len(array[0])):
        elements_val_to_move = 1

        for iterator_y in range(len(array)):
            if array[iterator_y][iterator_x] == 0 and accumulation[iterator_y] == 1:
                elements_val_to_move = 0
                break

        for iterator_y in range(len(array)):
            if elements_val_to_move == 0:
                if array[iterator_y][iterator_x] != 0:
                    accumulation[iterator_y] = 0

        for iterator_y in range(len(array)):
            if elements_val_to_move == 0 and accumulation[iterator_y] == 1:
                finding_result.append(0)
                break

            if elements_val_to_move == 1 and accumulation[iterator_y] == 1:
                finding_result.append(1)
                break

    return finding_result


def print_proc_f4(element_id_1, element_id_2, matrix_arr):
    print(matrix_arr[element_id_1])
    print(matrix_arr[element_id_2])
    matrix_arr[element_id_2] = transformative_operation_f4(matrix_arr[element_id_1], matrix_arr[element_id_2])
    print(matrix_arr[element_id_2])


def arrange_in_order(array, elements_key_max_min):

    arrange_answ = []
    matx_array = array[:]

    if elements_key_max_min == 'min':
        search_min_element(arrange_answ, matx_array)

    if elements_key_max_min == 'max':
        search_max_element(arrange_answ, matx_array)

    return arrange_answ


def display_list(matrix_tr_array):

    for iterator in range(len(matrix_tr_array)):
        print(matrix_tr_array[iterator])


def log_handling(element_id_1, element_id_2, procedure, matrix_arr):

    if procedure == 'f4':
        print_proc_f4(element_id_1, element_id_2, matrix_arr)

    if procedure == 'f9':
        matrix_arr[element_id_2] = transformative_operation_f9(matrix_arr[element_id_1], matrix_arr[element_id_2])

    if procedure == 'f6':
        matrix_arr[element_id_2] = transformative_operation_f6(matrix_arr[element_id_1], matrix_arr[element_id_2])

    if procedure == 'f11':
        matrix_arr[element_id_2] = transformative_operation_f11(matrix_arr[element_id_1], matrix_arr[element_id_2])




row_value_to_replacement = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_element_to_diagonal_search = 0
index_element_to_search = 1
index_row_to_repl_value = 0
index_row = [0, 0, 1]
flag_to_arrange_in_order = 'max'
advanced_matrix_transformer = create_matrix()
advanced_matrix_transformer.matrix_entries_fll()
advanced_matrix_transformer.visualize_mx()

vertical_matrix = create_matrix.interchange_vertical_sequence(advanced_matrix_transformer)

while True:

    print("(1) >> Отобразить матрицу.")
    print("(2) >> Отобразить матрицу в диагональном виде.")
    print("(3) >> Вывести элемент из диагональной матрицы по индексу.")
    print("(4) >> Вывести элемент из прямой матрицы по индексу.")
    print("(5) >> Установеть значение элемента по индексу .")
    print("(6) >> Сортировать матрицу.")
    print("(7) >> Найти сумму элемента по ключу.")
    print("(8) >> ( f4 | f6 | f9 | f11 ).")

    operation = input("Введите номер операции:")

    if operation == "1":
        advanced_matrix_transformer.visualize_mx()

    elif operation == "2":
        vertical_matrix.visualize_mx()

    elif operation == "3":

        print(create_matrix.acquire_vertical_expression(vertical_matrix, index_element_to_diagonal_search))
    elif operation == "4":

        comprehensive_search(advanced_matrix_transformer, index_element_to_search)

    elif operation == "5":
        attribute_setter(advanced_matrix_transformer, row_value_to_replacement, index_row_to_repl_value)

    elif operation == "6":

        display_list(arrange_in_order(advanced_matrix_transformer, flag_to_arrange_in_order))

    elif operation == "7":

        summation_in_row(index_row, advanced_matrix_transformer)
        advanced_matrix_transformer.visualize_mx()

    elif operation == "8":
        print('Operation (f4)\n')
        log_handling(1, 2, 'f4', advanced_matrix_transformer)
        print('\n')
        advanced_matrix_transformer.visualize_mx()
        print('\n')
        print('Operation (f6)\n')
        log_handling(1, 3, 'f6', advanced_matrix_transformer)
        advanced_matrix_transformer.visualize_mx()
        print('\n')
        print('Operation (f9)\n')
        log_handling(1, 4, 'f9', advanced_matrix_transformer)
        advanced_matrix_transformer.visualize_mx()
        print('\n')
        print('Operation (f11)\n')
        log_handling(1, 5, 'f11', advanced_matrix_transformer)
        advanced_matrix_transformer.visualize_mx()