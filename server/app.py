#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Home route displaying the application title
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string in the console and display it in the browser
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  
    return param  

# Route to display a list of numbers
@app.route('/count/<int:param>')
def count(param):
    numbers = [str(i) for i in range(param)]
    return '\n'.join(numbers) + '\n'  # Ensure the result ends with a newline character

# Route to perform basic arithmetic operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
