from flask import Flask, render_template ,url_for 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1> Hello World </h1>"

@app.route('/about', methods=['GET'])
def about():
    return "<h1> This is about page </h1>"

if __name__ == '__main__':
    app.run(debug=True)  