from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/dhruv')
def hello_dhruv():
    return 'Hello, Dhruv!'

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/post_data', methods=['POST'])
def post_data():
    req_data = request.get_json()
    print("Data received from frontend:", req_data)
    # Assuming db and retreive_all_found_items are implemented correctly
    # You can interact with Firebase here
    return jsonify({"message": "Data received successfully"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
