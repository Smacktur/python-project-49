from games_brain.utils.randomizer import get_rand_char, get_rand_int
from games_brain.core.engine import ask_question, get_answer, compare_result


def main_greeting():
    print("What is the result of the expression?")


def calc_result(player: str, win_score: int):
    main_greeting()

    # Available resources
    current_score = 0
    operation = ['+', '-', '*']

    while current_score < win_score:
        random_sum1 = get_rand_int(range_to=40)
        random_sum2 = get_rand_int(range_to=10)
        random_op = get_rand_char(operation)
        subj_struct = f'{random_sum1} {random_op} {random_sum2}'

        ask_question(subject=subj_struct)
        user_answer = get_answer()

        # Game terms
        if random_op == '+':
            curr_answer = str(random_sum1 + random_sum2)
        elif random_op == '-':
            curr_answer = str(random_sum1 - random_sum2)
        elif random_op == '*':
            curr_answer = str(random_sum1 * random_sum2)

        # We check the user's response with the terms of the game
        if curr_answer == user_answer:
            current_score += 1
            compare_result(player, user_answer, curr_answer, terms=True)

            if current_score == win_score:
                print(f'Congratulations, {player}!')
        else:
            compare_result(player, user_answer, curr_answer, terms=False)
            break
