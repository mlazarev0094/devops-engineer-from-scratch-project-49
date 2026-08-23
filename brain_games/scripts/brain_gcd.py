from brain_games.engine import run_game
from brain_games.games.gcd import generate_question_and_answer, get_rules


def main():
    run_game(generate_question_and_answer, get_rules)


if __name__ == '__main__':
    main()
