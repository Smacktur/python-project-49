#!/usr/bin/env python3

import prompt
from random import randint


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = prompt.string(prompt="May I have your name? ")
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    ranw_count = 0

    while ranw_count < 3:
        random_num = randint(0, 100)
        print(f'Question: {random_num}')
        answer = prompt.string(prompt='Your answer: ')

        # TODO: уменьшить код (есть повторы)
        if random_num % 2 == 0 and answer == 'yes':
            print('Correct!')
            ranw_count += 1
        elif random_num % 2 != 0 and answer == 'no':
            print('Correct!')
            ranw_count += 1
        elif random_num % 2 != 0 and answer == 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {user_name}!")
            break
        elif random_num % 2 == 0 and answer == 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {user_name}!")
            break

        if ranw_count == 3:
            print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
