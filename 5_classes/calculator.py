from complexnumber import ComplexNumber


class Calculator:

    @classmethod
    def ask_for_number(cls):
        user_input = input("Enter expression in format: 2.0+3.0j - 3.9-1.1j\n")
        try:
            first_num_as_str, op, second_num_as_str = user_input.split()
        except ValueError:
            print("Wrong input expression, check whitespace positions")
        else:
            first_num = ComplexNumber.str_format(first_num_as_str)
            second_num = ComplexNumber.str_format(second_num_as_str)
            if op == '+':
                result = first_num + second_num
            elif op == '-':
                result = first_num - second_num
            elif op == '*':
                result = first_num * second_num
            elif op == '/':
                result = first_num / second_num
            else:
                raise ValueError("Wrong operator, or operator not supported")
            print(f"{first_num} {op} {second_num} = {result}")


if __name__ == "__main__":

    while True:
        try:
            Calculator.ask_for_number()
        except KeyboardInterrupt:
            print("Interrupted by keyboard ctrl+c")
            break

