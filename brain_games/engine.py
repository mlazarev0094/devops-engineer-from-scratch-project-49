from brain_games.cli import (
    welcome_user,
    get_user_answer,
    display_correct,
    display_wrong
)

ROUNDS_TO_WIN = 3


def run_game(game_module):
    name = welcome_user()
    print(game_module.RULES)

    correct_count = 0

    while correct_count < ROUNDS_TO_WIN:
        correct_answer, question = game_module.generate_question_and_answer()
        print(question)

        user_answer = get_user_answer()

        if user_answer == correct_answer:
            display_correct()
            correct_count += 1
        else:
            display_wrong(user_answer, correct_answer, name)
            return

    print(f"Congratulations, {name}!")
