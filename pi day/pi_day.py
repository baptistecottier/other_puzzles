"""Global solver for Codyssi puzzles"""

import sys
import os

if __name__ == '__main__':
    year = sys.argv[1]
    project_path = os.path.abspath(os.getcwd())
    INPUT_PATH = f"{project_path}/events/year_{year}/"
    sys.path.append(INPUT_PATH)
    module = __import__(f"year_{year}")

    with open(f"{INPUT_PATH}/test_{year}.txt", encoding = "utf-8") as file:
        test_input = file.read()
        test_input, expected_test_answers = test_input.rsplit('\n', 1)
        expected_test_answers = expected_test_answers.splitlines()

    with open(f"{INPUT_PATH}/user_{year}.txt", encoding = "utf-8") as file:
        user_input = file.read()

    if 'preprocessing' in dir(module):
        pp = module.preprocessing
    else:
        def pp(x):
            """Identity function"""
            return x

    computed_user_answers = module.solver(pp(user_input))
    print("User answer:", next(computed_user_answers))

    # computed_test_answers = module.solver(pp(test_input))
    # for expected_test_answer in expected_test_answers:
    #     computed_test_answer = next(computed_test_answers)
    #     if  str(computed_test_answer) == expected_test_answer:
    #         print("Test passed ✅")
    #         computed_user_answers = module.solver(pp(user_input))
    #         print("User answer:", next(computed_user_answers))
    #     else:
    #         print("Test failed ❌. "
    #             f"Your answer: {computed_test_answer}. "
    #             f"Expected answer: {expected_test_answer}")