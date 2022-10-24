#!/usr/bin/env python3

from games_brain.core.welcome import greeting
from games_brain.config import WIN_SCORE
from games_brain.games.calc import calc_result


def main() -> None:
    user_name = greeting()
    calc_result(player=user_name, win_score=WIN_SCORE)


if __name__ == "__main__":
    main()
