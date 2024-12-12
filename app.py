from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Syria Hegemony Map!"

@app.route('/data')
def data():
    return jsonify({"message": "Data about the hegemony of groups in Syria"})

if __name__ == '__main__':
    app.run(debug=True)
