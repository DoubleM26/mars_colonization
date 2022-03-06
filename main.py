from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route("/landscapes")
def landscapes():
    return f"""
    <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
</head>
<body>
<h1>Пейзажи Марса</h1>
<div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active" data-bs-interval="10000">
      <img src="{url_for('static', filename='img/landscape_1.jpg')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="{url_for('static', filename='img/landscape_2.jpg')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/landscape_3.jpg')}" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
</body>
</html>
    """


@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name == "марс":
        phrases = ["На ней много необходимых ресурсов", "На ней есть вода и атмосфера",
                   "На ней есть небольшое магнитное поле", "Она красива!"]
    elif planet_name == "венера":
        phrases = ["Её можно увидеть с Земли", "Весить на ней мы будем меньше.",
                   "На её поверхности расположены три плоскогорья.", "Она прекрасна!"]
    else:
        phrases = ["нет описания"]
    content = f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        '''

    classes = ["alert alert-danger", "alert alert-primary", "alert alert-secondary", "alert alert-success"]
    for i in range(len(phrases)):
        content += f'''
                        <div class="{classes[i]}" role="alert">
                          {phrases[i]}
                        </div> '''
    content += "</body></html>"
    return content


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h3>Претендента на участие в миссии {nickname}</h3>
                        <div class="alert alert-success" role="alert">
                          Поздравляем! Ваш рейтинг после {level} этапа отбора
                        </div>
                        <p>составляет {rating}</p>
                        <div class="alert alert-warning" role="alert">
                          Поздравляем!
                        </div>
                      </body>
                    </html>'''


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
