#!/bin/python3
WIN  = 6
DRAW = 3
LOSE = 0

OPPONENT_ROCK     = "A"
OPPONENT_PAPER    = "B"
OPPONENT_SCISSORS = "C"

MY_ROCK           = "X"
MY_PAPER          = "Y"
MY_SCISSORS       = "Z"

POINTS_BY_SHAPE = {
    MY_ROCK:     1,
    MY_PAPER:    2,
    MY_SCISSORS: 3,
}

POINTS_BY_DESIRED_MOVE = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

CORRESPONDING_FOR_WIN = {
    OPPONENT_PAPER:    MY_SCISSORS,
    OPPONENT_ROCK:     MY_PAPER,
    OPPONENT_SCISSORS: MY_ROCK,
}

CORRESPONDING_FOR_DRAW = {
    OPPONENT_PAPER:    MY_PAPER,
    OPPONENT_ROCK:     MY_ROCK,
    OPPONENT_SCISSORS: MY_SCISSORS,
}

CORRESPONDING_FOR_LOSE = {
    OPPONENT_PAPER:    MY_ROCK,
    OPPONENT_ROCK:     MY_SCISSORS,
    OPPONENT_SCISSORS: MY_PAPER,
}

OPPONENT = 0
MY       = 1


def points_of_round(opponent: str, me: str) -> int:
    if (opponent == 'A' and me == 'Y') or \
       (opponent == 'B' and me == 'Z') or \
       (opponent == 'C' and me == 'X'):
        return WIN
    if (opponent == 'A' and me == 'X') or \
       (opponent == 'B' and me == 'Y') or \
       (opponent == 'C' and me == 'Z'):
        return DRAW
    if (opponent == 'A' and me == 'Z') or \
       (opponent == 'B' and me == 'X') or \
       (opponent == 'C' and me == 'Y'):
        return LOSE


def points_by_shape(my_shape: str) -> int:
    return POINTS_BY_SHAPE[my_shape]


def parse_matches_file(path: str) -> list:
    matches_list = []
    with open(path, 'r') as matches_table:
        for match in matches_table:
            matches_list.append(tuple(match.strip().split(' ')))
    return matches_list


def calculate_score(matches: list) -> int:
    return sum(points_by_shape(match[MY]) + points_of_round(match[OPPONENT], match[MY]) for match in matches)

POINTS_BY_DESIRED_MOVE = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

CORRESPONDING_FOR_WIN = {
    OPPONENT_ROCK: MY_PAPER,
    OPPONENT_PAPER: MY_SCISSORS,
    OPPONENT_SCISSORS: MY_ROCK,
}

CORRESPONDING_FOR_DRAW = {
    OPPONENT_ROCK: MY_ROCK,
    OPPONENT_PAPER: MY_PAPER,
    OPPONENT_SCISSORS: MY_SCISSORS,
}

CORRESPONDING_FOR_LOSE = {
    OPPONENT_ROCK: MY_SCISSORS,
    OPPONENT_PAPER: MY_ROCK,
    OPPONENT_SCISSORS: MY_PAPER,
}

TABLE_BY_RESULT = {
    DRAW: CORRESPONDING_FOR_DRAW,
    LOSE: CORRESPONDING_FOR_LOSE,
    WIN:  CORRESPONDING_FOR_WIN,
}

def new_strategy_game(matches: list) -> int:
    return sum(POINTS_BY_DESIRED_MOVE[match[MY]] + POINTS_BY_SHAPE[
                                                    TABLE_BY_RESULT[
                                                        POINTS_BY_DESIRED_MOVE[match[MY]]][match[OPPONENT]
                                                    ]
                                                   ] for match in matches)


if __name__ == "__main__":
    print(TABLE_BY_RESULT[LOSE][OPPONENT_SCISSORS])
    matches = parse_matches_file(path="./matches.txt")
    print(calculate_score(matches))
    print(new_strategy_game(matches))

