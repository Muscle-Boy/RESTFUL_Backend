from re import X
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/backend', )
def backend():
    return '3'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010)