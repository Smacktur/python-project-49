import prompt


def welcome_user():
    user_name = prompt.string(prompt="May I have your name? ")
    return f'Hello, {user_name}!'
