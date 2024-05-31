"""


 ██▓     █    ██ ▒██   ██▒ █    ██  ██▀███ ▓██   ██▓ ██ ▄█▀▄▄▄       ██▀███   ███▄ ▄███▓ ▄▄▄
▓██▒     ██  ▓██▒▒▒ █ █ ▒░ ██  ▓██▒▓██ ▒ ██▒▒██  ██▒ ██▄█▒▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄
▒██░    ▓██  ▒██░░░  █   ░▓██  ▒██░▓██ ░▄█ ▒ ▒██ ██░▓███▄░▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄
▒██░    ▓▓█  ░██░ ░ █ █ ▒ ▓▓█  ░██░▒██▀▀█▄   ░ ▐██▓░▓██ █▄░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██
░██████▒▒▒█████▓ ▒██▒ ▒██▒▒▒█████▓ ░██▓ ▒██▒ ░ ██▒▓░▒██▒ █▄▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒
░ ▒░▓  ░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ██▒▒▒ ▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░
░ ░ ▒  ░░░▒░ ░ ░ ░░   ░▒ ░░░▒░ ░ ░   ░▒ ░ ▒░▓██ ░▒░ ░ ░▒ ▒░ ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░
  ░ ░    ░░░ ░ ░  ░    ░   ░░░ ░ ░   ░░   ░ ▒ ▒ ░░  ░ ░░ ░  ░   ▒     ░░   ░ ░      ░     ░   ▒
    ░  ░   ░      ░    ░     ░        ░     ░ ░     ░  ░        ░  ░   ░            ░         ░  ░
                                            ░ ░


"""

"""
This script is to help into doing question and learn without being block in the same modual or need
to change question by your self.

Author: Luxury_Karma
Date: 2024-05-31
Version: a0.0.1
"""

import os.path

from modual.get_question import get_questions
from modual.question_randomizer import student_learning


def main(is_get_question: bool):
    print(""""
    
By using this program you understand that any bug created by abusing it is your own fault

 ██▓     █    ██ ▒██   ██▒ █    ██  ██▀███ ▓██   ██▓ ██ ▄█▀▄▄▄       ██▀███   ███▄ ▄███▓ ▄▄▄
▓██▒     ██  ▓██▒▒▒ █ █ ▒░ ██  ▓██▒▓██ ▒ ██▒▒██  ██▒ ██▄█▒▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄
▒██░    ▓██  ▒██░░░  █   ░▓██  ▒██░▓██ ░▄█ ▒ ▒██ ██░▓███▄░▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄
▒██░    ▓▓█  ░██░ ░ █ █ ▒ ▓▓█  ░██░▒██▀▀█▄   ░ ▐██▓░▓██ █▄░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██
░██████▒▒▒█████▓ ▒██▒ ▒██▒▒▒█████▓ ░██▓ ▒██▒ ░ ██▒▓░▒██▒ █▄▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒
░ ▒░▓  ░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ██▒▒▒ ▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░
░ ░ ▒  ░░░▒░ ░ ░ ░░   ░▒ ░░░▒░ ░ ░   ░▒ ░ ▒░▓██ ░▒░ ░ ░▒ ▒░ ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░
  ░ ░    ░░░ ░ ░  ░    ░   ░░░ ░ ░   ░░   ░ ▒ ▒ ░░  ░ ░░ ░  ░   ▒     ░░   ░ ░      ░     ░   ▒
    ░  ░   ░      ░    ░     ░        ░     ░ ░     ░  ░        ░  ░   ░            ░         ░  ░
                                            ░ ░
""")
    if is_get_question:
        get_questions(path_to_pdf=input('path to exercise pdf: '), page_to_ignore= [0,1,2])
    student_learning()


if __name__ == '__main__':
    if not os.path.isfile(r'./question_data/question.json'):
        main(True)
        exit()
    main(False)