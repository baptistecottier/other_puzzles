"""Global solver for i18n puzzles"""

import sys
import os
import builtins

if __name__ == '__main__':
    day = sys.argv[1].zfill(2)
    project_path = os.path.abspath(os.getcwd())
    INPUT_PATH = f"{project_path}/problems/problem_{day}/"
    sys.path.append(INPUT_PATH)
    module = __import__(f"solver_{day}")

    with open(f"{INPUT_PATH}/test_input_{day}.txt", encoding = "utf-8") as file:
        test_input = file.read()
        test_input, expected_test_answer = test_input.rsplit('\n', 1)

    with open(f"{INPUT_PATH}/user_input_{day}.txt", encoding = "utf-8") as file:
        user_input = file.read()

    if 'preprocessing' in dir(module):
        test_input = module.preprocessing(test_input)
        user_input = module.preprocessing(user_input)

    def solver(data):
        """
        Call module's solver with data, unpacking if data is a tuple.
        """
        if isinstance(test_input, builtins.tuple):
            return str(module.solver(*data))
        return str(module.solver(data))

    COMPUTED_TEST_ANSWER = solver(test_input)
    if  str(COMPUTED_TEST_ANSWER) == expected_test_answer:
        print("Test passed ✅")
        print("User answer:", solver(user_input))
    else:
        print("Test failed ❌. "
              f"Your answer: {COMPUTED_TEST_ANSWER}. "
              f"Expected answer: {expected_test_answer}")
