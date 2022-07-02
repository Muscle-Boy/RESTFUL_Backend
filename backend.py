from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def backend(data):
#     text = request.form['texts']
#     text = '3'
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010)
