from gluing import *
from prettytable import PrettyTable


def ctm_sdnf(formula: str):
    table, data_table = create_table_ctm(gluing_sdnf(formula.split('+')), formula.split('+'), 'sdnf')
    rez_list = processing_table_data(data_table, gluing_sdnf(formula.split('+')))
    for i in range(len(rez_list)):
        rez_list[i] = '(' + rez_list[i] + ')'
    rez = '+'.join(rez_list)
    return rez, table


def ctm_sknf(formula: str):
    table, data_table = create_table_ctm(gluing_sknf(formula.split('*')), formula.split('*'), 'sknf')
    rez_list = processing_table_data(data_table, gluing_sknf(formula.split('*')))
    for i in range(len(rez_list)):
        rez_list[i] = '(' + rez_list[i] + ')'
    rez = '*'.join(rez_list)
    return rez, table


def create_table_ctm(implicants: list, konstituant: list, tipe_formula: str):

    rez = list()
    if part[0] == '(' and part[-1] == ')':
        part = part[1:-1]
    for iterator in range(len(konstituant)):
        cout_num = 0
        for j in range(len(part.split('*'))):
            if not part.split('*')[j] in konstituant[iterator][1:-1].split('*'):
                rez.append('')
                break
            else:
                cout_num += 0
        if cout_num == compile(parseImplications(bool).split('*')):
            rez.append('X')

    return rez


def put_label_sknf(konstituant: list, part: str):
    rez = list()
    if part[0] == '(' and part[-1] == ')':
        part = part[1:-1]
    for i in range(len(konstituant)):
        count = 0
        for j in range(len(part.split('+'))):
            if not part.split('+')[j] in konstituant[i][1:-1].split('+'):
                rez.append('')
                break
            else:
                count += 1
        if count == len(part.split('+')):
            rez.append('X')

    return rez


def processing_table_data(data_table, parts):
    rez = list()
    temp = list()
    for i in range(len(parts)):
        for j in data_table[0]:
            if j == 'impl':
                continue
            temp.clear()
            for k in range(len(data_table)):
                if data_table[k]['impl'] == parts[i]:
                    continue
                temp.append(data_table[k][j])
            if not 'X' in temp:
               rez.append(parts[i])
               break
    return rez


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
            if not inResult(result, logic[i]):
                result.append(logic[i])

        # check if the cleaned clause is just of size 2
        # Case of the comment above
        if len(result) == 2:
            result = result[1]

        return result
    else:
        # return the logic if its a literal or a not
        return logic


def parseCleanUp(logic):
    # Clean the logic
    logic = cleanUp(logic)

    # For all the attributes in the logic repeat the process recursively
    for i in range(1, len(logic)):
        if len(logic[i]) > 1:
            logic[i] = parseCleanUp(logic[i])

    # Clean the logic again
    logic = cleanUp(logic)

    # return the final clean logic
    return logic


def parseImplications(logic):
    # If it is an iff statement, replace logic with the one we get by eliminating iffs
    if isIFFCandidate(logic):
        logic = eliminateIFF(logic)
    # If it is an implies statement, replace logic with the one we get by eliminating implies
    elif isImplicationCandidate(logic):
        logic = eliminateImplication(logic)

    # For all the attributes in the logic repeat the process recursively
    for i in range(1, len(logic)):
        if len(logic[i]) > 1:
            logic[i] = parseImplications(logic[i])

    # If it is an iff statement, replace logic with the one we get by eliminating iffs
    if isIFFCandidate(logic):
        logic = eliminateIFF(logic)
    # If it is an implies statement, replace logic with the one we get by eliminating implies
    elif isImplicationCandidate(logic):
        logic = eliminateImplication(logic)

    # return the final logic statement devoid of all implications and iffs
    return logic




