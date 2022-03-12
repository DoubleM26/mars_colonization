from flask import Flask, url_for, request, render_template, redirect

from data import db_session
from forms.login import LoginForm
from forms.register import RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.user import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        print(jobs)
    else:
        jobs = []
    return render_template("index.html", jobs=jobs)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# @app.route("/index/<title>")
# def index(title):
#     return render_template("base.html", title=title)


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


@app.route("/distribution")
def distribution():
    astronauts = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', astronauts=astronauts, str=str)


@app.route("/table/<sex>/<age>")
def table(sex, age):
    age = int(age)
    if age < 21:
        img = "../../static/img/kid.jpg"
    else:
        img = "../../static/img/adult.jpg"

    color = round(age * 255 / 100)
    color = 255 - color
    if sex == "female":
        color = f"rgb(255, {color}, {color})"
    else:
        color = f"rgb({color}, {color}, 255)"

    return render_template('table.html', img=img, color=color)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
