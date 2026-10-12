from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/math/<int:number>')
def math(number):
    return f"The number is {number*3}"

@app.route('/second')
def second():
    return render_template('second.html')

if __name__ == "__main__":
    app.run(debug=True)