from create_table import *


def formula_to_create_conunction_normal_form(formula):
    sdf_splut_formula = sdnf(formula).split()
    binary_sdnf_elements_formula = list()
    for i in range(0, len(sdf_splut_formula)):
        if sdf_splut_formula[i][0] == 'x':
            binary_sdnf_elements_formula.append('1')
        elif sdf_splut_formula[i][0] == '!':
            binary_sdnf_elements_formula.append('0')
        elif sdf_splut_formula[i][0] == ')':
            binary_sdnf_elements_formula.append('+')
    binary_sdnf_elements_formula = ''.join(binary_sdnf_elements_formula[:-1])
    sdnf_dec = bin_to_dec(binary_sdnf_elements_formula, formula)
    sdnf_dec = map(str, sdnf_dec)
    sdnf_dec = '+(' + ', '.join(sdnf_dec) + ')'
    return binary_sdnf_elements_formula, sdnf_dec


def method_to_create_conunction_normal_form(formula):
    sknf_form_to_create_output = ''
    data_with_elements = cr_tabl(formula)[1]
    for iterator in data_with_elements:
        if iterator['f'] == 0:
            part = '+'.join([values * '!' + keys for keys, values in iterator.items() if keys != 'f' and keys != 'i'])
            sknf_form_to_create_output += '(' + str(part) + ')' + '*'
    sknf_form_to_create_output = sknf_form_to_create_output[:-1]
    return sknf_form_to_create_output


def numb_to_create_conunction_normal_form(formula):
    perfect_conunction_form_in_number = method_to_create_conunction_normal_form(formula).split()
    binary_conunction_normal_elements = list()
    for iterator in range(0, len(perfect_conunction_form_in_number)):
        if perfect_conunction_form_in_number[iterator][0] == 'x':
            binary_conunction_normal_elements.append('0')
        elif perfect_conunction_form_in_number[iterator][0] == '!':
            binary_conunction_normal_elements.append('1')
        elif perfect_conunction_form_in_number[iterator][0] == ')':
            binary_conunction_normal_elements.append('*')
    binary_conunction_normal_elements = ''.join(binary_conunction_normal_elements[:-1])
    decembary_conunction_element_in = bin_to_dec(binary_conunction_normal_elements, formula)
    decembary_conunction_element_in = map(str, decembary_conunction_element_in)
    decembary_conunction_element_in = '*(' + ', '.join(decembary_conunction_element_in) + ')'

    return binary_conunction_normal_elements, decembary_conunction_element_in


def meinSort(meineListe):
    for i in range(len(meineListe)):
        minindex = i
        for j in range(minindex + 1, len(meineListe)):
            if meineListe[minindex] > meineListe[j]:
                minindex = j

        meineListe[i], meineListe[minindex] = meineListe[minindex], meineListe[i]
    return meineListe


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


def sdnf(formula):
    formula_to_create_disunction_normal_form = ''
    data_table = cr_tabl(formula)[1]
    for iterator in data_table:
        if iterator['f'] == 1:
            part = '*'.join([abs(values - 1) * '!' + keys for keys, values in iterator.items()
                             if keys != 'f' and keys != 'i'])
            formula_to_create_disunction_normal_form += '(' + str(part) + ')' + '+'
    formula_to_create_disunction_normal_form = formula_to_create_disunction_normal_form[0:-1]
    return formula_to_create_disunction_normal_form


def load_config(configfilepath):

    global VERBOSE
    if isinstance(configfilepath, list):
        configfilepath = configfilepath[0]
    with open(configfilepath) as inputfile:
        config = []
        inputfile.close()

    ersetzen = []
    for pattern in config["ersetzen"]:
        if VERBOSE:
            print("Überstetze Muster %s" % pattern["regexp"])
        ersetzen.append([compile(pattern["regexp"]), pattern["ziel"], pattern["regexp"]])
    warnung = []
    for pattern in config["warnung"]:
        if VERBOSE:
            print("Überstetze Muster %s" % pattern["regexp"])
        warnung.append([compile(pattern["regexp"]), pattern["warnung"], pattern["regexp"]])
    if VERBOSE:
        print("Ergebnisse: Ersetzten:")
        print(ersetzen)
        print("Warnen:")
        print(warnung)
    return ersetzen, warnung

