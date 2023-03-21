import BIN
import floa

while True:

    key1 = input('Enter data type:\n'
                 '1) int\n'
                 '2) float\n'
                 '0) exit..\n')
    if key1 == '1':
        while True:
            a10 = int(input('Press (0) to exit..\n\n'
                            'Enter the first number: '))
            if a10 == 0:
                break
            b10 = int(input('Enter the second number: '))
            result = ''

            a2 = BIN.dec_to_bi(a10)
            b2 = BIN.dec_to_bi(b10)

            a2_encoding = BIN.transform(a10, a2)
            b2_encoding = BIN.transform(b10, b2)

            a2_modul = BIN.dec_to_bi(abs(a10))
            b2_modul = BIN.dec_to_bi(abs(b10))

            a2_encoding_modul = BIN.transform(abs(a10), a2_modul)
            b2_encoding_modul = BIN.transform(abs(b10), b2_modul)

            while True:
                key = input('Enter operation number\n'
                            '1) +\n'
                            '2) -\n'
                            '3) *\n'
                            '4) /\n'
                            '0) exit..\n')

                print('a(10) =    ', a10)
                print('b(10) =    ', b10)

                print('a =    ', a2_encoding)
                print('b =    ', b2_encoding)

                if key == '1':
                    result = BIN.plus(a2_encoding, b2_encoding)
                    print('(a+b) =', result)
                    print('(10)->(2) = ', BIN.bi_to_dec(result))
                elif key == '2':
                    result = BIN.plus(a2_encoding, BIN.transform(-b10,
                                                                 b2))  # тута передаем число б в отрицательном виде для имитации вычитания
                    print('(a-b) =', result)
                    print('(10)->(2) = ', BIN.bi_to_dec(result))

                elif key == '3':
                    result = BIN.multiplication(a2_encoding_modul, b2_encoding_modul)
                    print('|a*b| =', result)
                    print('(10)->(2) = ', int(result, 2))

                elif key == '4':
                    result = BIN.division(a2_encoding_modul, b2_encoding_modul)
                    print('|a/b| =', result)
                    print('(10)->(2) = ', int(result, 2))

                if key == '0':
                    break
    elif key1 == '2':

        num1 = float(input('Press (0) to exit..\n\n'
                           'Enter the first number: '))
        if num1 == '0':
            break
        num2 = float(input('Enter the second number: '))

        if num1 < 0 < num2:
            temp_num = num1
            num1 = num2
            num2 = temp_num

        number1 = floa.dec_to_bin_straight(num1)
        number2 = floa.dec_to_bin_add(num2)

        print("a = " + floa.dec_to_bin_straight(num1))
        print("b = " + floa.dec_to_bin_add(num2))
        print("(a + b) = " + str(floa.from_float_to_decimal(floa.summ_of_floating(num1, num2))))

    elif key1 == '0':
        break
