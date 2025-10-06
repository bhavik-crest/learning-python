from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    # return "Welcome to the Flask App!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}"
    return '''
        <form method="post">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)