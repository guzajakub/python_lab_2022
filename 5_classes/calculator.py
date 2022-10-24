from complexnumber import ComplexNumber
import re


# # for example, valid expression is 23.43+48.32j / 32.49-43j - note position of whitespaces
# while True:
#     user_input = input("Enter your expression involving complex numbers >> ")
#     try:
#         first_num_as_str, op, second_num_as_str = user_input.split()
#     except ValueError:
#         print("Wrong convention of input")
#     else:
#
#         if op == '+':
#             result = first_num + second_num
#         elif op == '-':
#             result = first_num - second_num
#         elif op == '*':
#             result = first_num * second_num
#         elif op == '/':
#             result = first_num / second_num
#         else:
#             raise RuntimeError("Invalid operator provided")
#
#         print(f"The result of {first_num} {op} {second_num} == {result}")


def parse_complex_number(complex_num):
    split_ = re.split(r'[+-]', complex_num)
    return split_




if __name__ == "__main__":
    a = "23.43-48.32j / 32.49-43j"
    first_num_as_str, op, second_num_as_str = a.split(" ")
    print(parse_complex_number("23.43+48.32j"))

