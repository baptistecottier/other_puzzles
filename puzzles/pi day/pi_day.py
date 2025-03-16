"""Global solver for Codyssi puzzles"""

import sys
import os

if __name__ == '__main__':
    year = sys.argv[1]
    project_path = os.path.abspath(os.getcwd())
    INPUT_PATH = f"{project_path}/events/year_{year}/"
    sys.path.append(INPUT_PATH)
    module = __import__(f"year_{year}")

    with open(f"{INPUT_PATH}/user_{year}.txt", encoding = "utf-8") as file:
        user_input = file.read()

    if 'preprocessing' in dir(module):
        pp = module.preprocessing
    else:
        def pp(x):
            """Identity function"""
            return x

    computed_user_answers = module.solver(pp(user_input))
    for part, answer in enumerate(computed_user_answers, 1):
        print(f"Part {part}: {answer}")
