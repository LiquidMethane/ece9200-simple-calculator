def type_of(char):
    if 48 <= ord(char) <= 57:
        return 'Num'
    elif char == 'M':
        return 'Mode'
    elif char == '.':
        return 'Decimal'
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
    __state = None
    __layout = None
    __mode = 'INFIX'
    __opr = ''
    __key = ''
    __nk = ''
    __ans = ''
    __decimal = False
    __deci_count = 0
    __stack = []

    def __init__(self, inst):
        self.__layout = inst
        self.__initialize()

    def __initialize(self):
        if self.__mode == "INFIX":
            self.__infix_0()
        else:
            self.__stack = []
            self.__decimal = False

        return

    def handle_input(self, char):
        print(f'key press: [{char}]')
        print(f'current state: [{self.__state}]')
        print(f'input type: [{type_of(char)}]')

        if self.__state == 'INFIX1' and type_of(char) == 'Num':
            self.__infix_2(to_num(char))

        elif self.__state == 'INFIX1' and type_of(char) == 'Opr':
            self.__infix_4(char)

        elif self.__state == 'INFIX2' and type_of(char) == 'Opr':
            self.__infix_1(char)

        elif self.__state == 'INFIX2' and type_of(char) == 'Num':
            self.__infix_3(to_num(char))

        elif self.__state == 'INFIX2' and type_of(char) == 'Decimal':
            self.__infix_5(char)

        elif self.__state == 'INFIX3' and type_of(char) == 'Num':
            self.__infix_3(to_num(char))

        elif self.__state == 'INFIX3' and type_of(char) == 'Opr':
            self.__infix_1(char)

        elif self.__state == 'INFIX3' and type_of(char) == 'Decimal':
            self.__infix_5(char)

        elif self.__state == 'INFIX4' and type_of(char) == 'Num':
            self.__infix_2(to_num(char))

        elif self.__state == 'INFIX4' and type_of(char) == 'Opr':
            self.__infix_4(char)

        elif self.__state == 'INFIX5' and type_of(char) == 'Num':
            self.__infix_3(to_num(char))

        elif self.__state == 'INFIX5' and type_of(char) == 'Decimal':
            self.__infix_5(char)

        return

    def __infix_0(self):
        self.__state = 'INFIX0'
        self.__opr = ''
        self.__key = ''
        self.__nk = ''
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

    def __infix_5(self, decimal):
        self.__state = 'INFIX5'
        self.__decimal = True
        self.__key = decimal

        if isinstance(self.__nk, int):
            self.__layout.set_display(str(self.__nk) + '.')
        else:
            self.__layout.set_display(self.__nk)
