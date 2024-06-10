from flask import Flask, request, render_template, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        if 'number1' not in request.form or 'number2' not in request.form or 'operation' not in request.form:
            return "Missing input fields"
        
        number1 = request.form.get('number1')
        number2 = request.form.get('number2')

        if not number1 or not number2:
            return "Please enter valid numbers"
            flask.flash(message, category='message')

        number1 = float(number1)
        number2 = float(number2)

        operation = request.form.get('operation')
        operations = ('add', 'subtract', 'multiply','divide')

        if operation not in operations:
            return "Invalid operation"

        if operation == 'add':
            result = int(number1 + number2)

        elif operation == 'subtract':
            result = int(number1 - number2)
        elif operation == 'multiply':
            result = int(number1 * number2)
        elif operation == 'divide':
            if number2 == 0:
                result = "Cannot divide by 0"
            else:
                result = (number1 / number2)
        else:
            result = "Incorrect operation"

        return render_template('index.html', result=result, operation=operation.lower())
    except Exception as e:
        return str(e)
 
if __name__ == '__main__':
    app.run(debug=True)   