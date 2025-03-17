"""Global solver for coding quest puzzles"""

import sys
import os
from inspect import signature


if __name__ == '__main__':
    year = sys.argv[1]
    if year[0] == 'p':
        YEAR = f"practice_{year[1:]}"
    else:
        YEAR = f"challenge_{year[1:]}"

    day = sys.argv[2].zfill(2)

    project_path = os.path.abspath(os.getcwd())
    INPUT_PATH = f"{project_path}/events/{YEAR}/day_{day}/"
    sys.path.append(INPUT_PATH)
    module = __import__(f"solver_{day}")

    with open(f"{INPUT_PATH}/test_input_{day}.txt", encoding = "utf-8") as file:
        test_input = file.read()
        test_input, expected_test_answer = test_input.rsplit('\n', 1)

    with open(f"{INPUT_PATH}/user_input_{day}.txt", encoding = "utf-8") as file:
        user_input = file.read()

    if 'preprocessing' in dir(module):
        pp = module.preprocessing
    else:
        def pp(x):
            """Identity function"""
            return x

    def solver(data):
        """
        Call module's solver with data, unpacking if data is a tuple.
        """
        n_args = len(signature(module.solver).parameters)
        if n_args > 1:
            return module.solver(*data)
        return module.solver(data)

    COMPUTED_TEST_ANSWER = solver(pp(test_input))
    if  str(COMPUTED_TEST_ANSWER) == expected_test_answer:
        print("Test passed ✅")
        print("User answer:", solver(pp(user_input)))
    else:
        print("Test failed ❌. "
              f"Your answer: {COMPUTED_TEST_ANSWER}. "
              f"Expected answer: {expected_test_answer}")
