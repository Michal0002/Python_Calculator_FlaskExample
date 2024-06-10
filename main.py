from flask import Flask, request, render_template

def calculations():
    number1 = float(request.form['number1'])
    number2 = float(request.form['number2'])

    operation = request.form['operation']

    if operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        result = number1 / number2
    else:
        result = "Nieprawidłowa operacja"

    