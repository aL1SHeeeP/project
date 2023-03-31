from flask import render_template, flash, url_for, redirect, request
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    title = 'Главная страница'
    return render_template('index.html', title=title)


@app.route('/languages/<type>/<grade>')
def languages(type, grade):
    title = 'Иностранные языки'
    if type == 'english':
        teachers = EnglishTeachers.query.all()
        pupils_raw = Pupils.query.filter_by(grade=grade).join(EnglishGroups, EnglishGroups.group_id == Pupils.eng_group).add_columns(
            Pupils.pupil_id, Pupils.pupil_name, Pupils.grade, Pupils.eng_group.label('gr_id'), EnglishGroups.group_name.label('gr_name')).all()
        print(pupils_raw)
        pupils = {(x[4]): [] for x in pupils_raw}
        groups_names = {x[4]: x[5] for x in pupils_raw}
        for p in pupils_raw:
            pupils[(p[4])] += [(p[1], p[2])]
        print(pupils)
    elif type == 'secondlang':
        teachers = SecondLangTeachers.query.all()
        gr_db = SecondLangGroups
        gr_id = 'second_group'

    grade_title = f'Список групп {grade} классов'
    return render_template('languages.html', title=title, grade_title=grade_title, teachers=teachers, pupils=pupils, groups_names=groups_names,
                           type=type)


@app.route('/profile')
def profile():
    # обработка формы
    # if request.method == 'POST':
    #     r = request.form.to_dict()
    #     title = 'Сохранение УП'
    #     return render_template('profile_test.html', title=title, r=r)

    # вывод формы
    title = 'Профильное обучение'
    subjects_general = Subjects.query.filter_by(subj_general=1).all()
    subjects = Subjects.query.filter_by(subj_general=0).all()
    return render_template('profile.html',
                           title=title,
                           subjects_general=subjects_general,
                            subjects=subjects)




@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Регистрация'
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pwd = form.password.data
        pwd2 = form.password2.data
        if pwd != pwd2:
            flash("Пароль не совпадает с подтверждением!")
        else:
            user = Users(name=name, email=email, passwd=pwd)
            db.session.add(user)
            db.session.commit()
            flash("Успешная регистрация!")
            return redirect(url_for('index'))
    return render_template('register.html', title=title, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Вход в аккаунт'
    form = LoginForm()
    if form.validate_on_submit():
        usname = form.name.data
        psw = form.password.data
        user = Users.query.filter_by(name=usname).first()
        if not(user):
            flash("Неверное имя пользователя")
        elif psw != user.passwd:
            flash("Неверный пароль")
        else:
            flash("Вы вошли на сайт")
            return redirect(url_for('index'))
    return render_template('login.html', title=title, form=form)