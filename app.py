from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def mod_exp(base, exponent, modulus):
    """
    Fast exponentiation algorithm
    """
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])  # Update method to support POST
def calculate():
    if request.method == 'POST':  # Ensure the request method is POST
        base = int(request.form['base'])
        exponent = int(request.form['exponent'])
        modulus = int(request.form['modulus'])
        result = mod_exp(base, exponent, modulus)
        return redirect(url_for('show_result', result=result))
    else:
        return redirect(url_for('index'))  # Redirect to index page if method is not POST

@app.route('/result/<result>')
def show_result(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
