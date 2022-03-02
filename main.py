from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/promotion')
def promotion():
    promos = ["Человечество вырастает из детства.",
              "Человечеству мала одна планета.",
              "Мы сделаем обитаемыми безжизненные пока планеты.",
              "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(promos)


@app.route('/image_mars')
def image():
    content = "<h1>Жди нас, Марс!</h1>"
    content += f'''<img src="{url_for('static', filename='mars_image.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
    return content


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
