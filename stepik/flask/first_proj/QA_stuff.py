from flask import Flask  # импорт

app = Flask(__name__)  # подключение сервера


@app.route('/')
@app.route('/index')
def index():
    return """Hello world"""


@app.route('/test-case')
def test_case():
    return 'tester'


@app.route('/calculate/<int:a>/<int:b>')  # переменные в маршрутах
def calculator(a, b):
    return str(a ** b)


@app.route('/<string:x>/<string:y>/<string:z>/<string:o>')
@app.route('/<path:x>')
@app.route('/lesson/<y>/step/<o>')
def tester():
    return 'GOOD JOB'


operations = ('+', ':', '**', '-', '*')


@app.route('/<val>/')
def browser_calc(val):
    val = val.replace(':', '/')
    return str(eval(f'{val}'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
