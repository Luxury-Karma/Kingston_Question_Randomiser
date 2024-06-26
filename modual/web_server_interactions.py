from flask import Flask, render_template, request, jsonify
from modual.question_randomizer import (__get_questions, __get_new_questions, __get_random_new_question_key,
                                        _apply_answer_to_question, __save_modified_json)

app = Flask(__name__, template_folder='../html')

"""
Should not be using global but fuck it its quicker and I don't want to use more time to do this then needed.
if we need to make a real server interacting and all I'll use something else 
"""

all_question: dict = {}
new_question: dict = {}
all_keys: list = []
active_key = ''
path_to_question_file = ''


@app.route('/')
def home_page():
    global new_question
    question = new_question[active_key]
    remaining_questions = len(all_keys)  # Get the count of remaining questions
    return render_template('web_app_version.html', question=question, remaining_questions=remaining_questions)


@app.route('/submit', methods=['POST'])
def submit():
    global active_key, all_question, new_question, all_keys
    data = request.get_json()
    answer = data.get('answer')

    if not answer or answer.strip().strip('\n').strip(' ') == '':  # no answer received
        print('its okay you\'ll get it next time !')
        active_key = __get_random_new_question_key(all_keys, len(all_keys))

    else:  # answer received
        # Process the current answer
        print(f"answer of {active_key} is : {answer}")
        all_question = _apply_answer_to_question(all_question, active_key, answer)

        # next question
        new_question.pop(active_key)
        all_keys.remove(active_key)
        active_key = __get_random_new_question_key(all_keys, len(all_keys))

    # apply to webpage
    next_question_data = new_question[active_key]

    # Calculate remaining questions count
    remaining_questions = len(all_keys)

    __save_modified_json(path_to_question_file, all_question)  # save the question

    # Return the message, next question, and remaining questions count as JSON
    response = {
        "message": "Your answer has been submitted!",
        "next_question": {
            "question": next_question_data['question'],
            "section": next_question_data['section'],
            "question_index": next_question_data['question_index'],
            "answer": next_question_data['answer']
        },
        "remaining_questions": remaining_questions
    }
    return jsonify(response)


def run_web_server(debug, port, path_to_questions):
    global all_question, new_question, all_keys, active_key, path_to_question_file
    all_question = __get_questions(path_to_questions)
    new_question = __get_new_questions(all_question)
    all_keys = list(new_question.keys())
    active_key = __get_random_new_question_key(all_keys, len(all_keys))
    path_to_question_file = path_to_questions

    app.run(debug=debug, host='127.0.0.1', port=port)
