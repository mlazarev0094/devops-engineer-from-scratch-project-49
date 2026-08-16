from brain_games.cli import (
    welcome_user,
    get_user_unswer,
    display_correct,
    display_wrong
)


def run_game(generate_question_and_answer, get_rules):
    name = welcome_user()
    print(get_rules())

    correct_count = 0
    rounds_to_win = 3

    while correct_count < rounds_to_win:
        correct_answer, question = generate_question_and_answer()
        print(question)

        user_answer = get_user_unswer()

        if user_answer == correct_answer:
            display_correct()
            correct_count += 1
        else:
            display_wrong(user_answer, correct_answer, name)
            return

    print(f"Congratulations, {name}!")
