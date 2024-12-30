from flask import Flask, send_file
from ClassRoster import get_class_roster

app = Flask(__name__)

@app.route('/')
def index():
    students = get_class_roster()
    # Instead of render_template, use send_file to serve index.html
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)