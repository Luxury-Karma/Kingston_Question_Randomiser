import json
from docx import Document
from modual.text_color import text_color


def make_it_word_too(path_to_word):
    data = {}
    print(f'{text_color("INFO")}loading answer file at ./question_data/question.json{text_color("base")}')
    with open('./question_data/question.json') as f:
        data = json.load(f)
    print(f'{text_color("INFO")}Starting to build the word file{text_color("base")}')
    doc = Document()

    # Initialize variables for ToC
    toc = doc.add_paragraph()
    toc.add_run("Table of Contents").bold = True
    toc.add_run("\n\n")

    last_section_known = ''
    index = []

    for _, value in data.items():
        if last_section_known != value['section']:
            last_section_known = value['section']
            doc.add_heading(value['section'].upper(), level=1)
            index.append(value['section'])

        doc.add_paragraph(f'{value["question_index"]}. {value["question"]}')
        doc.add_paragraph(f'\t{value["answer"]}\n')

    # Add index to ToC
    for section in index:
        toc.add_run(section).bold = True
        toc.add_run("\n")

    # Save the document
    doc.save(path_to_word)
    print(f"{text_color('backup')}Word document saved at {path_to_word}{text_color('base')}")
