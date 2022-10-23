#!/usr/bin/env python3
from games_brain.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    print(f'Hello, {welcome_user()}!')


if __name__ == "__main__":
    main()