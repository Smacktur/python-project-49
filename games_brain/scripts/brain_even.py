#!/usr/bin/env python3

from games_brain.core.welcome import greeting
from games_brain.config import WIN_SCORE
from games_brain.games.even import equality_check


def main() -> None:
    user_name = greeting()
    equality_check(player=user_name, win_score=WIN_SCORE)


if __name__ == "__main__":
    main()
