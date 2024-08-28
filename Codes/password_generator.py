import random

def random_char(num):
    """
    Generate a random character based on the given number.

    Parameters:
    num (int): A number representing the type of character to generate.
        - 1: Generate a lowercase letter.
        - 2: Generate an uppercase letter.
        - 3: Generate a digit.
        - 4: Generate a special character.
        - Any other value: Generate a random character from the above categories.

    Returns:
    str: A random character based on the given number.
    """
    if num == 1:
        return chr(random.randint(97, 122))

    elif num == 2:
        return chr(random.randint(65, 90))

    elif num == 3:
        return chr(random.randint(48, 57))

    elif num == 4:
        symbol_ranges = [
            (33, 47),
            (58, 64),
            (91, 96),
            (123, 126)
        ]
        symbol_range = random.choice(symbol_ranges)

        return chr(random.randint(symbol_range[0], symbol_range[1]))

    else:
        return random_char(random.randint(1,4))



def password_generator(length: int) -> str:
    """
    Generate a random password of the specified length.

    The password is constructed by calling the 'random_char' function for each position in the password.
    The 'random_char' function generates a random character based on the position (1-indexed).
    The characters are then shuffled to ensure randomness.

    Parameters:
    length (int): The length of the password to generate.

    Returns:
    str: The generated password.
    """
    password_list = []
    for i in range(length):
        password_list.append(random_char(i+1))

    random.shuffle(password_list)
    return "".join(password_list)




if __name__ == "__main__":
    length = int(input("Enter the length of password: "))

    print(password_generator(length))
