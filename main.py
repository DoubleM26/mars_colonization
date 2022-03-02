from flask import Flask, url_for, request

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
    content += f'''<img src="{url_for('static', filename='img/mars_image.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
    return content


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_image.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <div class="header_container">
                        <h1>Анкета претендента</h1>
                        <h2>на участие в миссии</h2>
                    </div>
                    <div>
                        <form class="login_form" method="post">
                            <input class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                            <input class="form-control" id="name" placeholder="Введите имя" name="name">
                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                            <div class="form-group">
                                <label for="classSelect">Какое у вас образование</label>
                                <select class="form-control" id="classSelect" name="education">
                                  <option>Начальное</option>
                                  <option>Среднее</option>
                                  <option>Профессиональное</option>
                                </select>
                             </div>
                            <div class="form-group">
                                <label for="form-check">Какие у вас есть профессии</label>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="researchEngineer" name="profession">
                                  <label class="form-check-label" for="male">
                                    инженер-исследователь
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="pilot" name="profession">
                                  <label class="form-check-label" for="male">
                                    пилот
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="builder" name="profession">
                                  <label class="form-check-label" for="male">
                                    строитель
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="doctor" name="profession">
                                  <label class="form-check-label" for="male">
                                    врач
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="climatologist" name="profession">
                                  <label class="form-check-label" for="male">
                                      климатолог
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="radiation protection specialist" name="profession">
                                  <label class="form-check-label" for="male">
                                      специалист по радиационной защите
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input type="checkbox" class="form-check-input" id="astrogeologist" name="profession">
                                  <label class="form-check-label" for="male">
                                      астрогеолог
                                  </label>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="form-check">Укажите пол</label>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                  <label class="form-check-label" for="male">
                                    Мужской
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                  <label class="form-check-label" for="female">
                                    Женский
                                  </label>
                                </div>
                            </div>

                            <div class="form-group">
                                <label for="about">Почему вы хотите принять участие в миссии?</label>
                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                <label class="form-check-label" for="acceptRules">Готов остаться на Марсе</label>
                            </div>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                  </body>
                </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
