
def create_series_with_id(series):

    print('{}|{}|{}|{}|{}| {}'.format(
        str(series[0]).center(4),
        series[key_index].center(20),
        str(series[id_vertical]).center(6),
        str(series[id_horizontal]).center(7),
        str(series[id_collission]).center(6),
        series[information_id]
    ))


def create_full_table(vert_hor_tab):

    print('\n №  |        TERM        |   V  | h(V)  |  C   | DEFINITION''\n'
          '----+--------------------+------+-------+------+------------------------------------------------------------'
          '-----------------------------------------------------')

    for iterator in range(len(vert_hor_tab)):
        create_series_with_id(vert_hor_tab[iterator])
        print(
            '----+--------------------+------+-------+------+----------------------------------------------------------'
            '-------------------------------------------------------')


def element_calculate_value(value_k):

    character_1 = ord(value_k[0]) - ord('a')
    character_2 = ord(value_k[1]) - ord('a')
    final_value_to_generate = character_1 * alphabet_len + character_2

    return final_value_to_generate


def find_empty_value_in_table(table):

    for rows_id in range(len(table)):

        if table[rows_id][key_index] == '':
            return rows_id

        if table[rows_id][key_index].lower() == '':
            return rows_id

    return -1


def find_empty_value_in_table_extended(hash_t):
    for id_row_element in range(len(hash_t)):

        if hash_t[id_row_element][key_index] == '':
            return id_row_element

        if hash_t[id_row_element][key_index].lower() == '':
            return id_row_element

        if hash_t[id_row_element][key_index] == '':
            return id_row_element

        if hash_t[id_row_element][key_index].lower() == '':
            return id_row_element

    return -1


def calc_new_address(numeric_value_corresponding_element):

    elem_address = numeric_value_corresponding_element % number_of_cells_in_table

    return elem_address


def new_element_add(hash_table, id_k, information_of_rows):

    value_of_element = element_calculate_value(id_k)
    series_address = calc_new_address(value_of_element)
    handle_collision_and_update_table(series_address, id_k, information_of_rows, hash_table, value_of_element)


def handle_collision_and_update_table(elem_pass, id_k, additional_info, hash_tabl, element_value):

    if hash_tabl[elem_pass][key_index] == '':
        hash_tabl[elem_pass] = [elem_pass, id_k, element_value, elem_pass, additional_info, '']

    elif hash_tabl[elem_pass][id_horizontal] != elem_pass:
        update_and_relocate_row(elem_pass, additional_info, id_k, hash_tabl, element_value)

    else:
        insert_and_update_table(elem_pass, additional_info, id_k, hash_tabl, element_value)


def insert_and_update_table(address, information, key, hash_table, value):

    element_id = find_empty_value_in_table(hash_table)
    last = last_elem_find(hash_table, address)

    hash_table[last][id_collission] = element_id
    hash_table[element_id] = [element_id, key, value, address, information, '']


def update_and_relocate_row(element_address, informterm, key, hash_t, value):

    main_ky = hash_t[element_address][key_index]
    other_info = hash_t[element_address][key_index]

    del_row_with_elements(main_ky, hash_t)
    hash_t[element_address] = [element_address, key, value, element_address, informterm, '']
    new_element_add(hash_t, main_ky, other_info)


def last_elem_find(hash_tab, element_address):

    if hash_tab[element_address][id_collission] == '':
        return element_address

    else:
        return last_elem_find(hash_tab, hash_tab[element_address][id_collission])


def find_previous(hash_tabl, address):

    for iterator in range(number_of_cells_in_table):

        if hash_tabl[iterator][id_collission] == address:
            return iterator


def search_for_the_desired_element(key, input_hash_table, addr_of_element=''):

    if addr_of_element == '':
        element_val = element_calculate_value(key)
        addr_of_element = calc_new_address(element_val)

    if input_hash_table[addr_of_element][key_index] == key:
        return input_hash_table[addr_of_element]

    if input_hash_table[addr_of_element][id_collission] != '':
        return search_for_the_desired_element(key, input_hash_table,
                                              addr_of_element=input_hash_table[addr_of_element][id_collission])

    return None


