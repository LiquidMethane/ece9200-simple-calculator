def type_of(char):
    if 48 <= ord(char) <= 57:
        return 'Num'
    elif char == 'M':
        return 'Mode'
    elif char == '.':
        return 'Decimal'
    elif char == 'E':
        return 'Enter'
    else:
        return 'Opr'


def to_num(char):
    return ord(char) - 48


def calculate(n1, opr, n2):
    print(f'Calculate: [{n1}] [{opr}] [{n2}]')

    if opr == '+':
        res = n1 + n2
    elif opr == '-':
        res = n1 - n2
    elif opr == 'x':
        res = n1 * n2
    elif opr == '/':
        res = n1 / n2
    else:
        return -1

    if float(res).is_integer():
        return int(float(res))
    else:
        return round(res, 5)


def calculate_reverse(n1, opr, n2):
    return calculate(n2, opr, n1)


class Controller:

    # member variables
    # __state = None
    # __layout = None
    __mode = 'INFIX'
    __opr = ''
    __key = ''
    __nk = ''
    __ans = ''
    # __decimal = False
    __deci_count = 0
    __stack = []

    def __init__(self, inst):
        # assign layout instance and initialize calculator logic
        self.__layout = inst
        self.__initialize()

    def __initialize(self):
        if self.__mode == "INFIX":
            self.__infix_0()
        else:
            self.__rpn_0()

        return

    def handle_input(self, char):
        # print info
        # print(f'key press: [{char}]')
        # print(f'current state: [{self.__state}]')
        # print(f'input type: [{type_of(char)}]')

        # state transition for infix mode
        if self.__state == 'INFIX1' and type_of(char) == 'Num':
            self.__infix_2(to_num(char))

        elif self.__state == 'INFIX1' and type_of(char) == 'Opr':
            self.__infix_4(char)

        elif self.__state == 'INFIX2' and type_of(char) == 'Opr':
            self.__infix_1(char)

        elif self.__state == 'INFIX2' and type_of(char) == 'Num':
            self.__infix_3(to_num(char))

        elif self.__state == 'INFIX2' and type_of(char) == 'Decimal':
            self.__infix_5()

        elif self.__state == 'INFIX3' and type_of(char) == 'Num':
            self.__infix_3(to_num(char))

        elif self.__state == 'INFIX3' and type_of(char) == 'Opr':
            self.__infix_1(char)

        elif self.__state == 'INFIX3' and type_of(char) == 'Decimal':
            self.__infix_5()

        elif self.__state == 'INFIX4' and type_of(char) == 'Num':
            self.__infix_2(to_num(char))

        elif self.__state == 'INFIX4' and type_of(char) == 'Opr':
            self.__infix_4(char)

        elif self.__state == 'INFIX5' and type_of(char) == 'Num':
            self.__infix_3(to_num(char))

        elif self.__state == 'INFIX5' and type_of(char) == 'Decimal':
            self.__infix_5()

        # state transition for rpn mode
        elif self.__state == 'RPN0' and type_of(char) == 'Num':
            self.__rpn_1(to_num(char))

        elif self.__state == 'RPN1' and type_of(char) == 'Num':
            self.__rpn_3(to_num(char))

        elif self.__state == 'RPN1' and type_of(char) == 'Decimal':
            self.__rpn_2()

        elif self.__state == 'RPN1' and type_of(char) == 'Enter':
            self.__rpn_4()

        elif self.__state == 'RPN1' and type_of(char) == 'Opr':
            self.__rpn_5(char)

        elif self.__state == 'RPN2' and type_of(char) == 'Decimal':
            self.__rpn_2()

        elif self.__state == 'RPN2' and type_of(char) == 'Num':
            self.__rpn_3(to_num(char))

        elif self.__state == 'RPN3' and type_of(char) == 'Decimal':
            self.__rpn_2()

        elif self.__state == 'RPN3' and type_of(char) == 'Num':
            self.__rpn_3(to_num(char))

        elif self.__state == 'RPN3' and type_of(char) == 'Enter':
            self.__rpn_4()

        elif self.__state == 'RPN3' and type_of(char) == 'Opr':
            self.__rpn_5(char)

        elif self.__state == 'RPN4' and type_of(char) == 'Num':
            self.__rpn_1(to_num(char))

        elif self.__state == 'RPN5' and type_of(char) == 'Num':
            self.__rpn_1(to_num(char))

        elif self.__state == 'RPN5' and type_of(char) == 'Opr':
            self.__rpn_5(char)

        # mode selection
        elif self.__state == 'INFIX1' and type_of(char) == 'Mode':
            self.__layout.set_mode('RPN')
            self.__rpn_0()

        elif self.__state == 'INFIX2' and type_of(char) == 'Mode':
            self.__layout.set_mode('RPN')
            self.__rpn_0()

        elif self.__state == 'INFIX3' and type_of(char) == 'Mode':
            self.__layout.set_mode('RPN')
            self.__rpn_0()

        elif self.__state == 'INFIX4' and type_of(char) == 'Mode':
            self.__layout.set_mode('RPN')
            self.__rpn_0()

        elif self.__state == 'INFIX5' and type_of(char) == 'Mode':
            self.__layout.set_mode('RPN')
            self.__rpn_0()

        elif self.__state == 'RPN0' and type_of(char) == 'Mode':
            self.__layout.set_mode('INFIX')
            self.__infix_0()

        elif self.__state == 'RPN1' and type_of(char) == 'Mode':
            self.__layout.set_mode('INFIX')
            self.__infix_0()

        elif self.__state == 'RPN2' and type_of(char) == 'Mode':
            self.__layout.set_mode('INFIX')
            self.__infix_0()

        elif self.__state == 'RPN3' and type_of(char) == 'Mode':
            self.__layout.set_mode('INFIX')
            self.__infix_0()

        elif self.__state == 'RPN4' and type_of(char) == 'Mode':
            self.__layout.set_mode('INFIX')
            self.__infix_0()

        elif self.__state == 'RPN5' and type_of(char) == 'Mode':
            self.__layout.set_mode('INFIX')
            self.__infix_0()

        return

    def __infix_0(self):
        self.__state = 'INFIX0'
        self.__opr = ''
        self.__key = ''
        self.__nk = 0
        self.__decimal = False
        self.__infix_1('')

    def __infix_1(self, opr):
        self.__state = 'INFIX1'
        self.__deci_count = 0
        self.__key = opr
        if self.__opr == '':
            self.__ans = self.__nk
        else:
            self.__ans = calculate(self.__ans, self.__opr, self.__nk)

        self.__layout.set_display(self.__ans)
        self.__opr = self.__key

    def __infix_2(self, num):
        self.__state = 'INFIX2'
        self.__key = num
        self.__decimal = False
        self.__nk = self.__key
        self.__layout.set_display(self.__nk)

    def __infix_3(self, num):
        self.__state = 'INFIX3'
        self.__deci_count += 1
        self.__key = num
        if self.__decimal:
            self.__nk = self.__nk + self.__key * pow(0.1, self.__deci_count)
        else:
            self.__nk = self.__nk * 10 + self.__key

        self.__layout.set_display(self.__nk)

    def __infix_4(self, opr):
        self.__state = 'INFIX4'
        self.__key = opr
        self.__opr = self.__key

        self.__layout.set_display(self.__ans)

    def __infix_5(self):
        self.__state = 'INFIX5'
        self.__decimal = True

        if isinstance(self.__nk, int):
            self.__layout.set_display(str(self.__nk) + '.')
        else:
            self.__layout.set_display(self.__nk)

    def __rpn_0(self):
        self.__state = 'RPN0'
        self.__stack = []
        self.__decimal = False
        self.__deci_count = 0
        self.__layout.set_display(0)

    def __rpn_1(self, num):
        self.__state = 'RPN1'
        self.__key = num
        self.__decimal = False
        self.__stack.append(self.__key)
        self.__layout.set_display(self.__stack[-1])

    def __rpn_2(self):
        self.__state = 'RPN2'
        self.__decimal = True

        if isinstance(self.__stack[-1], int):
            self.__layout.set_display(str(self.__stack[-1]) + '.')
        else:
            self.__layout.set_display(self.__stack[-1])

    def __rpn_3(self, num):
        self.__state = 'RPN3'
        self.__deci_count += 1
        self.__key = num
        if self.__decimal:
            self.__stack[-1] = self.__stack[-1] + self.__key * pow(0.1, self.__deci_count)
        else:
            self.__stack[-1] = self.__stack[-1] * 10 + self.__key

        self.__layout.set_display(self.__stack[-1])

    def __rpn_4(self):
        self.__state = 'RPN4'
        self.__deci_count = 0
        self.__layout.set_display(self.__stack[-1])

    def __rpn_5(self, opr):
        self.__state = 'RPN5'
        self.__key = opr
        self.__stack.append(calculate_reverse(self.__stack.pop(), self.__key, self.__stack.pop()))
        self.__layout.set_display(self.__stack[-1])
