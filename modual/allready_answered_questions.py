import json
import re


def change_answer_to_question(question_to_find: str, answer_to_place: list[str], question_dict: dict):
    for key, values in question_dict.items():
        if question_to_find not in values['question']:
            continue
        answer = ''
        for e in answer_to_place:
            answer += f' {e}'
        values['answer'] = answer
    print(f'Answer for question : {question_to_find} was sett and formatted to : {answer_to_place}')
    return question_dict


def convert_to_json(path_of_original_file):
    """
    BE SUR THE QUESTION IS ONLY ON THE FIRST LINE. Everything else will be in the answer part
    Convert a text file into a premade json. The format need to be :
    EXACT QUESTION(enter)
    answer(enter)
    (enter)
    ...
    :param path_of_original_file:
    :return:
    """
    text = ''
    question_dict: dict = {}
    with open('question_data/question.json', 'r', encoding='utf-8') as f:
        question_dict = json.load(f)
    reg = r'\n\s*\n'
    with open(path_of_original_file,'r', encoding='utf-8') as f:
        text = f.read()
    # split question and answer
    split = re.split(reg, text)
    for e in split:
        question_answer = e.split('\n')
        if len(question_answer)<2:
            continue
        question_dict = change_answer_to_question(question_answer[0], question_answer[1:], question_dict)
