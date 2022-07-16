from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def backend():
    if request.is_json:
        data = request.get_json()       # "data" is in the form of a dictionary, with one key called 'data', and therefore the below
        text = data['data']
        output_text = "Hello " + text + "!"
        return output_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9010)
