import json
import os.path
import random
from modual.text_color import text_color


def __get_questions(question_path: str) -> dict:
    if os.path.isfile(question_path):
        with open(question_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                print('ERROR IN LOADING THE QUESTION JSON FILE')
                return {}
    print('NOT A VALID PATH')
    return {}


def __get_new_questions(questions: dict) -> dict :
    new_question = {}
    for key, value in questions.items():
        ans_val = value['answer'].replace(' ', '')
        if ans_val != '':
            continue
        new_question[key] = value
    return new_question


def __get_random_new_question_key(dictionary_keys: list, question_amount: int):
    return dictionary_keys[random.randint(0, question_amount)]


def __answer_question(new_question: dict, key_chosen: str):
    print(f'SECTION : {new_question[key_chosen]["section"]}')
    print(f'Question number: {new_question[key_chosen]["question_index"]}')
    print(f'Question : {new_question[key_chosen]["question"]}')
    return __input_sanitization('Enter your answer. If unknown just let empty. : \n')


def _apply_answer_to_question(full_question_dictionary: dict, key_chosen: str, answer_chosen: str):
    full_question_dictionary[key_chosen]['answer'] = answer_chosen
    return full_question_dictionary


def __save_modified_json(path, full_question_dict:dict):
    print(f'{text_color("INFO")}question received and will be save{text_color("base")}')
    if not os.path.isfile(path):
        print(f'{text_color("ERROR")} IN JSON ANSWER FILE PATH DO NOT CONTINUE ANSWERING{text_color("base")}')
    with open(path,'w',encoding='utf-8') as f:
        json.dump(full_question_dict,f)
        f.close()
    print(f"{text_color('backup')}applied. You can safely quit if needed\n\n{text_color('base')}")


# This is bad practice of not really looking what is in the input but I also want as much liberty as possible for us to answer
def __input_sanitization(prompt: str) -> str:
    user_input = input(prompt)
    if type(user_input) != str:
        user_input = str(user_input)
    return user_input


def student_learning(path_to_json: str = './question_data/question.json'):
    full_questions = __get_questions(path_to_json)
    new_questions = __get_new_questions(full_questions)
    len_n_question = len(new_questions)
    keys = list(new_questions.keys())
    while len(keys) > 0:
        print(f"The total question left are : {len(keys)}")
        question_key = __get_random_new_question_key(keys,len_n_question)
        answer = __answer_question(new_questions, question_key)
        if answer.replace(' ', '') == '':
            print('its okay we will come back later !')
            continue
        full_questions = _apply_answer_to_question(full_questions, question_key, answer)
        __save_modified_json(path_to_json, full_questions)
        keys.remove(question_key)
        new_questions.pop(question_key, None)  # kinda useless step. if error we will remove I just like removing it from the question pool insted of ignoring it


