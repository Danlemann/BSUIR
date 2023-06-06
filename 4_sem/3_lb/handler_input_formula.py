
def input_handl(form: str):
    form = convert_for_list(form)
    for iterator in range(len(form)):
        if form[iterator] == '!':
            form[iterator] = ' not '
        elif form[iterator] == '+':
            form[iterator] = ' or '
        elif form[iterator] == '*':
            form[iterator] = ' and '
    logic_formula = ''.join(form)
    return logic_formula


def take_arg():
    arguments_input = set()
    for iterator in range(len(formula)):
        if formula[iterator] == 'x':
            arguments_input.add(formula[iterator] + formula[iterator+1])
    arguments_input.sort(key=lambda x: int(x[1]))
    return arguments_input

