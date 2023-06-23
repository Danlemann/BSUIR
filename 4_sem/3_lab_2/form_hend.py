def listconvertation(formula):

    rezult_out = []

    for iterator in formula:
        rezult_out.append(iterator)

    return rezult_out


def hand_for_formila_in_inp(input_formula_data: str):
    input_formula_data = listconvertation(input_formula_data)
    for iterator_element_in_row in range(len(input_formula_data)):
        handler_inp(input_formula_data, iterator_element_in_row)
    logic_formula = ''.join(input_formula_data)
    return logic_formula


def handler_inp(input_formula_data, iterator_element_in_row):
    if input_formula_data[iterator_element_in_row] == '!':
        input_formula_data[iterator_element_in_row] = ' not '
    elif input_formula_data[iterator_element_in_row] == '+':
        input_formula_data[iterator_element_in_row] = ' or '
    elif input_formula_data[iterator_element_in_row] == '*':
        input_formula_data[iterator_element_in_row] = ' and '


def meinSort(meineListe):
    for i in range(len(meineListe)):
        minindex = i
        for j in range(minindex + 1, len(meineListe)):
            if meineListe[minindex] > meineListe[j]:
                minindex = j

        meineListe[i], meineListe[minindex] = meineListe[minindex], meineListe[i]
    return meineListe


def lements_move_to_form(formula: str):
    arg_elements_to_formulas_with_d = set()
    for iterator in range(len(formula)):
        if formula[iterator] == 'x':
            arg_elements_to_formulas_with_d.add(formula[iterator] + formula[iterator+1])
    arg_elements_to_formulas_with_d = list(arg_elements_to_formulas_with_d)
    arg_elements_to_formulas_with_d.sort(key=lambda x: int(x[1]))
    return arg_elements_to_formulas_with_d


def Func(group, variables, PIcount, PI):
    ungrouped = []

    for i in range(0, len(group) - 1):
        for j in range(0, len(group[i])):
            for k in range(0, len(group[i + 1])):
                new_min = ""
                differ = 0
                for bit in range(0, variables):
                    if group[i][j][variables - bit - 1] == group[i + 1][k][
                        variables - bit - 1]:
                        new_min = group[i][j][variables - bit - 1] + new_min
                    else:
                        new_min = "2" + new_min
                        differ += 1
                if new_min not in ungrouped and differ == 1:
                    ungrouped.append(new_min)
                if differ == 1:
                    PIcount[group[i][j]] += 1
                    PIcount[group[i + 1][k]] += 1
                    PIcount[new_min] = 0
                    PI[new_min] = (PI[group[i][j]].union(PI[group[i + 1][k]]))

    return group, PIcount, PI


def is_empty(any):
    if any:
        return False
    else:
        return True


def convert(PI):
    newPI = []
    for i in range(0, len(PI)):
        PIstr = ""
        for j in range(0, len(PI[i][0])):
            if PI[i][0][j] == "2":
                PIstr = PIstr + "-"
            else:
                PIstr = PIstr + PI[i][0][j]
        newPI.append(PIstr)
    return newPI


def solution(input):
    PIcount = {}
    PI = {}
    EPI = []
    NEPI = []


    while group != []:
        group, PIcount, PI = Func(group, PIcount, PI)
        if group == []:
            break

    PI_list = list(PI.items())
    PIcount_list = list(PIcount.items())
    PIs = []
    PI2 = []
    for i in range(0, len(PIcount_list)):
        if PIcount_list[i][1] == 0:
            PIs.append((PI_list[i][0]))
            PI2.append(set(PI_list[i][1]))
            if len(PI2) == 1:
                EPI.append(PI_list[i])
            else:
                for j in range(0, len(PI2)):
                    checker = 0
                    target = PI2[j]
                    for k in range(0, len(PI2)):
                        if is_empty(target - PI2[k]):
                            if target == PI2[k]:
                                pass
                            else:
                                checker += 1
                        else:
                            checker += 1
                    if checker == 1:
                        if PI_list[i] not in EPI:
                            EPI.append(PI_list[i])
                    else:
                        if PI_list[i] not in NEPI:
                            NEPI.append(PI_list[i])

    newEPI = convert(EPI)
    newNEPI = convert(NEPI)
    answer = []
    answer.append("EPI")
    if newEPI:
        for i in range(0, len(newEPI)):
            answer.append(newEPI[i])
    answer.append("NEPI")
    if newNEPI:
        for i in range(0, len(newEPI)):
            answer.append(newNEPI[i])
    return answer

def CrackingNumber():
    while True:
        x = int (input("gebe eine Zahl an von 0 - 10 an die erraten werden soll:"))#random.randrange(0,100)
        if x < 11 and x > 0:
            for i in range(0,5):
                y = []
                if (y < x):
                    print("Die gesuchte Zahl ist größer","Der Bot hat die Zahl", y, "geschätzt")
                elif (y > x):
                    print("Die gesuchte Zahl ist kleiner","Der Bot hat die Zahl", y, "geschätzt")
                else:
                    print("Der Computer sat Es ist die Zahl:", y)
                    return "0"
            print("Computer konnte deine Zahl net erraten.")
            print("Die gesuchte Zahl war: ", x)
            break
        else:
            print("deine musst nicht an die Bedingung halten..")
            continue