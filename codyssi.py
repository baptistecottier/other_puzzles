"""Global solver for Codyssi puzzles"""

import sys
import os

if __name__ == '__main__':
    year = sys.argv[1]
    day = sys.argv[2].zfill(2)
    project_path = os.path.abspath(os.getcwd())
    INPUT_PATH = f"{project_path}/events/year_{year}/day_{day}/"
    sys.path.append(INPUT_PATH)
    module = __import__(f"solver_{day}")

    with open(f"{INPUT_PATH}/test_input_{day}.txt", encoding = "utf-8") as file:
        test_input = file.read()
        test_input, expected_test_answers = test_input.split('\n\n', 1)
        expected_test_answers = expected_test_answers.splitlines()

    with open(f"{INPUT_PATH}/user_input_{day}.txt", encoding = "utf-8") as file:
        user_input = file.read()

    if 'preprocessing' in dir(module):
        user_input = module.preprocessing(user_input)
        test_input = module.preprocessing(test_input)

    computed_test_answers = module.solver(test_input)
    computed_user_answers = module.solver(user_input)
    for expected_test_answer in expected_test_answers:
        computed_test_answer = next(computed_test_answers)
        if  str(computed_test_answer) == expected_test_answer:
            print("Test passed ✅")
            print("User answer:", next(computed_user_answers))
        else:
            print("Test failed ❌. "
                f"Your answer: {computed_test_answer}. "
                f"Expected answer: {expected_test_answer}")
