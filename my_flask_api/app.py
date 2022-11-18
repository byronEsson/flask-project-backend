from flask import Flask, request, abort
from model import findKeyWords
import json
app = Flask(__name__) 


@app.route('/model', methods=['POST'])
def model():
    try:
        words = request.json  
        return json.dumps({'keywords': findKeyWords(words['positive'], words['negative'] )})
    except:
        abort(400)

@app.route('/')
def home():
    return {'greeting': 'hello'}

@app.route("/*")
def not_found():
    abort(404)

@app.errorhandler(400)
def handle_400(e):
    return 'Request object not formatted correctly', 400

if __name__ == '__main__':
    app.run(threaded=True, port=5000)