from games_brain.utils.randomizer import get_rand_int
from games_brain.core.engine import ask_question, get_answer, compare_result


def main_greeting():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def equality_check(player: str, win_score: int):
    main_greeting()

    # Available resources
    current_score = 0

    while current_score < win_score:
        random_num = get_rand_int(range_to=100)
        ask_question(subject=random_num)
        user_answer = get_answer()

        # Game terms
        if random_num % 2 == 0:
            curr_answer = 'yes'
        elif random_num % 2 != 0:
            curr_answer = 'no'

        # We check the user's response with the terms of the game
        if curr_answer == user_answer:
            current_score += 1
            compare_result(player, user_answer, curr_answer, terms=True)

            if current_score == win_score:
                print(f'Congratulations, {player}!')
        else:
            compare_result(player, user_answer, curr_answer, terms=False)
            break
