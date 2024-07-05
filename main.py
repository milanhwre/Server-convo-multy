from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    convo_id = request.form['convo_id']
    tokens_file = request.files['tokens_file']
    np_file = request.files['np_file']
    hater_name = request.form['hater_name']
    speed = request.form['speed']

    # फाइल्स को सेव करें
    tokens_file_path = os.path.join('uploads', tokens_file.filename)
    np_file_path = os.path.join('uploads', np_file.filename)
    tokens_file.save(tokens_file_path)
    np_file.save(np_file_path)

    # यहाँ पर और प्रोसेसिंग कर सकते हैं
    # ...

    return f'Submitted details: Convo ID: {convo_id}, Hater Name: {hater_name}, Speed: {speed}'

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(host='0.0.0.0', port=55665)
