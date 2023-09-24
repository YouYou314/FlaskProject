from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return f"The temperature {celsius} Celsius is equivalent to {fahrenheit} Fahrenheit."


if __name__ == '__main__':
    app.run()