def del_row_with_elements(el_ky, hash_table, address=''):

    if address == '':
        value = element_calculate_value(el_ky)
        address = calc_new_address(value)

    if hash_table[address][key_index] == el_ky:
        pass_through_the_table(address, hash_table)

    else:
        del_row_with_elements(el_ky, hash_table, address=hash_table[address][id_collission])


def pass_through_the_table(address_elem, hash_table_check):

    if hash_table_check[address_elem][id_collission] == '' and \
            address_elem == hash_table_check[address_elem][id_horizontal]:
        hash_table_check[address_elem] = [address_elem, '', '', '', '', '']

    elif hash_table_check[address_elem][id_collission] != '':
        relocate_collision_entry(address_elem, hash_table_check)

    else:
        prev_index = find_previous(hash_table_check, address_elem)

        hash_table_check[prev_index][id_collission] = hash_table_check[address_elem][id_collission]
        hash_table_check[address_elem] = [address_elem, '', '', '', '', '']


def process_data_and_insert_into_table():

    global main_key
    global m_info
    global current_row

    for line in lines_with_data:
        main_key, m_info = line.split(', ')
        m_info = m_info.replace('\n', '')
        element_val = element_calculate_value(main_key)
        address = calc_new_address(element_val)
        current_row = [address, main_key, element_val, address, m_info, '']

        if hash_table[address][key_index] == '':

            hash_table[address] = current_row
        else:
            collisions.append(current_row)


def handle_collisions_and_create_full_table():

    global current_row

    for current_row in collisions:
        new_element_add(hash_table, current_row[key_index], current_row[information_id])

    create_full_table(hash_table)


def hash_table_insert(hash_table, key):

    hashed_key = hash(key)
    index = hashed_key % hash_table.capacity
    existing_node = hash_table.storage[index]

    if existing_node:
        if existing_node.key == key:
            print("You are overwriting an existing el_ky's value.")


def relocate_collision_entry(address_elem, hash_table_check):

    step_index = hash_table_check[address_elem][id_collission]
    hash_table_check[address_elem] = hash_table_check[step_index]
    hash_table_check[address_elem][0] = address_elem
    hash_table_check[step_index] = [step_index, '', '', '', '', '']

def handle_search_and_create_table(search_term):

    if search_term == None:
        print('The specified term was not found in the dictionary.')

    else:
        create_full_table([search_term])

def add_new_term_to_hash_table():

    global main_key, m_info
    main_key = input('\nEnter a new definition: ')

    if search_for_the_desired_element(main_key, hash_table) != None:
        print('The specified term already exists in the dictionary.')

    else:
        m_info = input('definition: ')
        new_element_add(hash_table, main_key, m_info)


def create_hash_table():

    for iterator in range(number_of_cells_in_table):
        hash_table.append([iterator, '', '', '', '', ''])


def stap_case():

    global main_key, m_info
    match main_case:

        case '1':
            create_full_table(hash_table)
        case '2':
            add_new_term_to_hash_table()
        case '3':
            main_key = input('\nEnter the desired definition: ')

            search_term = search_for_the_desired_element(main_key, hash_table)
            handle_search_and_create_table(search_term)
        case '4':
            main_key = input('\nEnter the definition to be removed: ')
            del_row_with_elements(main_key, hash_table)


number_of_cells_in_table = 35
id_horizontal = 3
alphabet_len = 26

information_id = 4
id_vertical = 2
key_index = 1
id_collission = 5

hash_table = []

create_hash_table()

information = open('transport.txt')
lines_with_data = information.readlines()

collisions = []

process_data_and_insert_into_table()

handle_collisions_and_create_full_table()

while True:

    main_case = input('\n(1): display a hash_table_check\t|\t(2): add definition\t|\t(3): '
                'find  definition\t|\t(4): delete definition\n')

    stap_case()

