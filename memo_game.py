from flask import Flask, render_template, request, redirect 
import os
import random
import memo_game_functions as mf

app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

def read_submit_form(request_form_dict):
#    print(request_form_dict)
    vocab_value = request_form_dict.getlist("vocab")
    draw_words = int(request_form_dict.getlist("num_pairs")[0])
    
    if len(vocab_value) == 0:
        vocab_value.append("default")
    if not draw_words:
        draw_words = 6
#    print(vocab_value)
#    print(draw_words)
    return vocab_value, draw_words

def generage_words_buttoms_attr(sel_list1, sel_list2):
    buttons_attr = []
    for i in range(0, len(sel_list1)):
        attr_dict1 = {
            'id': 1000+i,
            'name': sel_list1[i]
        }
        attr_dict2 = {
            'id': 2000+i,
            'name': sel_list2[i]
        }
        buttons_attr.append(attr_dict1)
        buttons_attr.append(attr_dict2)
    random.shuffle(buttons_attr)
    return buttons_attr

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global vocabulary_buttons
    global vocab_lists
    global draw_words

    draw_words = 6
    vocab_lists = ["default"] 

    vocabulary_buttons = mf.analyze_list_files() 

    if request.method == 'POST':
        vocab_lists, draw_words = read_submit_form(request.form)

    total_words = 0
    total_list1 = []
    total_list2 = []
    for item in vocabulary_buttons: 
        if item['vocab'] in vocab_lists:
            total_list1 += item['list1']
            total_list2 += item['list2']
            total_words += item['num_words']

#    print(total_list1)
    sel_list1, sel_list2 = mf.draw_elements(total_list1, total_list2, draw_words)
    buttons_game=generage_words_buttoms_attr(sel_list1, sel_list2)
    #mf.generate_layout()
    #mf.start_game()

    return render_template('index.html', title='Home', 
                            vocabulary_buttons=vocabulary_buttons, 
                            selected_lists=vocab_lists, nwords=total_words, draw=draw_words,
                            buttons_game=buttons_game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
