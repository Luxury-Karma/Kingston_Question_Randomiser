import json

from pypdf import PdfReader
import re


def get_pdf_text(pdf_path: str, page_to_ignore: list[int]) -> str:
    doc = PdfReader(pdf_path)
    text: str = ""
    for e in doc.pages:
        if e.page_number in page_to_ignore:
            print(f'ignoring page {e.page_number}')
            continue
        t = re.sub(r'Unclass – Cyber Training Unit', '', e.extract_text("text"))
        text += t
    return text


def get_question_split(text: str, word_to_split_sections: str) -> dict:
    """
     question_format: dict = {
        'question': str,
        'section': str,
        'answer': str,
        'question_index': int
    }
    :param text:
    :param word_to_split_sections:
    :return:
    """
    # Split text into sections
    sections = text.split(word_to_split_sections)
    questions = {}
    regex_chapter_title = r'^\d+: [A-Za-z ]+'

    for section in sections:
        # Match and capture the section title
        match = re.match(regex_chapter_title, section.strip())
        if match:
            section_title = match.group(0)
            print(f'Section Title: {section_title}')
        else:
            section_title = 'No title found'

        # Split the section by questions and remove empty strings
        section_questions = [q.strip() for q in re.split(r'\n\d+\.', section) if q.strip()]

        # Print the questions for each section
        question_index = 1
        section_questions.pop(0)
        for question in section_questions:
            question = question.replace('\n',' ')
            question_format = {
                'question': question,
                'section': section_title,
                'answer': '',
                'question_index': question_index
            }
            question_index +=1
            questions[f'Question_{question_index}_section_{section_title.replace(" ", "_")}'] = question_format

    return questions


def get_questions(path_to_pdf: str, page_to_ignore: list[int] = [], word_to_split_section: str = 'Section'):
    path_to_pdf = path_to_pdf.strip(r'"').strip(r"'")
    with open('.\\question_data\\question.json','w', encoding='utf-8') as f:
        json.dump(get_question_split(get_pdf_text(path_to_pdf, page_to_ignore), word_to_split_section), f)
        f.close()
