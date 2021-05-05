from flask import Flask, render_template, redirect, make_response, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key_1'


@app.route('/')
@app.route('/index')
def index():
    return '<a href="/slider">Начать показ</a><br><a href="/add_type">Добавить</a>'


@app.route('/slider')
def slider():
    return '''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"></head><body><div 
    class="main_div"></div><script src="/static/js/main.js"></script></body></html>'''


@app.route('/add_type', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return '''<form action="/add_type" method="POST" enctype="multipart/form-data"><input 
        type="file" name="file"><br><br><button type="submit">Загрузить</button></form>'''
    if request.method == 'POST':
        file = request.files['file']
        name = file.filename
        with open('uploaded/' + name, 'wb') as f:
            f.write(file.read(1024 * 1024 * 200))
        return redirect('/')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
