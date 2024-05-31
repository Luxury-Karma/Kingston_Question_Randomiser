import json


def make_it_word():
    data: dict = {}
    with open('./question_data/question.json') as f:
        data = json.load(f)
    full_file = ''
    last_section_known = ''
    for _, value in data.items():
        if last_section_known != value['section']:
            last_section_known = value['section']
            full_file += f'\n\n {value["section"].upper()} \n\n'
        new_line = f'#{value["question_index"]} {value["question"]}\n\t{value["answer"]}\n\n'
        full_file += new_line
    with open('./text_file.txt', 'w', encoding='utf-8') as f:
        f.write(full_file)