from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    # Call your recommendation room function with data
    response = {'output': 'Your room recommendation'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
