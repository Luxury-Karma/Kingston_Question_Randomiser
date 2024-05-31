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



This script is to help into doing question and learn without being block in the same modual or need
to change question by your self.

Author: Luxury_Karma
Date: 2024-05-31
Version: a0.0.1
"""

import os.path
from modual.get_question import get_questions
from modual.question_randomizer import student_learning
from modual.allready_answered_questions import convert_to_json
from modual.text_color import text_color
from modual.port_question_answer_to_word import make_it_word_too
import argparse




def parser():
    par = argparse.ArgumentParser(prog='Luxury_karma', description='A tiny script to help me studie and maybe you',
                                  epilog='If you need help contact me if you have the mean too')
    par.add_argument('-aq', '--already_answered_question', required=False, type=str,
                     help='The path to a formatted way of already answer question so you do not need to redo them again')
    par.add_argument('-r', '--resset', required=False, action='store_true',
                     help='If you action this it will redo the full process of making the json question file and you '
                          'WILL loose it if its not back up or allready exist')
    par.add_argument('-pdf', '--path_to_pdf', required=False, type=str,
                     help='Store the path to the pdf file we need to convert the question too. If needed to program '
                          'will ask an input if this parameter is not there')
    par.add_argument('-f', '--finalise', required=False, type=str,
                     help='If you want to make the word file this is the parameter for you! also don\'t forget its a word file path you need')
    par.add_argument('-i', '--ignore', required=False, type=list,
                     help='will modify the ignore page part of the script (base value [0,1,2])')
    return par


def main(is_get_question: bool):
    print(f""""
{text_color('ERROR')}By using this program you understand that any bug created by abusing it is your own fault{text_color('INFO')}

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
{text_color('TITLE')}                                                                                                                                                                       
   ____                                                                    ________                           ___                                                      
  6MMMMb                                      68b                          `MMMMMMMb.                         `MM                         68b                          
 8P    Y8                               /     Y89                           MM    `Mb                          MM                         Y89                          
6M      Mb ___   ___   ____     ____   /M     ___   _____  ___  __          MM     MM    ___   ___  __     ____MM   _____  ___  __    __  ___   ____     ____  ___  __ 
MM      MM `MM    MM  6MMMMb   6MMMMb\/MMMMM  `MM  6MMMMMb `MM 6MMb         MM     MM  6MMMMb  `MM 6MMb   6MMMMMM  6MMMMMb `MM 6MMb  6MMb `MM  6MMMMb\  6MMMMb `MM 6MM 
MM      MM  MM    MM 6M'  `Mb MM'    ` MM      MM 6M'   `Mb MMM9 `Mb        MM    .M9 8M'  `Mb  MMM9 `Mb 6M'  `MM 6M'   `Mb MM69 `MM69 `Mb MM MM'    ` 6M'  `Mb MM69 " 
MM      MM  MM    MM MM    MM YM.      MM      MM MM     MM MM'   MM        MMMMMMM9'     ,oMM  MM'   MM MM    MM MM     MM MM'   MM'   MM MM YM.      MM    MM MM'    
MM      MM  MM    MM MMMMMMMM  YMMMMb  MM      MM MM     MM MM    MM        MM  \M\   ,6MM9'MM  MM    MM MM    MM MM     MM MM    MM    MM MM  YMMMMb  MMMMMMMM MM     
YM      M9  MM    MM MM            `Mb MM      MM MM     MM MM    MM        MM   \M\  MM'   MM  MM    MM MM    MM MM     MM MM    MM    MM MM      `Mb MM       MM     
 8b    d8   YM.   MM YM    d9 L    ,MM YM.  ,  MM YM.   ,M9 MM    MM        MM    \M\ MM.  ,MM  MM    MM YM.  ,MM YM.   ,M9 MM    MM    MM MM L    ,MM YM    d9 MM     
  YMMMM9     YMMM9MM_ YMMMM9  MYMMMM9   YMMM9 _MM_ YMMMMM9 _MM_  _MM_      _MM_    \M\`YMMM9'Yb_MM_  _MM_ YMMMMMM_ YMMMMM9 _MM_  _MM_  _MM_MM_MYMMMM9   YMMMM9 _MM_    
    MM                                                                                                                                                                 
    YM.                                                                                                                                                                
     `Mo                                                                                                                                                               
{text_color('base')}

""")
    arg = parser().parse_args()

    if is_get_question or arg.resset:
        page_to_ignore = arg.ignore if arg.ignore else [0, 1, 2]
        path_to_pdf = arg.path_to_pdf if arg.path_to_pdf else input('path to exercise pdf: ')
        get_questions(path_to_pdf=path_to_pdf, page_to_ignore=page_to_ignore)

    if arg.already_answered_question:
        path = arg.already_answered_question.strip('"').strip("'")
        convert_to_json(path)
    if arg.finalise:
        make_it_word_too(arg.finalise)
        print(f"{text_color('TITLE')}Good job hope it went well!")
        exit()

    student_learning()


if __name__ == '__main__':
    if not os.path.isfile(r'./question_data/question.json'):
        main(True)
    main(False)
