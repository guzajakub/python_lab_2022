class InputException(Exception):
    """Raised when user inputs differs from integer"""


def lock_with_cipher():
    cipher = 2137
    while True:
        try:
            user_input = int(input("Please enter cipher: "))
            if user_input == cipher:
                print("Passed - provided good code")
                break
            else:
                print("Failed - provided wrong code")
                continue
        except ValueError:
            print("Provided input is not an integer")


lock_with_cipher()

