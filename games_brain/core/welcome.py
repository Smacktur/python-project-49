def get_name():
    user_name = input()
    return user_name


def greeting():
    print("Welcome to the Brain Games!")
    print("May I have your name? ", end="")

    user_name = get_name()

    print(f'Hello, {user_name}!')

    return user_name
