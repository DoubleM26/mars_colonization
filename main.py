from flask import Flask, url_for, request, render_template, redirect
from forms.login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof:
        img = "..\static\img\инженер.png"
    elif "строитель" in prof:
        img = "..\static\img\строитель.png"
    else:
        img = "..\static\img\другие.png"
    if prof in ["врач", "химик", "физик", "астронавт"]:
        text = "Научные симуляторы"
    else:
        text = "Инженерные тренажеры"
    return render_template("training.html", img=img, text=text)


@app.route("/list_prof/<li>")
def list_prof(li):
    return render_template("list_prof.html", li=li)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        "title": "Анкета",
        "surname": "Яблоков",
        "name": "Андрей",
        "education": "Среднее",
        "profession": "Астронавт",
        "sex": "вечером",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("auto_answer.html", data=data, title=data["title"])


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index/главная')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route("/distribution")
def distribution():
    astronauts = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', astronauts=astronauts, str=str)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
