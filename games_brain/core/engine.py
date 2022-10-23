import prompt


def ask_question(subject: int) -> None:
    print(f'Question: {subject}')


def get_answer():
    return prompt.string(prompt='Your answer: ')


def compare_result(player: str, user_answer, curr_answer, terms: bool):
    if terms:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{curr_answer}'.")
        print(f"Let's try again, {player}!")
