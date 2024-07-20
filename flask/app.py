from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    input_string = data.get('input', '')
    reversed_string = input_string[::-1]
    return jsonify({'output': reversed_string})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
