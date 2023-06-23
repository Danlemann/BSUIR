
from method_t import *
from method_c_t import *

formula_test = ['!(x1+!x2*(!x3))']


def main():

    for iterator in range(len(formula_test)):

        print('\t\tTest № {}:{} '.format(iterator + 1, formula_test[iterator]), '\n')
        main_f_to_create = formula_test[iterator]

        formula_compile_in_sdnf = method_to_create_conunction_normal_form(main_f_to_create)
        formula_compile_in_sknf = sdnf(main_f_to_create)

        print('Стандартная форма\nСДНФ ==> {}'.format(formula_compile_in_sknf), '\n',
              ('СКНФ ==> {}'.format(formula_compile_in_sdnf)), '\n',
              ('Расчетный метод\nСДНФ ==> {}'.format(calc_method(formula_compile_in_sknf))), '\n',
              ('СКНФ ==> {}'.format(calculation_method_sknf(formula_compile_in_sdnf))), '\n',
              ('Расчетно-табличный метод\nСДНФ ==> {}\n{}'
               .format(funcrion_reate_c_t_m_disunction_form(formula_compile_in_sknf)[0],
                                                                 funcrion_reate_c_t_m_disunction_form
                                                                 (formula_compile_in_sknf)[1])), '\n',
              ('СКНФ ==> {}\n{}'.format(function_create_knf_method(formula_compile_in_sdnf)[0],
                                        function_create_knf_method(formula_compile_in_sdnf)[1])),
              '\n',
              ('Табличный метод\n{}\nСДНФ ==> {}'.format(datatable_method(main_f_to_create)[2],
                                                     datatable_method(main_f_to_create)[0])), '\n',
              ('СКНФ ==> {}'.format(datatable_method(main_f_to_create)[1])))


if __name__ == '__main__':

    main()